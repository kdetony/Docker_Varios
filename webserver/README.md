# Webserver sobre un Contendor

Analizaremos 2 casos, para Nginx y para Apache, ambos partiendo de una forma general para llevarlo luego a un Dockerfile.

# Primer Caso Apache

Forma Manual
----------------------

Creamos la carpeta **/home/docker/apache**

En ella descargamos **Web-Bootstrap.tar.gz** 

La renombramos por web 

Descargamos la imagen: 

>**docker pull httpd**

Arrancamos el contenedor: 

>**docker run -dit -p 80:80 --name webapache httpd**

Copiamos el directorio: 

>**docker cp web webapache:/usr/local/apache2/htdocs/**

Y validamos :) 


Forma "Via Dockerfile" 
---------------------------


