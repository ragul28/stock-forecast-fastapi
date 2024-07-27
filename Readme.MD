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

* Trigger the forcast api
```sh
curl http://localhost:8080/forecast?stock=NVDA
```
