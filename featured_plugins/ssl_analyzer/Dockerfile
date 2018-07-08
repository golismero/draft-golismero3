FROM python:3.6-slim

COPY requirements.txt /

RUN apt-get update && \
    apt-get install -y g++ testssl.sh

RUN pip install -r /requirements.txt && \
    pip install https://codeload.github.com/golismero/golismero-python-helpers/zip/master && \
    mkdir /plugin

RUN mkdir -p /app/featured_plugins && touch /app/featured_plugins/__init__.py
COPY ./ /app/featured_plugins/ssl_analyzer
RUN chmod +x /app/featured_plugins/ssl_analyzer/plugin_executor.py

WORKDIR /app
ENTRYPOINT ["/usr/local/bin/python", "/app/featured_plugins/ssl_analyzer/plugin_executor.py"]