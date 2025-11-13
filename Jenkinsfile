pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vipulitinfra/pythonapp_demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "🛠️ Building Docker image..."
                    sh 'docker build -t vipulitinfra/pythonapp_demo .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    echo "🚀 Running Docker container..."
                    sh 'docker run -d -p 5000:5000 --name pythonapp vipulitinfra/pythonapp_demo'
                }
            }
        }

        stage('Show Logs (Last Part)') {
            steps {
                script {
                    echo "📜 Showing last part of container logs..."
                    sh 'docker logs --tail 20 pythonapp'
                }
            }
        }
    }
}
