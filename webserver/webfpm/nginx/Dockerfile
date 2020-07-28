FROM alpine

RUN apk add nginx --no-cache

WORKDIR /app

COPY index.php . 

COPY default.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/nginx.conf     
    
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
