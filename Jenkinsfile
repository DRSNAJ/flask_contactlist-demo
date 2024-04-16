def backend_img
def frontend_img
pipeline {
    environment {
        BACKEND_REGISTRY = "drsnaj/contactlist_backend" 
        FRONTEND_REGISTRY = "drsnaj/contactlist_frontend" 
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
                    cd ..
                    nohup python main.py  > flask.log 2>&1 &
                    sleep 5
                    
                    pkill -f main.py

                    '''
                }
        }
        
        stage ('Clean Up'){
            steps{
                // sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME}-2 | awk \'{print $1}\')'
                // sh returnStatus: true, script: 'docker rmi $(docker images | grep ${BACKEND_REGISTRY} | awk \'{print $3}\') --force' //this will delete all images
                // sh returnStatus: true, script: 'docker rm ${JOB_NAME}-2'
                
                // sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME}-1 | awk \'{print $1}\')'
                // sh returnStatus: true, script: 'docker rmi $(docker images | grep ${FRONTEND_REGISTRY} | awk \'{print $3}\') --force' //this will delete all images
                // sh returnStatus: true, script: 'docker rm ${JOB_NAME}-1'
                sh returnStatus: true, script: 'minikube stop'
                sh returnStatus: true, script: 'minikube delete'

                sh 'rm -rf venv'
            }
        }

        stage('Build') {
            steps {
                script {
                    parallel(
                        frontend: {
                            script {
                                frontend_img = FRONTEND_REGISTRY + ":v2.1.${env.BUILD_ID}"
                                println ("${frontend_img}")
                                frontendDockerImage = docker.build("${frontend_img}", '-f frontend/deployments/Dockerfile frontend/')
                            }
                        },
                        backend: {
                            script {
                                backend_img = BACKEND_REGISTRY + ":v2.1.${env.BUILD_ID}"
                                println ("${backend_img}")
                                backendDockerImage = docker.build("${backend_img}", '-f backend/deployments/Dockerfile backend/')
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
                        frontendDockerImage.push()
                    }

                    docker.withRegistry( 'https://registry.hub.docker.com ', docker_Credential ) {
                        backendDockerImage.push()
                    }
                }
            }
        }
                    
        stage('Deploy') {
           steps {
               sh 'minikube start'
               sh "sed -i 's|drsnaj/contactlist_backend:v2.1|drsnaj/contactlist_backend:v2.1.${env.BUILD_ID}|g' ./k8s/contactlist-backend.yaml"
               sh "sed -i 's|drsnaj/contactlist_frontend:v2.1|drsnaj/contactlist_frontend:v2.1.${env.BUILD_ID}|g' ./k8s/contactlist-frontend.yaml"
               sh "kubectl apply -f ./k8s/."
          }
        }

      }
    }