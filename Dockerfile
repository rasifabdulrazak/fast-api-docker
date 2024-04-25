FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt

COPY ./app /app

WORKDIR /app

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt \
    && adduser --disabled-password --no-create-home django-user \
    && mkdir -p /vol/web/static \
    && mkdir -p /vol/web/media \
    && chown -R django-user:django-user /vol \
    && chown -R django-user:django-user /app \
    && chmod -R 755 /vol \
    && chmod -R 755 /app 

COPY ./app/static /vol/web/


