pipeline {
    agent any
    triggers {
        cron('H/5 * * * *')
    }
    stages {
        stage('Run Scenario 1') {
            steps {
                sh '''
                    source venv/bin/activate
                    python Test1.py
                '''
            }
        }
        stage('Run Scenario 2') {
            steps {
                sh '''
                    source venv/bin/activate
                    python Test2.py
                '''
            }
        }
        stage('Run Scenario 3') {
            steps {
                sh '''
                    source venv/bin/activate
                    python Test3.py
                '''
            }
        }
    }
}
