pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def imageName = "fastapi-demo:${env.BUILD_NUMBER}"
                    sh "docker build -t ${imageName} ."
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    def imageName = "fastapi-demo:${env.BUILD_NUMBER}"
                    // Uncomment and set your registry details below
                    // sh "docker tag ${imageName} <your-registry>/<your-repo>:${env.BUILD_NUMBER}"
                    // sh "docker push <your-registry>/<your-repo>:${env.BUILD_NUMBER}"
                }
            }
        }
    }
    post {
        always {
            echo 'Build completed.'
        }
    }
}
