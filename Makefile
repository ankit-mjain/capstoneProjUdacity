#!/bin/bash

setup:
	sudo apt-get install -y python3.8 python3.8-dev python3.8-venv && \
	python3 -m venv ~/.venv
	sudo wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v2.7.0/hadolint-Darwin-x86_64
	sudo chmod +x /bin/hadolint
	
install:
	python3 -m pip install --upgrade pip && \
		python3 -m pip install -r requirements.txt
		
lint:
	pylint --disable=R,C,W1203 frontend/*.py backend/*.py
	/bin/hadolint ./frontend/Dockerfile
	/bin/hadolint ./backend/Dockerfile

build-frontend:
	docker build -t frontend -f ./frontend/Dockerfile .

build-backend:
	docker build -t backend -f ./backend/Dockerfile .

deploy-frontend:

deploy-backend:


test:

all:
	install test lint
