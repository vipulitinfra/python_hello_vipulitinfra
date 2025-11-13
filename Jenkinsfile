pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/vipulitinfra/python_hello_vipulitinfra.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t vipulitinfra/python_hello_vipulitinfra:latest .'
      }
    }

    stage('Push to Docker Hub') {
      steps {
        // Ensure Jenkins has Docker Hub credentials or run docker login before pipeline
        sh 'echo "$DOCKER_HUB_PASS" | docker login --username "$DOCKER_HUB_USER" --password-stdin'
        sh 'docker push vipulitinfra/python_hello_vipulitinfra:latest'
      }
    }

    stage('Deploy with Compose') {
      steps {
        sh 'docker-compose down || true'
        sh 'docker-compose up -d --build'
      }
    }

    stage('Verify') {
      steps {
        sh 'sleep 5'
        sh 'curl -f http://localhost:5001 || (echo "Health check failed" && exit 1)'
      }
    }
  }

  post {
    success { echo "✅ Pipeline finished successfully" }
    failure { echo "❌ Pipeline failed — check console output" }
  }
}
