# 📊 Project Manager Dashboard

A Django-based dashboard application for project managers to track deliverables and ensure timely project delivery. Designed for deployment on Kubernetes via CI/CD pipeline.

---

## 🚀 Application Overview

**Name:** 2401032-managerdash  
**Type:** Django Web Application  
**Port:** 8000  
**Health Check Endpoint:** `/healthz/`  
**Framework:** Django 5.1.4 with Gunicorn WSGI server

### Features

- Project deliverable tracking
- User authentication and role management
- Admin panel for project management
- Real-time project monitoring
- Responsive dashboard interface

---

## 🏗️ Project Structure

```
project-manager-dashboard/
├── k8s-deployment/           # Kubernetes manifests
│   ├── deployment.yaml       # Application deployment
│   ├── service.yaml          # ClusterIP service
│   ├── ingress.yaml          # External access
│   └── pvc.yaml              # Persistent storage
├── projectmanagerdashboard/  # Django project
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── authentication/           # Authentication app
├── projectdashboard/         # Core dashboard app
├── donetask/                 # Task management app
├── templates/                # HTML templates
├── Dockerfile                # Container image definition
├── Jenkinsfile               # CI/CD pipeline
├── requirements.txt          # Python dependencies
├── sonar-project.properties  # Code quality config
├── pytest.ini                # Test configuration
└── README.md
```

---

## 🐳 Docker

### Build Locally

```bash
cd projectmanagerdashboard
docker build -t 2401032-managerdash:latest .
```

### Run Locally

```bash
docker run -d -p 8000:8000 --name managerdash 2401032-managerdash:latest
```

Access at: `http://localhost:8000`

### Health Check

```bash
curl http://localhost:8000/healthz/
```

Expected response: `ok`

---

## 🔄 CI/CD Pipeline

### Pipeline Stages

1. **Build Docker Image** - Builds container using Dockerfile
2. **Run Tests** - Executes pytest with coverage
3. **SonarQube Analysis** - Code quality and security scan
4. **Login to Registry** - Authenticate with Nexus registry
5. **Tag & Push Image** - Push to Nexus Docker registry
6. **Deploy Application** - Deploy to Kubernetes cluster

### Pipeline Configuration

**Registry:** `nexus-service-for-docker-hosted-registry.nexus.svc.cluster.local:8085`  
**Repository:** `managerdash`  
**Image Tag:** `latest`  
**Namespace:** `2401032`  
**SonarQube:** `my-sonarqube-sonarqube.sonarqube.svc.cluster.local:9000`

### Automatic Deployment

1. Push code to GitHub repository
2. Jenkins pipeline triggers automatically
3. Application builds, tests, and deploys
4. Access via Ingress: `managerdash-2401032.local`

---

## ☸️ Kubernetes Deployment

### Resources Created

- **Deployment:** `2401032-managerdash` (2 replicas)
- **Service:** `managerdash-service` (ClusterIP on port 80)
- **Ingress:** `managerdash-ingress` (External access)
- **PVC:** `managerdash-pvc` (1Gi storage for database)

### Resource Limits

- **Memory Request:** 256Mi
- **Memory Limit:** 512Mi
- **CPU Request:** 250m
- **CPU Limit:** 500m

### Health Probes

**Liveness Probe:**
- Path: `/healthz/`
- Initial Delay: 45s
- Period: 30s

**Readiness Probe:**
- Path: `/healthz/`
- Initial Delay: 30s
- Period: 10s

### Access Application

Via Ingress: `http://managerdash-2401032.local`

*Note: Update your hosts file or use cluster DNS*

---

## 🔧 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DJANGO_SETTINGS_MODULE` | `projectmanagerdashboard.settings` | Django settings module |
| `PYTHONUNBUFFERED` | `1` | Unbuffered Python output |
| `DEBUG` | `False` | Django debug mode (production) |
| `ALLOWED_HOSTS` | `*` | Allowed hosts (configure for production) |

---

## 💾 Database

**Development:** SQLite (db.sqlite3)  
**Production:** Persistent volume mounted at `/app/db`

### Run Migrations

Migrations run automatically during Docker build. To run manually:

```bash
python manage.py migrate
```

### Create Superuser

```bash
kubectl exec -it deployment/2401032-managerdash -n 2401032 -- python manage.py createsuperuser
```

---

## 🧪 Testing

### Run Tests Locally

```bash
pytest --maxfail=1 --disable-warnings --cov=. --cov-report=xml
```

### Run Tests in Docker

```bash
docker run --rm 2401032-managerdash:latest pytest --maxfail=1 --disable-warnings --cov=. --cov-report=xml
```

### Test Coverage

Coverage reports are generated in `coverage.xml` and sent to SonarQube during pipeline execution.

---

## 🔍 Monitoring & Debugging

### View Logs

```bash
kubectl logs -f deployment/2401032-managerdash -n 2401032
```

### Check Pod Status

```bash
kubectl get pods -n 2401032
kubectl describe pod <pod-name> -n 2401032
```

### View Services

```bash
kubectl get svc -n 2401032
```

### View Ingress

```bash
kubectl get ingress -n 2401032
```

---

## ⚠️ Troubleshooting

### ImagePullBackOff

**Causes:**
- Image tag mismatch
- Wrong registry URL
- Missing imagePullSecrets

**Fix:**
```bash
kubectl describe pod <pod-name> -n 2401032
# Check image name and registry URL
```

### CrashLoopBackOff

**Causes:**
- Application not starting
- Wrong PORT configuration
- Missing environment variables
- Database connection issues

**Fix:**
```bash
kubectl logs <pod-name> -n 2401032
# Check application logs for errors
```

### Health Check Failing

**Causes:**
- Application not responding on port 8000
- `/healthz/` endpoint not accessible
- Application startup taking too long

**Fix:**
- Increase `initialDelaySeconds` in deployment.yaml
- Check if Gunicorn is running correctly
- Verify Django routes configuration

---

## 📋 Deployment Checklist

Before submitting/deploying:

- ✅ Dockerfile builds successfully
- ✅ All tests pass locally
- ✅ Jenkins pipeline is GREEN
- ✅ Image pushed to Nexus registry
- ✅ Deployment stage completed
- ✅ Application pods are running
- ✅ Health check endpoint returns 200 OK
- ✅ K8s manifests are in `k8s-deployment/` directory
- ✅ SonarQube analysis completed

---

## 🔐 Access & Permissions

### Jenkins-Only Kubernetes Access

All Kubernetes deployments are managed through Jenkins. Users do not need direct cluster access.

### Lens (Exception Only)

Use Lens only for:
- Viewing logs
- Inspecting pod events
- Debugging cluster-level issues

**Important:** All configuration changes must go through GitHub → Jenkins pipeline.

---

## 👨‍💼 Admin Panel

Access Django admin at: `/admin/`

Default superuser must be created manually (see Database section).

---

## 📜 License

MIT License - See LICENSE file for details

---

## 🤝 Contributing

1. Create feature branch
2. Make changes
3. Push to GitHub
4. Jenkins auto-deploys to staging
5. Review and merge to main

---

## 📞 Support

For issues or questions:
- Check Jenkins pipeline logs
- Review pod logs in Kubernetes
- Check SonarQube for code quality issues
