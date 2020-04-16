FROM node:12.16.2-alpine3.9

RUN mkdir /app
WORKDIR /app

ADD ./monitor /app

RUN apk update
RUN yarn install

RUN yarn build