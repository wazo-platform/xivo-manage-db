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
          string(name: 'PACKAGE', value: "xivo-manage-db"),
          string(name: "BRANCH", value: "bookworm"),
          string(name: "DISTRIBUTION", value: "wazo-dev-bookworm"),
        ]
      }
    }
    stage('Docker build base DB') {
      steps {
        sh "docker build --no-cache -t wazoplatform/wazo-base-db:bookworm -f contribs/docker/wazo-base-db/Dockerfile contribs/docker/wazo-base-db"
      }
    }
    stage('Docker publish base DB') {
      steps {
        sh "docker push wazoplatform/wazo-base-db:bookworm"
      }
    }
    stage('Docker build confd DB') {
      steps {
        sh "docker build --no-cache -t wazoplatform/wazo-confd-db:bookworm ."
      }
    }
    stage('Docker publish confd DB') {
      steps {
        sh "docker push wazoplatform/wazo-confd-db:bookworm"
      }
    }
    stage('Docker build confd DB test') {
      steps {
        sh "docker build --no-cache -t wazoplatform/wazo-confd-db-test:bookworm -f contribs/docker/wazo-confd-db-test/Dockerfile ."
      }
    }
    stage('Docker publish confd DB test') {
      steps {
        sh "docker push wazoplatform/wazo-confd-db-test:bookworm"
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
