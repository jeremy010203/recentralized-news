#! /bin/sh

# Arg: name of the file

if [ $# -ne 2 ]; then
    echo "Usage: <path/to/app> <network>"
    exit 1
fi

sudo docker stop flaskapp
sudo docker rm flaskapp
sudo docker run --network=$2 --name flaskapp \
    -d \
    -p 80:80 \
    -v $1:/app \
    -t flask

#docker exec --privileged flask /bin/sh -c 'nginx && uwsgi --ini /app.ini'
