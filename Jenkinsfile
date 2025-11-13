pipeline {
    agent any

    environment {
        APP_NAME = "python_hello_vipulitinfra"
        DOCKER_IMAGE = "python_hello_vipulitinfra:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                git branch: 'main', url: 'https://github.com/vipulitinfra/python_hello_vipulitinfra.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Run Container') {
            steps {
                echo "Running container..."
                // Stop previous container if running
                sh '''
                docker rm -f $APP_NAME || true
                docker run -d --name $APP_NAME -p 5000:5000 $DOCKER_IMAGE
                '''
            }
        }

        stage('Show Logs') {
            steps {
                echo "Showing last 10 log lines..."
                sh 'docker logs --tail 10 $APP_NAME'
            }
        }
    }
}
