pipeline {
    
    agent any
    triggers {
    githubPush()
  }
    stages {

	stage ("Init") {
	   steps {
	   git branch: 'master',
	   url: 'https://github.com/Bibek-Sutradhar/boto3-scripts.git'
	   echo 'Success'
	}
	
    }
        
        stage ("Build") {
            steps {
                echo 'Build Triggered from pipeline script !!'
            }
        }
    }
}
