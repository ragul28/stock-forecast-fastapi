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
    ticker = stock.strip().upper()
    
    # Check if ticker contains valid chars
    valid_chars = set(string.ascii_uppercase + string.digits + "^.-")
    if not all(c in valid_chars for c in ticker):
        raise HTTPException(status_code=400, detail="Invalid ticker symbol format.")

    prediction_list = predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    return response_object