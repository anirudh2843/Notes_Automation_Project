pipeline {

    agent any

    stages {

        stage('Install Dependencies') {

            steps {

                bat '''
                python -m venv venv

                call venv\\Scripts\\activate

                pip install --upgrade pip

                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Parallel Tests') {

            steps {

                bat '''
                call venv\\Scripts\\activate

                pytest -n 1 --alluredir=reports/allure-results
                '''
            }
        }

        stage('Generate Allure Report') {

            steps {

                allure(
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'reports/allure-results']]
                )
            }
        }
    }

    post {

        always {

            archiveArtifacts artifacts: 'screenshots/*.png'
            archiveArtifacts artifacts: 'logs/*.log'

            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'index.html',
                reportName: 'Automation Report'
            ])
        }

        success {

            echo 'Build Executed Successfully'
        }

        failure {

            echo 'Build Failed'
        }
    }
}