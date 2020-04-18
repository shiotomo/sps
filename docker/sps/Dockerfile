FROM python:3.7

ENV LANG=ja_JP.UTF-8

RUN mkdir /app
WORKDIR /app

COPY ./Pipfile /app
COPY ./Pipfile.lock /app

RUN apt-get update
RUN apt-get install -y python-dev default-libmysqlclient-dev \
      task-japanese locales-all

COPY . /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system