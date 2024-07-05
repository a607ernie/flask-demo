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

        stage('Run Tests') {
            steps {
                script {
                    // 运行测试
                    sh 'docker-compose exec -T web sh -c pytest'
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