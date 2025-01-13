FROM python:3.13.0-bookworm

WORKDIR /app

#COPY ./ /app/
COPY ./requirements.txt /app/requirements.txt
#
RUN pip install -r requirements.txt