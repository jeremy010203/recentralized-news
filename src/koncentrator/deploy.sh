#! /bin/sh

# Arg: name of the file

if [ $# -ne 2 ]; then
    echo "Usage: <path/to/app> <network>"
    exit 1
fi

sudo docker stop koncentrator
sudo docker rm koncentrator
sudo docker run --network=$2 --name koncentrator \
    -p 81:80 \
    -v $1:/app \
    -t flask
    -i /bin/sh

#docker exec --privileged flask /bin/sh -c 'nginx && uwsgi --ini /app.ini'
