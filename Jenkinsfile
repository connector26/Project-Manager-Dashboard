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
                    # Setup portable python if system python is missing or incompatible
                    if ! command -v python3 >/dev/null 2>&1; then
                        echo "python3 not found. Downloading portable python..."
                        if [ ! -d "python" ]; then
                            PYTHON_URL="https://github.com/indygreg/python-build-standalone/releases/download/20230826/cpython-3.10.13+20230826-x86_64-unknown-linux-gnu-install_only.tar.gz"
                            if command -v curl >/dev/null 2>&1; then
                                curl -L -o python.tar.gz "$PYTHON_URL"
                            elif command -v wget >/dev/null 2>&1; then
                                wget -O python.tar.gz "$PYTHON_URL"
                            else
                                echo "Error: Neither curl nor wget found. Cannot download python."
                                exit 1
                            fi
                            tar -xzf python.tar.gz
                            rm python.tar.gz
                        fi
                        # Add portable python to PATH for this script block
                        export PATH="$PWD/python/bin:$PATH"
                    fi
                    
                    echo "Using python: $(which python3)"
                    python3 --version
                    
                    python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }
        
        stage('Lint') {
            steps {
                sh '''
                    # Add portable python to PATH if it exists
                    if [ -d "python/bin" ]; then
                        export PATH="$PWD/python/bin:$PATH"
                    fi
                    
                    . venv/bin/activate
                    python3 -m pip install flake8 pylint
                    flake8 projectmanagerdashboard/ --max-line-length=120 --exclude=migrations,__pycache__
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    # Add portable python to PATH if it exists
                    if [ -d "python/bin" ]; then
                        export PATH="$PWD/python/bin:$PATH"
                    fi
                    
                    . venv/bin/activate
                    python3 manage.py test --noinput
                '''
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                script {
                    try {
                        withSonarQubeEnv('SonarQube') {
                            sh '''
                                # Add portable python to PATH if it exists
                                if [ -d "python/bin" ]; then
                                    export PATH="$PWD/python/bin:$PATH"
                                fi
                                
                                . venv/bin/activate
                                python3 -m pip install sonar-scanner-cli
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
