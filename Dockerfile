FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR C:\Users\melan\PycharmProjects\pythonProject1\mysite

RUN pip install --upgrade pip
#RUN pip install gunicorn
#RUN apt-get install python-dev libxml2-dev libxslt-dev libpq-dev gcc
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN python -m pip install Jinja2

RUN python -m pip install django

COPY . .

CMD python mysite/manage.py runserver