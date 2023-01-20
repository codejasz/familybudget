# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/family_budget
COPY requirements.txt /usr/src/family_budget/
RUN pip install -r requirements.txt
COPY . /usr/src/family_budget/
