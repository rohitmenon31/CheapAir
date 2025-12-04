pipeline {
    agent {
        docker { image 'python:3.11' }
    }

    triggers {
        cron('H/10 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Automation') {
            steps {
                sh 'python3 Test1.py'
            }
        }
    }
}

