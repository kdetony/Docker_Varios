Empezando 
========
Creando servicios varios

> docker service create --name plugapp --replicas 4 --publish 9090:8080 kdetony/plugapp:0.1

> docker service create --name nodeapp --replicas 5 --publish 5000:5000 imgjs

> docker service create --name srvnginx --replicas 6 --publish 8181:80 --mount type=bind,source=/mnt/nginx,target=/usr/share/nginx/html   nginx
