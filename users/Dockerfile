FROM python:3.7-slim-buster

COPY requirements.txt /users/requirements.txt
WORKDIR /users

RUN pip3 install --no-cache-dir -r requirements.txt --verbose

COPY . /users

EXPOSE 5000

CMD bash -c "python manage.py --host=0.0.0.0 port=5000"