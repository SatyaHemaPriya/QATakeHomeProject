FROM --platform=linux/amd64 python:3.11-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements* ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . ./

CMD exec uvicorn --port 8080 --host 0.0.0.0 main:app