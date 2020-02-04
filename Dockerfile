FROM python:3.6.9

ADD setup.py /usr/src/app
ADD run.py /usr/src/app
WORKDIR /usr/src/app

EXPOSE 5000

RUN pip install -e .

CMD ["python3", "app.py"]
