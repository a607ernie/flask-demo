pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                // Cloning the repository to our workspace
                checkout scm
            }
        }

        stage('Build and Run Docker Compose') {
            steps {
                script {
                    // Build and run Docker Compose
                    docker.compose('docker-compose.yml').build().up()
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests
                    docker.compose('docker-compose.yml').exec(['web'], 'pytest')
                }
            }
        }

        stage('Teardown') {
            steps {
                script {
                    // Stop and remove containers
                    docker.compose('docker-compose.yml').down()
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up the work environment
                docker.compose('docker-compose.yml').down()
                deleteDir()
            }
        }
    }
}
