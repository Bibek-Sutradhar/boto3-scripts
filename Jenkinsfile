pipeline {
    
    agent any
    triggers {
    githubPush()
  }
    stages {
        
        stage ("Build") {
            steps {
                echo 'Build Triggered from pipeline script !!'
            }
        }
    }
}
