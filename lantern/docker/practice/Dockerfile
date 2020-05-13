FROM python:3.8
LABEL email="email@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "app.py"]