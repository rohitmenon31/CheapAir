pipeline {
    agent any

    triggers {
        cron('H/1 * * * *')
    }

    stages {
        stage('Build') {
            steps {
                sh 'echo Building...'
            }
        }
        stage('Test') {
            steps {
                sh 'echo Testing...'
            }
        }
    }
}

