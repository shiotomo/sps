FROM python:3.7.7-alpine3.11

RUN mkdir /app
WORKDIR /app

ADD Pipfile /app
ADD Pipfile.lock /app

RUN apk update

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system

ADD . /app

CMD pipenv run service
