FROM python:3.6-alpine

RUN apk update && \
    apk add g++ && \
    pip install -U pip

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app