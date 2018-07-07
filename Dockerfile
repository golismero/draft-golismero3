from python:3.6-alpine

COPY requirements-dev.txt /app/requirements-dev.txt
WORKDIR /app

RUN pip install -r requirements-dev.txt

COPY . /app