pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DipayanAwsm/JenkisTestPythonRepo1.git'
            }
        }

        stage('Check Python Version') {
            steps {
                sh 'python3 --version || echo "Python not installed"'
                sh 'pip3 --version || echo "pip not installed"'
            }
        }

        stage('Install Requirements (if possible)') {
            steps {
                sh 'python3 -m venv venvTemp'
                sh '. venvTemp/bin/activate
                 python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Python Code') {
            steps {
                sh '''
            . venvTemp/bin/activate
            python PythonCode.py
             '''
            }
        }
    }
}
