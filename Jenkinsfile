pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                // Cloning the Repository to our Workspace
                checkout scm
            }
        }

        stage('Build and Run Docker Compose') {
            steps {
                script {
                    // 构建和运行 Docker Compose
                    sh 'docker-compose up --build -d'
                }
            }
        }

        stage('Run Test: Create Resource') {
            steps {
                script {
                    sh "docker-compose exec -T web pytest tests/test_create_resource.py || (docker-compose logs web && exit 1)"
                }
            }
        }

        stage('Run Test: Delete Resource') {
            steps {
                script {
                    sh "docker-compose exec -T web pytest tests/test_delete_resource.py"
                }
            }
        }

        stage('Run Test: Get Resource') {
            steps {
                script {
                    sh "docker-compose exec -T web pytest tests/test_get_resource.py"
                }
            }
        }

        stage('Run Test: Update Resource') {
            steps {
                script {
                    sh "docker-compose exec -T web pytest tests/test_update_resource.py"
                }
            }
        }

        stage('Teardown') {
            steps {
                script {
                    // 停止并移除容器
                    sh 'docker-compose down -v'
                }
            }
        }
    }

    post {
        always {
            // 清理工作环境
            sh 'docker-compose down'
            deleteDir()
        }
    }
}