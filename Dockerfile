#imagen de python
FROM python:3.10-slim-bullseye

#Crea un usuario llamado flaskapp
RUN useradd --create-home --home-dir /home/flaskapp flaskapp

#Directorio dentro del contenedor donde se ejecutaran los archivos
WORKDIR /home/flaskapp

USER flaskapp
RUN mkdir app

COPY ./app ./app
COPY ./app.py .

ADD requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt


#Numero de puerto
EXPOSE 5000

# Especificar el comando a ejecutar cuando se inicie el contenedor
CMD [ "python", "./app.py" ]