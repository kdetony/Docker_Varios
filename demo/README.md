Construyendo imagen en base a aplicacion Flask
=====

Contruyendo imagen

> docker build -t imgbase . 

Construyendo contenedor

> docker run -dit -p 8080:8080  --name webdemo imgbase 
