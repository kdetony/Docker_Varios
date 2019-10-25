# docker/docker-install
Instalacion de Docker via script

## Uso:

From `https://get.docker.com`:
```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

Para realizar un test antes de la instalacion:

From `https://test.docker.com`:
```shell
curl -fsSL https://test.docker.com -o test-docker.sh
sh test-docker.sh
```

From the source repo (This will install latest from the `test` channel):
```shell
sh install.sh
```

## Testing:

To verify that the install script works amongst the supported operating systems run:

```shell
make check
```
