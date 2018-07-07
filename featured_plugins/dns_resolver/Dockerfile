FROM python:3.6-alpine

COPY requirements.txt /

RUN apk update && \
    apk add g++ && \
    pip install -U pip

RUN pip install -r /requirements.txt && \
    mkdir /plugin


COPY ./ /plugin
RUN chmod +x /plugin/plugin_executor.py

WORKDIR /plugin
ENTRYPOINT ["/usr/local/bin/python", "/plugin/plugin_executor.py"]