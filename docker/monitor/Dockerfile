FROM node:12.16.2-alpine3.9

RUN mkdir -p /app/monitor
WORKDIR /app/monitor

RUN apk update

CMD yarn install && yarn build