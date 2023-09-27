pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u root:root'
        }
    }

    environment {
        // Assuming you've stored your GitHub token with the ID 'github-token'
        GH_TOKEN = credentials('githubtoken')
    }

    stages {
        stage('Setup') {
            steps {
                sh 'pip install pytest'
            }
        }
        
        stage('Run Pytest') {
            steps {
                script {
                    try {
                        sh 'pytest -v'
                        updateGitHubStatus('success', 'Pytest passed')
                    } catch (Exception e) {
                        updateGitHubStatus('failure', 'Pytest failed')
                        throw e
                    }
                }
            }
        }
    }

    post {
        always {
            // Additional steps if you want to capture and archive the pytest results, e.g., JUnit format
        }
    }
}

def updateGitHubStatus(String state, String description) {
    def repo = 'marounayli-usj/introops'  // Replace with your repo details
    def commitSha = env.GIT_COMMIT  // This environment variable should have the commit SHA

    def apiUrl = "https://api.github.com/repos/${repo}/statuses/${commitSha}"

    sh(script: """
        curl -s -X POST ${apiUrl} \
        -H "Authorization: token ${GH_TOKEN}" \
        -H "Content-Type: application/json" \
        -d '{
            "state": "${state}",
            "description": "${description}",
            "context": "continuous-integration/jenkins"
        }'
    """, label: 'Updating GitHub commit status')
}
