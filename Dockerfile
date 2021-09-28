FROM python:3.9.0

WORKDIR /home/

RUN echo "reset_"

RUN git clone https://github.com/meanwo/meanwo.git

WORKDIR /home/meanwo/

RUN pip install -r requirements.txt

#RUN echo "SECRET_KEY=django-insecure-#1^h3bs&z18cztti#o8f8nh-#stp(qmwfk%wbrl@x#4%qkc+$k" > .env

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000


CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=June_29_1.settings.deploy && python manage.py migrate --settings=June_29_1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=June_29_1.settings.deploy June_29_1.wsgi --bind 0.0.0.0:8000"]

