pipeline {
    agent any

    // Run every 10 minutes
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
                // Ensure Jenkins uses the correct Python path
                withEnv(["PATH=/usr/bin:$PATH"]) {
                    sh '/usr/bin/python3 Test1.py'
                }
            }
        }
    }

    post {
        always {
            echo "Automation finished!"
        }
    }
}
