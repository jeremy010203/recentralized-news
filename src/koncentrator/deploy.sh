#! /bin/sh

# Arg: name of the file

if [ $# -ne 2 ]; then
    echo "Usage: <path/to/app> <network>"
    exit 1
fi

if [ ! -n "$(sudo docker network ls | grep "$2")" ]; then
    echo "Error: Network '$2' does not exit"
    exit 2
elif [ -n "$(sudo docker ps | grep "koncentrator")" ]; then
		echo "Stopping 'koncentrator' container:"
    sudo docker stop koncentrator
		echo "Removing 'koncentrator' container:"
    sudo docker rm koncentrator
elif [ -n "$(sudo docker ps -a | grep "koncentrator")" ]; then
		echo "Removing 'koncentrator' container:"
    sudo docker rm koncentrator
fi
sudo docker run --network=$2 --name koncentrator \
    -d \
    -v $1:/app \
    -t flask

#docker exec --privileged flask /bin/sh -c 'nginx && uwsgi --ini /app.ini'
