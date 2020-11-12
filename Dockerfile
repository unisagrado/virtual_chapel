FROM python:3.9-slim-buster

ARG A_SECRET_KEY=super-secret-key-of-the-app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
ENV SECRET_KEY=${A_SECRET_KEY}}

# set timezone 
ENV TIME_ZONE=UTC
ENV TZ=$TIME_ZONE
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install mysqlclient
RUN apt-get update \ 
    && apt-get install -y python3-dev default-libmysqlclient-dev build-essential

RUN pip install --upgrade pip

RUN mkdir virtual_chapel

WORKDIR virtual_chapel

COPY requirements.txt manage.py ./

RUN pip install -r requirements.txt

COPY ./chapel ./chapel
COPY ./.docker/entrypoint.sh /bin/entrypoint.sh

RUN python manage.py test

EXPOSE $PORT

ENTRYPOINT ["/bin/entrypoint.sh"]