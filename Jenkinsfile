pipeline {
    agent any

    environment {
        IMAGE_NAME = "simple-react-app"
        CONTAINER_NAME = "react_app_container"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Build React App') {
            steps {
                sh 'npm run build'
                echo 'React build complete'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
                echo 'Docker image built'
            }
        }

        stage('Deploy') {
            steps {
                sh """
                   docker stop $CONTAINER_NAME || true
                   docker rm $CONTAINER_NAME || true
                   docker run -d -p 3000:80 --name $CONTAINER_NAME $IMAGE_NAME
                """
                echo 'Application deployed'
            }
        }
    }
}
