# Capstone Project for Udacity DevOps Course

This repository is associated with the capstone project. It contains a flask app with frontend & backend services containerized using Docker & deployed EKS cluster on AWS

## Setup
1) Setup an EC2 server with ubuntu OS on AWS

2) Install Jenkins on the same using the below:
https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/

3) Create eksctl cluster using the below command:
eksctl create cluster -y eksCluster.yml

The above command would setup clouformation stacks for setting up the cluster & node groups.

4) Connect the github repository with the Jenkins server using Github webhooks & github credentials in Jenkins

5) Commit the code in Github which would automatically publish on the Jenkins pipeline 

6) Used Dockerhub to upload the Docker images whic would be deployed on kubernetes cluster

7) Blue deployment is done first in the pipeline. Post which user is asked to confirm if he is fine with the deployment. If yes, then green deployment is done. 
