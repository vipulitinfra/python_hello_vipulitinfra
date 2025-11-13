pipeline {
    agent any

    stage('Checkout') {
      steps {
         git branch: 'main', url: 'https://github.com/vipulitinfra/python_hello_vipulitinfra.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t vipulitinfra/python_hello_vipulitinfra:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }

        stage('Show Logs') {
            steps {
                sh 'docker logs --tail 20 $(docker ps -q --filter ancestor=vipulitinfra/python_hello_vipulitinfra:latest)'
            }
        }
    }
}
