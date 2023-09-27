pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello, World!'
            }
        }
        
        stage('Run Pytest') {
            steps {
                script {
                    bat 'pip install pytest'
                    bat 'pytest -v'
                }
            }
        }
    }
}
