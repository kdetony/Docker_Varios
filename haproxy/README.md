Empezando 
========
Creando servicios varios

> docker service create --name plugapp --replicas 4 --publish 9090:8080 kdetony/plugapp:0.1

> docker service create --name nodeapp --replicas 5 --publish 9191:5000 kdetony/imghostprint:0.1

Ejemplo 
=====

1. Creamos un servicio de nombre srv_web

> docker service create --name srv_web --mount type=bind,source=/opt/web,target=/data nginxdemos/hello

2. Actualizamos el servicio:

> docker service update --publish-add 9292:80 srv_web

3. Lo escalamos a 5:

> docker service scale srv_web=5

4. Ahora copiamos la carpeta web y creamos el servicio:

> docker service create --name srv_prd --replicas 6 --publish 9393:80 --mount type=bind,source=/opt/prd,target=/usr/share/nginx/html   nginx
