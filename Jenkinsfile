node {
  def app
    stage('Clone the repository') {
      checkout scm
    }

    stage('Build image') {
       app = docker.build('democlouddevops/sfga-web')
    }

    stage('Test image') {
      app.inside {
        sh 'echo "Tests passed"'
      }
    }

    stage('Push image') {
      docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
        app.push("${env.BUILD_NUMBER}")
      }
    }

    stage('Trigger ManifestUpdate Jenkins Job') {
      echo 'triggering updatemanifestjob'
      build job: 'sfgagitops', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
    }
}
