pipeline {
    agent {
        docker { image 'python:3.11' } // Python container
    }

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
                sh 'python Test1.py' // runs your script inside Python container
            }
        }
    }

    post {
        always {
            echo "Automation finished!"
        }
    }
}
