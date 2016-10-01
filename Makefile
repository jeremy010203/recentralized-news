NETWORK=my_network

all: deploy

build:
	sudo docker build -t flask src/docker_images/alpine-flask/

deploy:
	sudo docker network rm $(NETWORK)
	sudo docker network create --driver bridge $(NETWORK)
	./src/flask/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/flask)) $(NETWORK)
	./src/koncentrator/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/koncentrator)) $(NETWORK)
	./src/modules/hello-world/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/modules/hello-world)) $(NETWORK)
	./src/modules/web-pages/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/modules/web-pages)) $(NETWORK)

stop:
	sudo docker stop flaskapp
	sudo docker stop koncentrator
	sudo docker stop hello-world
	sudo docker stop web-pages

rm:
	sudo docker rm -f flaskapp
	sudo docker rm -f koncentrator
	sudo docker rm -f hello-world
	sudo docker rm -f web-pages

clean:
	rm -rf *~ *#
	rm -rf src/flask/*~ src/flask/*# src/flask/*.pyc
	rm -rf src/koncentrator/*~ src/koncentrator/*# src/koncentrator/*.pyc
	rm -rf src/flask/alpine-flask/*~ src/docker_images/alpine-flask/*# src/docker_images/alpine-flask/*.pyc

.PHONY: deploy clean stop rm build
