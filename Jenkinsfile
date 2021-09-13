pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages{
        stage('Setup'){
            steps{
                sh 'make setup'
                withAWS(credentials:'aws-credentials-for-jenkins-user'){
                    sh 'aws --version'
                }
                echo 'Initial Setup done for the project'
            }
        }
        stage('Install'){
            steps{
                sh 'make install'
                echo 'Installed the python dependencies'
            }
        }
        stage('Lint'){
            steps{
                sh 'make lint'
                echo 'Linting the application complete'
            }
        }
        stage('Build-frontend'){
            steps{
                sh 'make build-frontend'
                echo 'Building frontend of the application'
            }
        }
        stage('Build-backend'){
            steps{
                sh 'make build-backend'
                echo 'Building backend of the application'
            }
        }
        stage('Publish-2-DockerHub'){
            steps{
                withCredentials([usernamePassword(credentialsId:'docker-creds', usernameVariable:'USERNAME', passwordVariable:'PASSWORD')]){
                    sh 'sudo docker login -u ${USERNAME} --password ${PASSWORD}'
                    sh 'make publish-to-dockerhub'
                }
            }
        }
        stage('Deploy'){
            steps{
                withAWS(region:'ap-south-1', credentials:'AWSCreds'){
                    sh 'curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.21.2/2021-07-05/bin/linux/amd64/kubectl'
                    sh 'chmod +x ./kubectl'
                    sh 'mv ./kubectl /usr/local/bin'
                    sh 'kubectl config use-context arn:aws:eks:ap-south-1:858493975654:cluster/upplCluster'
                    sh 'kubectl config view'
                }
            }
        }
    }
}
