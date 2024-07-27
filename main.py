import string
from fastapi import FastAPI, HTTPException
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

@app.post("/forecast", response_model=StockOut, status_code=200)
def get_forecast(stock: string):

    forecast_list = predict(stock)

    if not forecast_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": stock, "forecast": convert(forecast_list)}
    return response_object