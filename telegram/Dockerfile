FROM python:alpine

WORKDIR /app

COPY req.txt .
RUN pip install -r req.txt

COPY . .

CMD [ "python", "bot.py" ]