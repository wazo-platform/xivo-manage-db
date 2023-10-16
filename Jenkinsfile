pipeline {
  agent any
  triggers {
    githubPush()
    pollSCM('H H * * *')
  }
  environment {
    MAIL_RECIPIENTS = 'dev+tests-reports@wazo.community'
  }
  options {
    skipStagesAfterUnstable()
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }
  stages {
    stage('Debian build and deploy') {
      steps {
        build job: 'build-package-no-arch', parameters: [
          string(name: 'PACKAGE', value: "${JOB_NAME}"),
        ]
      }
    }
    stage('Docker build base DB') {
      steps {
        sh "docker build --no-cache -t wazoplatform/wazo-base-db:latest -f contribs/docker/wazo-base-db/Dockerfile contribs/docker/wazo-base-db"
      }
    }
    stage('Docker publish base DB') {
      steps {
        sh "docker push wazoplatform/wazo-base-db:latest"
      }
    }
    stage('Docker build confd DB') {
      steps {
        sh "docker build --no-cache -t wazoplatform/wazo-confd-db:latest ."
      }
    }
    stage('Docker publish confd DB') {
      steps {
        sh "docker push wazoplatform/wazo-confd-db:latest"
      }
    }
    stage('Docker build confd DB test') {
      steps {
        sh "docker build --no-cache -t wazoplatform/wazo-confd-db-test:latest -f contribs/docker/wazo-confd-db-test/Dockerfile ."
      }
    }
    stage('Docker publish confd DB test') {
      steps {
        sh "docker push wazoplatform/wazo-confd-db-test:latest"
      }
    }
  }
  post {
    failure {
      emailext to: "${MAIL_RECIPIENTS}", subject: '${DEFAULT_SUBJECT}', body: '${DEFAULT_CONTENT}'
    }
    fixed {
      emailext to: "${MAIL_RECIPIENTS}", subject: '${DEFAULT_SUBJECT}', body: '${DEFAULT_CONTENT}'
    }
  }
}
