FROM python:3.10.0-slim-buster

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1



RUN pip3 install --upgrade pip

COPY ./req.txt /app/req.txt

RUN pip3 install -r req.txt

CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000