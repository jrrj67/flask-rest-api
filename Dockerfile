FROM python:3.8

WORKDIR /code/app

COPY /app .

RUN pip install -r requirements.txt

WORKDIR /code

COPY /run.py .