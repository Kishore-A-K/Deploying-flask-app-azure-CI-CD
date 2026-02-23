pipeline {
    agent any
    environment {
        ACR_LOGIN_SERVER = 'flaskdevopsacr.azurecr.io'
        IMAGE_NAME = 'flask-app'
        RESOURCE_GROUP = 'flask-devops-rg'
        AKS_CLUSTER = 'flask-devops-aks'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }
        stage('Push to ACR') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'acr-credentials', usernameVariable: 'ACR_USER', passwordVariable: 'ACR_PASS')]) {
                    sh "docker login ${ACR_LOGIN_SERVER} -u ${ACR_USER} -p ${ACR_PASS}"
                    sh "docker push ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }
        stage('Deploy to AKS') {
            steps {
                withCredentials([string(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_DATA')]) {
                    sh """
                        echo \$KUBECONFIG_DATA | base64 -d > /tmp/kubeconfig
                        export KUBECONFIG=/tmp/kubeconfig
                        kubectl set image deployment/flask-app flask-app=${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${BUILD_NUMBER}
                        kubectl rollout status deployment/flask-app
                    """
                }
            }
        }
    }
    post {
        success { echo 'Deployed successfully!' }
        failure { echo 'Pipeline failed!' }
    }
}
