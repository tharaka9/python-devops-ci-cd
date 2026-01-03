pipeline {
    agent any

    environment {
        IMAGE_NAME = "lahiru128/python-devops-app"
        IMAGE_TAG  = "jenkins-${BUILD_NUMBER}"
        KUBECONFIG = "/etc/rancher/k3s/k3s.yaml"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/tharaka9/python-devops-ci-cd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push $IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
                kubectl set image deployment/python-devops-app \
                  python-app=$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }
}
