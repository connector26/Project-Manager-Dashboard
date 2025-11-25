pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    
    environment {
        // PYTHON_IMAGE = 'python:3.11-slim' // Not used in native mode
        DOCKER_REGISTRY = 'docker-registry-url'
        DOCKER_IMAGE = 'project-manager-dashboard'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        SONAR_TOKEN = 'squ_18656fce255fc6a3434e2cba3a27c3015a2e3be5'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/connector26/Project-Manager-Dashboard.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    if ! command -v python &> /dev/null; then
                        echo "python not found. Attempting installation..."
                        if [ -f /etc/debian_version ]; then
                            apt-get update && apt-get install -y python python-pip
                        elif [ -f /etc/alpine-release ]; then
                            apk add --no-cache python py-pip
                        else
                            echo "Unsupported OS. Cannot install python automatically."
                            exit 1
                        fi
                    fi
                    python --version
                    python -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }
        
        stage('Lint') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pip install flake8 pylint
                    flake8 projectmanagerdashboard/ --max-line-length=120 --exclude=migrations,__pycache__
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python manage.py test --noinput
                '''
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                script {
                    try {
                        withSonarQubeEnv('SonarQube') {
                            sh '''
                                . venv/bin/activate
                                python -m pip install sonar-scanner-cli
                                sonar-scanner -Dproject.settings=sonar-project.properties -Dsonar.login=${SONAR_TOKEN}
                            '''
                        }
                    } catch (Exception err) {
                        echo "Skipping SonarQube analysis: ${err.getMessage()}"
                    }
                }
            }
        }
        
        /*
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                '''
            }
        }
        
        stage('Push to Registry') {
            steps {
                sh '''
                    docker login -u ${DOCKER_REGISTRY_USR} -p ${DOCKER_REGISTRY_PSW} ${DOCKER_REGISTRY}
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    docker push ${DOCKER_IMAGE}:latest
                '''
            }
        }
        */
    }
    
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            script {
                if (env.NODE_NAME?.trim()) {
                    node(env.NODE_NAME) {
                        deleteDir()
                    }
                } else if (env.WORKSPACE?.trim()) {
                    dir(env.WORKSPACE) {
                        deleteDir()
                    }
                } else {
                    echo 'Skipping workspace cleanup: node/workspace unknown.'
                }
            }
        }
    }
}
