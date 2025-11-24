pipeline {
    agent any
    
    environment {
        DOCKER_REGISTRY = credentials('docker-registry-url')
        DOCKER_IMAGE = 'project-manager-dashboard'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        KUBECONFIG = credentials('kubeconfig')
        SONAR_TOKEN = credentials('sonar-token')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv || true
                    source venv/bin/activate || . venv/Scripts/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Lint') {
            steps {
                sh '''
                    source venv/bin/activate || . venv/Scripts/activate
                    pip install flake8 pylint || true
                    flake8 projectmanagerdashboard/ --max-line-length=120 --exclude=migrations,__pycache__ || true
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    source venv/bin/activate || . venv/Scripts/activate
                    cd projectmanagerdashboard
                    python manage.py test --noinput || true
                '''
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        source venv/bin/activate || . venv/Scripts/activate
                        pip install sonar-scanner-cli || true
                        sonar-scanner -Dproject.settings=sonar-project.properties -Dsonar.login=${SONAR_TOKEN} || true
                    '''
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                        docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }
        
        stage('Push to Registry') {
            steps {
                script {
                    sh '''
                        docker login -u ${DOCKER_REGISTRY_USR} -p ${DOCKER_REGISTRY_PSW} ${DOCKER_REGISTRY}
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                        docker push ${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh '''
                        export KUBECONFIG=${KUBECONFIG}
                        kubectl set image deployment/project-manager-dashboard \
                            project-manager-dashboard=${DOCKER_IMAGE}:${DOCKER_TAG} \
                            -n default || kubectl apply -f k8s/ -n default
                    '''
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            cleanWs()
        }
    }
}

