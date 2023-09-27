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
                    // Use bat for Windows commands
                    bat 'pytest -v'
                }
            }
        }
    }
}
