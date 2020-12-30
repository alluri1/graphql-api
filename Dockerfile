FROM python:3.8
WORKDIR /app
ADD . /app
RUN apt-get update
RUN pip install -r requirements.txt
CMD [ "python", "./api.py" ]