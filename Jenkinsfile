pipeline {
    agent any

    stages{
        stage('Setup'){
            steps{
                sh 'make setup'
                echo 'Initial Setup done for the project'
            }
        }
        stage('Build'){
            steps{
                echo 'Building the application'
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
