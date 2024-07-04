pipeline {
    agent {
        docker {
            image 'jenkins/jenkins:lts'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                // 从 Git 仓库克隆代码
                git 'https://github.com/a607ernie/flask-demo.git'
            }
        }
        stage('Install Docker Compose') {
            steps {
                script {
                    sh '''
                    curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                    chmod +x /usr/local/bin/docker-compose
                    '''
                }
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
                    sh 'docker-compose exec web sh -c "cd .. && cd tests && pytest"'
                }
            }
        }

        stage('Teardown') {
            steps {
                script {
                    // 停止并移除容器
                    sh 'docker-compose down'
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
