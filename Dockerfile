FROM python:2.7
WORKDIR /home/app
COPY . .
CMD [ "python", "./manage.py","runserver","0.0.0.0:8080" ]