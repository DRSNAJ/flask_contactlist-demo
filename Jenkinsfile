def backend_img
def frontend_img
pipeline {
    environment {
        DH_backend_registy = "drsnaj/contactlist_backend" 
        DH_frontend_registy = "drsnaj/contactlist_frontend" 
        docker_Credential = 'docker_hub-cred'
        github_Credential = 'github-cred'
        dockerImage = ''
    }
    agent any
    stages {
        
        stage('Pull Code') {
                steps {
                git branch: 'main',
                credentialsId: github_Credential,
                url: 'https://github.com/DRSNAJ/flask_contactlist-demo.git'
                }
        }
        
        stage ('Test'){
                steps {
                    sh '''
                    cd backend/
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install pytest
                    cd tests/
                    pytest
                    '''
                }
        }
        
        stage ('Clean Up'){
            steps{
                sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
                sh returnStatus: true, script: 'docker rmi $(docker images | grep ${DH_backend_registy} | awk \'{print $3}\') --force' //this will delete all images
                sh returnStatus: true, script: 'docker rm ${JOB_NAME}'
                sh 'rm -rf venv'
            }
        }

        stage('Build') {
            steps {
                script {
                    parallel(
                        frontend: {
                            script {
                                frontend_img = DH_frontend_registy + ":1.${env.BUILD_ID}"
                                println ("${frontend_img}")
                                dockerImage = docker.build("${frontend_img}", '-f frontend/Dockerfile frontend/')
                            }
                        },
                        backend: {
                            script {
                                backend_img = DH_backend_registy + ":1.${env.BUILD_ID}"
                                println ("${backend_img}")
                                dockerImage = docker.build("${backend_img}", '-f backend/Dockerfile backend/')
                            }
                        }

                    ) 
                }
            }
        }

        stage('Push To DockerHub') {
            steps {
                script {
                    docker.withRegistry( 'https://registry.hub.docker.com ', docker_Credential ) {
                        dockerImage.push()
                    }
                }
            }
        }
                    
        stage('Deploy') {
           steps {
                sh label: '', script: "docker run -d --name ${JOB_NAME} -p 5000:5000 ${backend_img}"
          }
        }

      }
    }