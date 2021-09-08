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
        stage('Test'){
            steps{
                echo 'Testing the application'
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deploying the application'
            }
        }
    }
}
