#! /bin/sh

# Arg: name of the file

if [ $# -ne 1 ]; then
    echo "Usage: <path/to/app>"
    exit 1
fi

docker stop flaskapp
docker rm flaskapp
docker run --name flaskapp --restart=always \
    -p 80:80 \
    -v $1:/app \
    -d jazzdd/alpine-flask
