pipeline {
    agent any

    triggers {
        cron('H/10 * * * *')  // Run every 10 minutes
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Automation') {
            steps {
                sh 'Test1.py'
            }
        }
    }

    post {
        always {
            echo "Automation finished!"
        }
    }
}
