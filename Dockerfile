FROM python:3.9-slim-buster

WORKDIR /api_labs/app

COPY app/ .

RUN pip install --no-cache-dir flask

EXPOSE 8080

CMD [ "python", "app.py" ]
