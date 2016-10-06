#! /bin/sh

# Arg: name of the file

if [ $# -ne 2 ]; then
    echo "Usage: <path/to/app> <network>"
    exit 1
fi

if [ ! -n "$(sudo docker network ls | grep "$2")" ]; then
    echo "Error: Network '$2' does not exit"
    exit 2
elif [ -n "$(sudo docker ps | grep "wikipedia-random")" ]; then
		echo "Stopping 'wikipedia-random' container:"
    sudo docker stop wikipedia-random
		echo "Removing 'wikipedia-random' container:"
    sudo docker rm wikipedia-random
elif [ -n "$(sudo docker ps -a | grep "wikipedia-random")" ]; then
		echo "Removing 'wikipedia-random' container:"
    sudo docker rm wikipedia-random
fi
sudo docker run --network=$2 --name wikipedia-random \
	  -d \
    -v $1:/app \
    -t flask

#docker exec --privileged flask /bin/sh -c 'nginx && uwsgi --ini /app.ini'
