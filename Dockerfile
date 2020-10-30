FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

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

EXPOSE $PORT

ENTRYPOINT ["/bin/entrypoint.sh"]