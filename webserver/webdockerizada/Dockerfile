FROM alpine

LABEL maintainer="kdetony@kdetony.com"

RUN apk add --update nodejs nodejs-npm

# directorio de trabajo
WORKDIR /src

# Copiar app a /src
COPY . /src

# Dependencias
RUN  npm install

# Exponiendo puerto del servicio
EXPOSE 8181

ENTRYPOINT ["node", "./app.js"]
