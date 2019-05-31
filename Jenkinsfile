pipeline {
  agent any
  stages {
    stage('build steps') {
      steps {
        echo "building steps"
        script {
          def envs = sh(script: 'uname', returnStdout: true).trim().split('\n')
          envs.each { env ->
            script {
              stage(module) {
                echo(env)
              }
            }
          }
        }
      }
    }
    stage('test') {
      steps {
        sh '''
        #!/bin/bash
        export PATH="/home/jure/.pyenv/bin:$PATH"
        eval "$(pyenv init -)"
        eval "$(pyenv virtualenv-init -)"

        pyenv local 3.7.3
        export REMOTE_SELENIUM=win-velis:4444,jenkins,FIREFOX
        # FIREFOX, EDGE, INTERNETEXPLORER
        # tox
        '''
      }
    }
  }
}
