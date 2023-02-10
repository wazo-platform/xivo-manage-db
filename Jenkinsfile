pipeline {
  agent any
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
          string(name: "BRANCH", value: "bullseye"),
          string(name: "DISTRIBUTION", value: "wazo-dev-wip-bullseye"),
        ]
      }
    }
    stage('Docker build') {
      steps {
        sh "sed -i 's/master.zip/bullseye.zip/g' requirements.txt"
        sh "sed -i 's/master.zip/bullseye.zip/g' contribs/docker/wazo-base-db/Dockerfile"
        sh "sed -i 's|wazoplatform/wazo-base-db|wazoplatform/wazo-base-db:bullseye|g' Dockerfile"
        sh "sed -i 's|wazoplatform/wazo-confd-db|wazoplatform/wazo-confd-db:bullseye|g' contribs/docker/wazo-confd-db-test/Dockerfile"
        sh "docker build --no-cache -t wazoplatform/wazo-base-db:bullseye -f contribs/docker/wazo-base-db/Dockerfile contribs/docker/wazo-base-db"
        sh "docker build --no-cache -t wazoplatform/wazo-confd-db:bullseye ."
        sh "docker build --no-cache -t wazoplatform/wazo-confd-db-test:bullseye -f contribs/docker/wazo-confd-db-test/Dockerfile ."
        sh "git reset --hard"
      }
    }
    stage('Docker publish') {
      steps {
        sh "docker push wazoplatform/wazo-base-db:bullseye"
        sh "docker push wazoplatform/wazo-confd-db:bullseye"
        sh "docker push wazoplatform/wazo-confd-db-test:bullseye"
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
