# Dockerfile para contenedor Jboss 

En este es una breve explicación de como instalar Jboss en un contenedor, para ello, obtaré por usar una imagen, en este caso jboss/wildfly

>**docker pull jboss/wildfly**

Ahora, vamos a iniciar el contenedor: 

>docker run -p 8080:8080 -p 9990:9990 -dit --name webjboss   jboss/wildfly /opt/jboss/wildfly/bin/standalone.sh -bmanagement 0.0.0.0 

Para poder subsanar el detalle de accesos, solo se tiene habilitado el acceso via 127.0.0.1 o localhost para el Middleware, y como lo validamos??

Para ello vamos a ejecutar lo siguiente: 

>docker run -p 8080:8080 -p 9990:9990 -dit --name webjboss   jboss/wildfly /opt/jboss/wildfly/bin/standalone.sh -bmanagement 0.0.0.0 -b=0.0.0.0

**Para usar el Dockerfile:**
--------------------------------

>mkdir -p /home/docker/jboss ( Aqui descargamos el Dockerfile y calendar.war)

>**docker build -t imgjboss .**

Iniciamos el contenedor

>docker run -dit  --name jboss1 imgjboss



