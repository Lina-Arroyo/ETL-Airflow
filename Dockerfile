FROM apache/airflow:2.5.0-python3.10

USER root

RUN apt-get update

USER airflow

ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/"
COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY . .
