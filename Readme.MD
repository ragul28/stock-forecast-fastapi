# Simple stock forecast app based on fastapi

## Setup

* Setup python virtual env & install packages
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

* Train model using prophet
```sh
python model.py train
```

* Run the fastapi for local testing
```sh
uvicorn main:app --reload --workers 1 --host 127.0.0.1 --port 8080
```

## Docker setup

Build & run service as container
```sh
docker build -t stock-forecast-api:v1 .
docker run -it -p 8080:8080 stock-forecast-api:v1
```

## Api endpoint

* Trigger the model training for stock
```sh
curl -X POST http://localhost:8080/train \
    -H "Content-Type: application/json" \
    -d '{"stock": "NVDA", "start_date": "2020-01-01"}'
```

* Trigger the forecast api
```sh
curl http://localhost:8080/forecast?stock=NVDA
```