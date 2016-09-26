CUR_DIR := $(shell echo $(shell pwd)$(shell echo /src/flask))

all: deploy

build:
	docker build -t flask src/flask/alpine-flask/

deploy: deploy-flask

deploy-flask:
	./src/flask/deploy.sh $(CUR_DIR)

stop:
	docker stop flaskapp

rm: stop
	docker rm flaskapp

clean:
	rm -rf *~ *#
	rm -rf src/flask/*~ src/flask/*# src/flask/*.pyc
	rm -rf src/flask/alpine-flask/*~ src/flask/alpine-flask/*# src/flask/alpine-flask/*.pyc

.PHONY: deploy clean stop rm build
