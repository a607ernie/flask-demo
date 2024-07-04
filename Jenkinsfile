pipeline {
    agent any

    environment {
        // 定义Docker Compose文件路径
        COMPOSE_FILE = 'docker-compose.yaml'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // 从 Git 仓库克隆代码
                git 'https://github.com/a607ernie/flask-demo.git'
            }
        }

        stage('Build and Run Docker Compose') {
            steps {
                script {
                    // 构建和运行 Docker Compose
                    sh 'docker-compose -f $COMPOSE_FILE up -d --build'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // 运行测试
                    sh 'docker-compose -f $COMPOSE_FILE exec web sh -c "cd .. && cd tests && pytest"'
                }
            }
        }

        stage('Teardown') {
            steps {
                script {
                    // 停止并移除容器
                    sh 'docker-compose -f $COMPOSE_FILE down'
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
