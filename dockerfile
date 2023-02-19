FROM python:3.8.10
RUN pip install --upgrade pip

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

COPY reqirements.txt /code/
RUN pip install -r reqirements.txt

COPY . /code/
