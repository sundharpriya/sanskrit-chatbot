pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'python --version'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test / Validate') {
            steps {
                echo 'Validating Python application...'
                bat 'python -m py_compile app.py'
                echo 'Python validation successful.'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t sanskrit-chatbot:jenkins .'
            }
        }

        stage('Result') {
            steps {
                echo 'Sanskrit Chatbot CI pipeline completed successfully.'
            }
        }
    }
}