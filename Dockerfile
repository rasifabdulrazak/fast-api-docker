FROM python:3.9

COPY ./requirements.txt /tmp/requirements.txt

COPY ./app /app

WORKDIR /app

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt