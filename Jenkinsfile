pipeline {
    agent any
    environment {
        ACR_NAME = 'flaskdevopsacr'
        ACR_LOGIN_SERVER = 'flaskdevopsacr.azurecr.io'
        IMAGE_NAME = 'flask-app'
        IMAGE_TAG = "v${BUILD_NUMBER}"
        RESOURCE_GROUP = 'flask-devops-rg'
        AKS_CLUSTER = 'flask-devops-aks'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Push to ACR') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'acr-credentials',
                    usernameVariable: 'ACR_USER',
                    passwordVariable: 'ACR_PASS'
                )]) {
                    sh "docker login ${ACR_LOGIN_SERVER} -u ${ACR_USER} -p ${ACR_PASS}"
                    sh "docker push ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
        stage('Deploy to AKS') {
            steps {
                withCredentials([string(
                    credentialsId: 'kubeconfig',
                    variable: 'KUBECONFIG_DATA'
                )]) {
                    sh '''
                        echo $KUBECONFIG_DATA | base64 -d > /tmp/kubeconfig
                        export KUBECONFIG=/tmp/kubeconfig
                        kubectl set image deployment/flask-app flask-app=${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG}
                        kubectl rollout status deployment/flask-app
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
pipeline {
    agent any
    environment {
        ACR_NAME = 'flaskdevopsacr'
        ACR_LOGIN_SERVER = 'flaskdevopsacr.azurecr.io'
        IMAGE_NAME = 'flask-app'
        IMAGE_TAG = "v${BUILD_NUMBER}"
        RESOURCE_GROUP = 'flask-devops-rg'
        AKS_CLUSTER = 'flask-devops-aks'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Push to ACR') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'acr-credentials',
                    usernameVariable: 'ACR_USER',
                    passwordVariable: 'ACR_PASS'
                )]) {
                    sh "docker login ${ACR_LOGIN_SERVER} -u ${ACR_USER} -p ${ACR_PASS}"
                    sh "docker push ${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
        stage('Deploy to AKS') {
            steps {
                withCredentials([string(
                    credentialsId: 'kubeconfig',
                    variable: 'KUBECONFIG_DATA'
                )]) {
                    sh '''
                        echo $KUBECONFIG_DATA | base64 -d > /tmp/kubeconfig
                        export KUBECONFIG=/tmp/kubeconfig
                        kubectl set image deployment/flask-app flask-app=${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG}
                        kubectl rollout status deployment/flask-app
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
