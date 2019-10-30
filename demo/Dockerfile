FROM alpine:latest

RUN apk add --no-cache python3-dev bash \
   && pip3 install --upgrade pip 

WORKDIR /deploy

COPY . /deploy

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["app.py"]
