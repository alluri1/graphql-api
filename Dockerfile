FROM python:3.8
WORKDIR /app
ADD . /app
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "./rest_api.py" ]
#CMD ["python", "./graphql/graphql_api.py"]