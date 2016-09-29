all: deploy

build:
	docker build -t flask src/docker_images/alpine-flask/

deploy:
	./src/flask/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/flask))
	./src/koncentrator/deploy.sh $(shell echo $(shell pwd)$(shell echo /src/koncentrator))

stop:
	docker stop flaskapp
	docker stop koncentrator

rm: stop
	docker rm flaskapp
	docker rm koncentrator

clean:
	rm -rf *~ *#
	rm -rf src/flask/*~ src/flask/*# src/flask/*.pyc
	rm -rf src/koncentrator/*~ src/koncentrator/*# src/koncentrator/*.pyc
	rm -rf src/flask/alpine-flask/*~ src/docker_images/alpine-flask/*# src/docker_images/alpine-flask/*.pyc

.PHONY: deploy clean stop rm build
