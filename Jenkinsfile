pipeline {
    agent {
        docker {
            image 'python:3.9'  // Use the Python 3.9 official image as a base
            args '-u root:root'  // Run as root to avoid permission issues
        }
    }

    stages {
        stage('Setup') {
            steps {
                // Install pytest inside the container
                sh 'pip install pytest'
            }
        }
        
        stage('Run Pytest') {
            steps {
                sh 'pytest -v'
            }
        }
    }
}
