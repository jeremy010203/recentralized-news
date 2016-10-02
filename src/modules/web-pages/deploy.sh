#! /bin/sh

# Arg: name of the file

if [ $# -ne 2 ]; then
    echo "Usage: <path/to/app> <network>"
    exit 1
fi

if [ ! -n "$(sudo docker network ls | grep "$2")" ]; then
    echo "Error: Network '$2' does not exit"
    exit 2
elif [ -n "$(sudo docker ps | grep "web-pages")" ]; then
		echo "Stopping 'web-pages' container:"
    sudo docker stop web-pages
		echo "Removing 'web-pages' container:"
    sudo docker rm web-pages
elif [ -n "$(sudo docker ps -a | grep "web-pages")" ]; then
		echo "Removing 'web-pages' container:"
    sudo docker rm web-pages
fi
sudo docker run --network=$2 --name web-pages \
    -d \
    -v $1:/app \
    -t flask

#docker exec --privileged flask /bin/sh -c 'nginx && uwsgi --ini /app.ini'
