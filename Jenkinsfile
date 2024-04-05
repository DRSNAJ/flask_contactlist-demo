pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        echo 'Testing'
        timestamps() {
          sh '''cd /backend/tests
pytest'''
        }

      }
    }

  }
}