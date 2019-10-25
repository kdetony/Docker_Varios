Docker Ejemplos Varios 
--------------
# Nginx Proxy Reverso
Este ejemplo trata de explicar como podemos configurar un proxy ( nginx ) como front-end para aplicaciones
que se ejecutan en contenedores, en este ejemplos veremos como hacerlo y teniendo en cuenta que la RED para
los contenedores incluyendo el Proxy es la misma ojo! ya que podemos crear una Red para los contenedores y/o aplicativos
y otra para el Proxy.

Para ellos, ejecutamos: 

>docker-compose up -d

Estos nos creará los contenedores docker-nginx y docker-apache, el cual serán atendidos por Nginx.

