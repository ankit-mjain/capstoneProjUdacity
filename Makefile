#!/bin/bash

setup:
	sudo apt-get install -y python3.8 python3.8-dev python3.8-venv && \
	python3 -m venv ~/.venv
	
install:
	python3 -m pip install --upgrade pip && \
		python3 -m pip install -r requirements.txt
		
lint:
	pylint --disable=R,C,W1203 frontend/*.py backend/*.py

deploy:
	docker build -t frontend -f ~/environment/capstoneProjUdacity/frontend/Dockerfile .
	docker build -t backend -f ~/environment/capstoneProjUdacity/backend/Dockerfile .

test:

all:
	install test lint