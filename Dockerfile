FROM ubuntu

WORKDIR /dev/app

EXPOSE 8080

RUN apt-get update \
  && apt-get install python3 -y

COPY . .

ENTRYPOINT while true; do sleep 600; done
