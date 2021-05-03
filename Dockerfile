FROM python:3.8

WORKDIR /code/app

COPY /app .

WORKDIR /code

COPY /requirements.txt .

COPY /config.py .

RUN pip install -r requirements.txt

COPY /run.py .