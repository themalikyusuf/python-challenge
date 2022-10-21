FROM python:alpine3.16

WORKDIR /app

COPY . .

ENV FLASK_APP hello

ENV FLASK_RUN_HOST 0.0.0.0

RUN python setup.py install

EXPOSE 5000

CMD ["flask", "run"]
