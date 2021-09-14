# Capstone Project for Udacity DevOps Course

This repository is associated with the capstone project. It contains a flask app with frontend & backend services containerized using Docker & deployed EKS cluster on AWS

## Setup
1) Setup an EC2 server with ubuntu OS on AWS

2) Install Jenkins on the same using the below:
- https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/
- Below is the list of pipeline stages which are listed in the Jenkinsfile
--- Setup: Create initial setup for python/hadolint
--- Install: Install the project requirements
--- Lint: Linting python code / Dockerfile
--- Build-frontend: Build docker image for frontend
--- Build-backend: Build docker image for backend
--- Publish-2-Dockerhub: publish both the images to Dockerhub
--- setup-kubectl: Setup Kubectl on Jenkins server. Assuming that the EKS Cluster is already up.
--- Deploy-Blue: Blue deployment
--- Validate-Deployment: User to validate if he / she is fine with the deployment
--- Deploy-Green: Green deployment if approved

3) Create eksctl cluster using the below command. This command would setup clouformation stacks for setting up the cluster & node groups.
- eksctl create cluster -y eksCluster.yml

4) Connect the github repository with the Jenkins server using Github webhooks & github credentials in Jenkins

5) Commit the code in Github which would automatically publish on the Jenkins pipeline 

6) Used Dockerhub to upload the Docker images whic would be deployed on kubernetes cluster

7) Blue deployment is done first in the pipeline. Post which user is asked to confirm if he is fine with the deployment. If yes, then green deployment is done. Below command was used to deploy on the kubernetes cluster.
- kubectl apply -f blue-deployment.yml
- kubectl apply -f green-deployment.yml
