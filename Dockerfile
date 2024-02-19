FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

# install dependancies
RUN apt-get update -y && \
  apt-get install -y python3-pip python3-dev && \
  apt install -y git-all && \
  apt-get install -y libglib2.0-0

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --upgrade -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 5000

WORKDIR /app/backend

CMD [ "uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", " 5000"]