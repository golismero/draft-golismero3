FROM python:3.6-alpine

COPY requirements.txt /

RUN apk update && \
    apk add g++ && \
    pip install -U pip

RUN pip install -r /requirements.txt && \
    mkdir /plugin

COPY ./task.py /plugin
RUN chmod +x /plugin/task.py

ENTRYPOINT ["/usr/local/bin/python", "/plugin/task.py"]