# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

RUN apt-get install -y openssh-server

WORKDIR /app

COPY requirements.txt requirements.txt
COPY test.py test.py
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3"]