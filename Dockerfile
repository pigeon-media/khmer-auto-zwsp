FROM python:3.8.1

RUN apt-get update

RUN apt-get install python3-icu


RUN pip install --no-binary=:pyicu: pyicu

RUN pip install Flask

WORKDIR /usr/src/app

COPY . .

EXPOSE 5000

CMD [ "python", "server.py" ]

