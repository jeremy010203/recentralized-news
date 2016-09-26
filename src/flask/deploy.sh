#! /bin/sh

# Arg: name of the file

if [ $# -ne 1 ]; then
    echo "Usage: <path/to/app>"
    exit 1
fi

docker stop flaskapp
docker rm flaskapp
docker run --name flaskapp \
    -p 80:80 \
    -v $1:/app \
    -t flask > /dev/null &

#docker exec --privileged flask /bin/sh -c 'nginx && uwsgi --ini /app.ini'
