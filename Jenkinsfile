pipeline{

    agent any

    environment{
        //set env vars
        COMMIT_HASH = "latest"
        SERVICE_NAME = 'underwriter-ms'
        REGION = 'us-west-1'
        APP_NAME = 'my-underwriter-microservice'
        APP_ENV = 'dev'
        ORGANIZATION = 'Aline-Financial-MY'
        PROJECT_NAME = 'aline-underwriter-microservice-my'
    }

    stages{
        stage('Checkout'){
            steps{
                //get branch
                git branch: 'dev', url: 'https://github.com/markyates7748/aline-underwriter-microservice-my.git'
                sh'git submodule init'
                sh'git submodule update'
            }
        }
        stage('Test'){
            steps{
                //run project tests
                sh'mvn clean test'
            }
        }
        stage('Package'){
            steps{
                //package project
                sh'mvn package -DskipTests'
            }
        }
        stage('Build Image'){
            steps{
                //build docker image
                sh'docker build . -t ${APP_NAME}/${APP_ENV}/${SERVICE_NAME}:${COMMIT_HASH}'
                sh'docker tag ${APP_NAME}/${APP_ENV}/${SERVICE_NAME}:${COMMIT_HASH} ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}:${COMMIT_HASH}'
            }
        }
        stage('Push Image'){
            steps{
                //push image to cloud
                sh'docker push ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}:${COMMIT_HASH}'
            }
        }
    }

    post{
        always{
            //clean up
            sh'mvn clean'
            sh'docker image rm ${APP_NAME}/${APP_ENV}/${SERVICE_NAME}:${COMMIT_HASH}'
            sh'docker image rm ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}:${COMMIT_HASH}'
        }
    }

}