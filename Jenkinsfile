pipeline {
    agent any
    triggers {
        cron('H/5 * * * *') // Runs every 5 minutes
    }
    stages {
        stage('Run Scenario 1') {
            steps {
                sh 'python3 Test1.py'
            }
        }
        stage('Run Scenario 2') {
            steps {
                sh 'python3 Test2.py'
            }
        }
        stage('Run Scenario 3') {
            steps {
                sh 'python3 Test3.py'
            }
        }
    }
}

