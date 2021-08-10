pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                sh """
                    docker build -t fastapi_test:latest .
                """
            }
        }
        stage("run") {
            steps {
                sh """
                    docker run -p 8081:80 -d fastapi_test:latest
                """
            }
        }
    }
}

