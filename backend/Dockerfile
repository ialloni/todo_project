FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY req.txt .

EXPOSE 8000

RUN pip install -r req.txt

COPY . .

RUN chmod +x /app/scripts/*

