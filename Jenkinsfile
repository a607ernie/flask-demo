pipeline {
    agent any

    environment {
        SHARED_DATA_DIR = '/shared_data'
        GIT_REPO = 'https://github.com/your-repo/your-project.git'
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // 清理共享卷中的旧数据
                    sh "rm -rf ${SHARED_DATA_DIR}/*"
                    
                    // 克隆新的代码到共享卷中
                    sh "git clone ${GIT_REPO} ${SHARED_DATA_DIR}"
                    
                    // Optional: 如果需要安装依赖，可以在这里进行
                    // sh "cd ${SHARED_DATA_DIR} && pip install -r requirements.txt"
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