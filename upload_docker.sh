#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
# dockerpath=<your docker ID/path>
dockerpath="ankit4all/capstoneprojudacity"

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
# docker login
docker tag frontend:latest ankit4all/capstoneprojudacity:frontend
docker tag backend:latest ankit4all/capstoneprojudacity:backend

# Step 3:
# Push image to a docker repository
docker push $dockerpath:frontend
docker push $dockerpath:backend
