FROM python:3.8.1

RUN apt-get update

RUN apt-get install python3-icu

RUN pip install --no-binary=:pyicu: pyicu

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

WORKDIR /usr/src/app

COPY . .

EXPOSE 5000

CMD ["waitress-serve", "--call", "server:create_app"]