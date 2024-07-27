FROM python:3.13-slim

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
    python3-dev \
    apt-utils \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools
RUN pip install \
    cython==0.29.35 \
    numpy==1.24.3 \
    pandas==2.0.1 \
    pystan==3.7.0

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8080