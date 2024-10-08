FROM hub.hamdocker.ir/library/python:3.8
WORKDIR /django_app/
ADD ./requirements.txt ./
RUN pip install -r ./requirements.txt
ADD ./ ./
RUN python manage.py collectstatic --noinput
ENTRYPOINT ["/bin/sh", "-c" , "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 personal_portfolio.wsgi"]