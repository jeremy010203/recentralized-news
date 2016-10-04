#! /bin/sh

# Arg: name of the file

if [ $# -ne 2 ]; then
    echo "Usage: <path/to/app> <network>"
    exit 1
fi

if [ ! -n "$(sudo docker network ls | grep "$2")" ]; then
    echo "Error: Network '$2' does not exit"
    exit 2
elif [ -n "$(sudo docker ps | grep "hello-world-push")" ]; then
		echo "Stopping 'hello-world-push' container:"
    sudo docker stop hello-world-push
		echo "Removing 'hello-world-push' container:"
    sudo docker rm hello-world-push
elif [ -n "$(sudo docker ps -a | grep "hello-world-push")" ]; then
		echo "Removing 'hello-world-push' container:"
    sudo docker rm hello-world-push
fi
sudo docker run --network=$2 --name hello-world-push \
    -d \
    -v $1:/app \
    -t flask

#docker exec --privileged flask /bin/sh -c 'nginx && uwsgi --ini /app.ini'
