#! /bin/sh

# Arg: name of the file

if [ $# -ne 2 ]; then
    echo "Usage: <path/to/app> <network>"
    exit 1
fi

if [ ! -n "$(sudo docker network ls | grep "$2")" ]; then
    echo "Error: Network '$2' does not exit"
    exit 2
elif [ -n "$(sudo docker ps | grep "flaskapp")" ]; then
		echo "Stopping 'flaskapp' container:"
    sudo docker stop flaskapp
		echo "Removing 'flaskapp' container:"
    sudo docker rm flaskapp
elif [ -n "$(sudo docker ps -a | grep "flaskapp")" ]; then
		echo "Removing 'flaskapp' container:"
    sudo docker rm flaskapp
fi
sudo docker run --network=$2 --name flaskapp \
    -d \
    -p 80:80 \
    -v $1:/app \
    -t flask

#docker exec --privileged flask /bin/sh -c 'nginx && uwsgi --ini /app.ini'
