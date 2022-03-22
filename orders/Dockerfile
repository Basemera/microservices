FROM python:3.7-slim-buster

COPY requirements.txt /orders/requirements.txt
WORKDIR /orders

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /orders

EXPOSE 80

CMD bash -c "python manage.py --host=0.0.0.0 port=80"