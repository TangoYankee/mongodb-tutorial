FROM python:3.6


WORKDIR /app

COPY setup.py /app
COPY flask-env.sh /app

COPY . /app

RUN pip install -e .
RUN source flask-env.sh

ADD run.py /app

EXPOSE 5000
CMD ["python3", "run.py"]
