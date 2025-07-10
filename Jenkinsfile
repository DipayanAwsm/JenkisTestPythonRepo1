pipeline {
    agent any

    stages {
        stage('PreStage') {
            steps {
                sh 'echo HIPreStage'
            }
        }
        stage('Clone Repo') {
            steps {
                git 'https://github.com/DipayanAwsm/JenkisTestPythonRepo1.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover'
            }
        }
    }
}
