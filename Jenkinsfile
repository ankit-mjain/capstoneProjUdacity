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
        stage('SetupK8sCluster'){
            steps{
                sh 'eksctl create cluster -f eksCluster.yml'
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploying the application'
            }
        }
    }
}
