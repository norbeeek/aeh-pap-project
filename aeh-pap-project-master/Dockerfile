FROM python:3.10-slim

COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install -r requirements.txt

COPY . \app
WORKDIR \app
ENV FLASK_APP=main.py

EXPOSE 9000
CMD ["flask", "run", "--host=0.0.0.0", "--port=9000"]