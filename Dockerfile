FROM python:3.7.6-slim

RUN apt-get update && \
  apt-get -y install gcc && \
  rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "src/app.py"]
