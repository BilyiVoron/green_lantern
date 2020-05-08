#FROM python:3.8.2-alpine
FROM python:3.8

COPY . /app

WORKDIR /app

#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "/app/wsgi.py"]