#! /bin/sh

# Arg: name of the file

if [ $# -ne 2 ]; then
    echo "Usage: <path/to/app> <network>"
    exit 1
fi

if [ ! -n "$(sudo docker network ls | grep "$2")" ]; then
    echo "Error: Network '$2' does not exit"
    exit 2
elif [ -n "$(sudo docker ps | grep "hello-world")" ]; then
		echo "Stopping 'hello-world' container:"
    sudo docker stop hello-world
		echo "Removing 'hello-world' container:"
    sudo docker rm hello-world
elif [ -n "$(sudo docker ps -a | grep "hello-world")" ]; then
		echo "Removing 'hello-world' container:"
    sudo docker rm hello-world
fi
sudo docker run --network=$2 --name hello-world \
    -d \
    -v $1:/app \
    -t flask

#docker exec --privileged flask /bin/sh -c 'nginx && uwsgi --ini /app.ini'
