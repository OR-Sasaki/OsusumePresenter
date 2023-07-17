FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja_JP
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install -upgrade pip
RUN pip install --upgrade setuptools

RUN pip install -U discord.py