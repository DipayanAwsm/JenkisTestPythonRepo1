pipeline {
    agent {
        docker {
            image 'python:3.10'  // Official Python image from Docker Hub
        }
    }

    stages {
        stage('PreStage') {
            steps {
                sh 'echo HIPreStage'
            }
        }

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/DipayanAwsm/JenkisTestPythonRepo1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'echo about to deploy'
            }
        }

        stage('Deploy Thecode') {
            steps {
                sh 'echo Code is deployed'
                sh 'python PythonCode.py'
            }
        }
    }
}
