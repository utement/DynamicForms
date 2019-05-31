pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh '''#!/bin/bash
export && PATH="/home/jure/.pyenv/bin:$PATH"
&& eval "$(pyenv init -)"
&& eval "$(pyenv virtualenv-init -)"

&& pyenv local 3.7.3
&& export REMOTE_SELENIUM=win-velis:4444,jenkins,FIREFOX
&& # FIREFOX, EDGE, INTERNETEXPLORER
&& tox
'''
      }
    }
  }
}