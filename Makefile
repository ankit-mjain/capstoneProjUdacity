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
	python3 frontend/app.py & 
	python3 backend/app.py & 
	
test:

all:
	install test lint