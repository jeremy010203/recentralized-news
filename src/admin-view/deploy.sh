#! /bin/sh

# Arg: name of the file

if [ $# -ne 2 ]; then
    echo "Usage: <path/to/app> <network>"
    exit 1
fi

if [ ! -n "$(sudo docker network ls | grep "$2")" ]; then
    echo "Error: Network '$2' does not exit"
    exit 2
elif [ -n "$(sudo docker ps | grep "admin-view")" ]; then
		echo "Stopping 'admin-view' container:"
    sudo docker stop admin-view
		echo "Removing 'admin-view' container:"
    sudo docker rm admin-view
elif [ -n "$(sudo docker ps -a | grep "admin-view")" ]; then
		echo "Removing 'admin-view' container:"
    sudo docker rm admin-view
fi
sudo docker run --network=$2 --name admin-view \
    -d \
    -p 80:80 \
    -v $1:/app \
    -t flask

#docker exec --privileged flask /bin/sh -c 'nginx && uwsgi --ini /app.ini'
