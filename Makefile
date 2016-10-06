NETWORK=my_network

all: deploy

build:
	sudo docker build -t flask src/docker_images/alpine-flask/

deploy:
	-sudo docker network create --driver bridge $(NETWORK)
	./src/flask/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/flask)) $(NETWORK)
	./src/koncentrator/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/koncentrator)) $(NETWORK)
	./src/modules/hello-world/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/modules/hello-world)) $(NETWORK)
	./src/modules/web-pages/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/modules/web-pages)) $(NETWORK)
	./src/modules/wikipedia-random/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/modules/wikipedia-random)) $(NETWORK)

stop:
	-sudo docker stop flaskapp
	-sudo docker stop koncentrator
	-sudo docker stop hello-world
	-sudo docker stop web-pages
	-sudo docker stop wikipedia-random

rm:
	-sudo docker rm -f flaskapp
	-sudo docker rm -f koncentrator
	-sudo docker rm -f hello-world
	-sudo docker rm -f web-pages
	-sudo docker rm -f wikipedia-random
	-sudo docker network rm $(NETWORK)

clean:
	$(RM) *~ *#
	$(RM) src/flask/*~ src/flask/*# src/flask/*.pyc
	$(RM) src/koncentrator/*~ src/koncentrator/*# src/koncentrator/*.pyc
	$(RM) src/flask/alpine-flask/*~ src/docker_images/alpine-flask/*# src/docker_images/alpine-flask/*.pyc

.PHONY: deploy clean stop rm build deploy-modules
