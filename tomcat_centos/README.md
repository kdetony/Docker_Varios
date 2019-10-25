# Dockerfile / Tomcat 7/8 en Centos 7.X

Este es un Dockerfile para instalar Tomcat sobre Centos 7.x. Así como los ficheros de configuración necesarios para su administración, configuración y tuning. Descargar la versión 8.x de Tomcat, desde este enlace : http://apache.uvigo.es/tomcat/tomcat-8/v8.5.41/bin/apache-tomcat-8.5.41.tar.gz, hay que dejarlo en la misma carpeta del proyecto ojo ( */home/docker/tomcat* Dockerfile y XML por ejm.) 

Para realizar la construcción de la imagen:

<code>docker build -t kdetony/tomcat8:latest .</code>

Una vez generada la imagen, utilizamos el siguiente comando:

<code>docker run -dit -p 8080:8080 --name mytomcat kdetony/tomcat8:latest  </code>

Ahora para poder validarlo, abrimos un browser : http://localhost:8080 

Vamos ahora a deployar sample(1).war  de la siguiente manera:

docker cp /home/kdetony/tomcat/sample(1).war  mytomcat:/opt/tomcat/webapps/

Y lo validamos: http://localhost:8080/sample
