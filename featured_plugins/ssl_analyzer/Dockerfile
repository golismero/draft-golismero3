FROM python:3.6-slim

COPY requirements.txt /

RUN apt-get update && \
    apt-get install -y testssl.sh && \

RUN pip install -r /requirements.txt && \
    mkdir /plugin

COPY ./ /plugin
RUN chmod +x /plugin/task.py

WORKDIR /plugin
ENTRYPOINT ["/usr/local/bin/python", "/plugin/plugin_executor.py"]