from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/status")
def get_status():
    return {"status": "healthy"}
