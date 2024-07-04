pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-demo"
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/a607ernie/flask-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'pytest --maxfail=1 --disable-warnings'
                    }
                }
            }
        }

        // stage('Deploy') {
        //     steps {
        //         script {
        //             dockerImage.push()
        //         }
        //     }
        // }
    }

    post {
        always {
            cleanWs()
        }
    }
}
