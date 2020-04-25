FROM node:12.16.2-alpine3.9

RUN mkdir -p /app/monitor
WORKDIR /app/monitor

ADD ./monitor /app/monitor/package.json
# ADD ./monitor /app/monitor/yarn.lock

RUN apk update

CMD yarn install && yarn build