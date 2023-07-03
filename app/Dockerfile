FROM python:3.8.3-slim-buster

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install --upgrade pip

# copio el requirements.txt en la carpeta definida en WORKDIR
COPY ./requirements.txt . 

# instalo las dependencias
RUN pip install -r requirements.txt 

# copio todo donde estoy en la carpeta definida en WORKDIR
COPY . .


