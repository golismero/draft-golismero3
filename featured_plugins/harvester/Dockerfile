FROM python:2.7-alpine

RUN apk update && \
    apk add g++ && \
    pip install -U pip

RUN mkdir /plugin && \
    wget https://github.com/laramies/theHarvester/archive/2.7.zip -O /plugin/2.7.zip && \
    unzip /plugin/2.7.zip -d /plugin/ && \
    mv /plugin/theHarvester-2.7 /plugin/theHarvester

COPY ./requirements.txt /plugin
COPY ./task.py /plugin
COPY ./theharvester_wrapper.py /plugin
RUN chmod +x /plugin/task.py && \
    pip install -r /plugin/requirements.txt

ENTRYPOINT ["/usr/local/bin/python2", "/plugin/task.py"]