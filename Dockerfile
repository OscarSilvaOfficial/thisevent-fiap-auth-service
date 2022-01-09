FROM python:3.9.5

ENV DATABASE_URL=mysql+pymysql://root:admin@db/admin

RUN pip install gunicorn --upgrade pip

ADD . /customer-service-api
WORKDIR /customer-service-api

COPY . /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
EXPOSE 5001

CMD ["gunicorn", "--config=gunicorn.py", "run:app"]