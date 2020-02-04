FROM python:3.6

WORKDIR /app

ADD setup.py /app
ADD flask-env.sh /app
ADD run.py /app

COPY . /app

RUN ["chmod", "+x", "/app/flask-env.sh"]
RUN /app/flask-env.sh
RUN pip install -e .

EXPOSE 80
ENTRYPOINT ["python3", "run.py"]
