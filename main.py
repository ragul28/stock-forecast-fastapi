import string
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from model import convert, predict

app = FastAPI()

class StockIn(BaseModel):
    ticker: str

class StockOut(StockIn):
    forecast: dict

@app.get("/status")
def get_status():
    return {"status": "healthy"}

@app.get("/forecast", response_model=StockOut, status_code=200)
def get_prediction(stock: str = Query(..., description="Stock ticker symbol", min_length=1, max_length=5)):

    prediction_list = predict(stock)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": stock, "forecast": convert(prediction_list)}
    return response_object