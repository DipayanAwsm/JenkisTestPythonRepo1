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
                sh 'source venvTemp/bin/activate'
                sh 'test -f requirements.txt && python3 -m pip install -r requirements.txt || echo "No requirements.txt or pip failed"'
            }
        }

        stage('Run Python Code') {
            steps {
                sh 'test -f PythonCode.py && python3 PythonCode.py || echo "PythonCode.py not found or failed to run"'
            }
        }
    }
}
