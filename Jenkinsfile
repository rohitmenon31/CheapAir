pipeline {
    agent any

    triggers {
        cron('H/10 * * * *') // every 10 minutes
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

    post {
        always {
