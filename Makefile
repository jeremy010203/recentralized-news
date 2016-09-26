CUR_DIR := $(shell echo $(shell pwd)$(shell echo /src/flask))

all: deploy

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

.PHONY: deploy clean stop rm