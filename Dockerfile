FROM python:3.12.1-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000