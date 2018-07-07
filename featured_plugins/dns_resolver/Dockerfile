FROM python:3.6-alpine

COPY requirements.txt /

RUN apk update && \
    apk add g++ && \
    pip install -U pip

RUN pip install -r /requirements.txt && \
    pip install https://codeload.github.com/golismero/golismero-python-helpers/zip/master && \
    mkdir /plugin


RUN mkdir -p /app/featured_plugins && touch /app/featured_plugins/__init__.py
COPY ./ /app/featured_plugins/dns_resolver
RUN chmod +x /app/featured_plugins/dns_resolver/plugin_executor.py

WORKDIR /app
ENTRYPOINT ["/usr/local/bin/python", "/app/featured_plugins/dns_resolver/plugin_executor.py"]