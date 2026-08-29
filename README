# ☁️ CloudPulse

**CloudPulse** is a cloud-native monitoring platform built as a personal DevOps project.

The goal is to build a complete DevOps workflow around a real application: **develop → test → containerize → monitor → automate → deploy to the cloud**.

The project uses **FastAPI, Docker, Prometheus, Grafana and GitHub Actions**, with cloud deployment planned as the next stage.

---

## 🎯 Project Goal

CloudPulse was created to learn and demonstrate practical **DevOps and Cloud Engineering** concepts through one complete project.

The platform monitors the health and performance of an application and provides a dashboard for:

* CPU usage
* Memory usage
* Disk usage
* HTTP request rate
* HTTP 5xx error rate

The project is intentionally small enough to understand while following practices used in real-world DevOps environments.

---

## 🏗️ Architecture

```text
                        CloudPulse
                            │
                            ▼
                       FastAPI API
                            │
                    ┌───────┴────────┐
                    │                │
                Application       /metrics
                  endpoints           │
                                     ▼
                                Prometheus
                                     │
                                     ▼
                                  Grafana
                                     │
                                     ▼
                              Monitoring Dashboard
```

The complete environment runs using Docker Compose.

---

## 🛠️ Tech Stack

| Technology         | Purpose                           |
| ------------------ | --------------------------------- |
| **Python**         | Application development           |
| **FastAPI**        | REST API                          |
| **Prometheus**     | Metrics collection and storage    |
| **Grafana**        | Metrics visualization             |
| **Docker**         | Application containerization      |
| **Docker Compose** | Local multi-container environment |
| **Pytest**         | Automated testing                 |
| **Ruff**           | Python linting and code quality   |
| **Bandit**         | Python security scanning          |
| **GitHub Actions** | CI/CD automation                  |
| **Git**            | Version control                   |

---

## 📊 Monitoring

CloudPulse exposes application and system metrics through the `/metrics` endpoint.

Prometheus periodically scrapes this endpoint and stores the metrics.

Grafana then queries Prometheus and visualizes the data.

### Current Dashboard

The Grafana dashboard contains:

* 🖥️ **CPU Usage** — current CPU utilization
* 🧠 **Memory Usage** — current memory utilization
* 💾 **Disk Usage** — current disk utilization
* 📈 **HTTP Request Rate** — requests per second over time
* 🚨 **HTTP 5xx Error Rate** — server errors per second over time

The Grafana dashboard is stored as **JSON in the repository**, making it reproducible and version-controlled.

---

## 🐳 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/eya-lachhab/cloudpulse.git
cd cloudpulse
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate it

**Git Bash / Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the tests

```bash
python -m pytest
```

Expected result:

```text
5 passed
```

---

## 🚀 Run with Docker

Build and start the complete environment:

```bash
docker compose up -d --build
```

Check the containers:

```bash
docker compose ps
```

Stop the environment:

```bash
docker compose down
```

---

## 🌐 Services

Once the containers are running:

| Service            | URL                           |
| ------------------ | ----------------------------- |
| CloudPulse API     | http://localhost:8000         |
| Health check       | http://localhost:8000/health  |
| System metrics     | http://localhost:8000/system  |
| Prometheus metrics | http://localhost:8000/metrics |
| Prometheus         | http://localhost:9090         |
| Grafana            | http://localhost:3000         |

---

## 🔍 Example API

### System information

```http
GET /system
```

Example response:

```json
{
  "hostname": "cloudpulse",
  "cpu": {
    "usage_percent": 10.2,
    "cores": 8
  },
  "memory": {
    "usage_percent": 35.4,
    "total_gb": 7.69
  },
  "disk": {
    "usage_percent": 12.8
  },
  "uptime_seconds": 372
}
```

---

## 🧪 Testing Error Monitoring

CloudPulse includes a test endpoint that intentionally generates a server error:

```http
GET /test-error
```

It returns:

```text
HTTP 500 Internal Server Error
```

The middleware records the error as:

```text
status="500"
```

Prometheus can then calculate the 5xx request rate, which is visualized in Grafana.

This provides a simple way to validate the complete monitoring pipeline:

```text
/test-error
     ↓
HTTP 500
     ↓
FastAPI middleware
     ↓
Prometheus metric
     ↓
Prometheus
     ↓
Grafana
```

---

## 🔄 Current DevOps Workflow

The project is being developed incrementally.

### Completed

* [x] FastAPI application
* [x] Health endpoint
* [x] System monitoring endpoint
* [x] Prometheus metrics
* [x] HTTP request metrics
* [x] HTTP 5xx error tracking
* [x] Automated tests
* [x] Docker containerization
* [x] Docker Compose environment
* [x] Prometheus integration
* [x] Grafana integration
* [x] Grafana dashboard
* [x] Dashboard as Code

### Next Steps

* [ ] GitHub Actions CI
* [ ] Automated testing on every push
* [ ] Ruff linting
* [ ] Bandit security scanning
* [ ] Automated Docker image build
* [ ] Container registry
* [ ] Cloud deployment
* [ ] Infrastructure as Code with Terraform
* [ ] Production health checks
* [ ] Alerting
* [ ] HTTPS

---

## ☁️ Planned Cloud Architecture

The final goal is to deploy CloudPulse to a cloud environment and automate the deployment through GitHub Actions.

```text
Developer
    │
    │ git push
    ▼
 GitHub
    │
    ▼
GitHub Actions
    │
    ├── Pytest
    ├── Ruff
    ├── Bandit
    └── Docker Build
            │
            ▼
     Container Registry
            │
            ▼
       Cloud Platform
            │
      ┌─────┴─────┐
      ▼           ▼
 CloudPulse   Monitoring
                 │
           ┌─────┴─────┐
           ▼           ▼
       Prometheus   Grafana
```

---

## 📚 What This Project Demonstrates

CloudPulse is designed to demonstrate practical experience with:

* REST API development
* Linux and container environments
* Docker and Docker Compose
* CI/CD concepts
* Automated testing
* Code quality and security scanning
* Application observability
* Prometheus metrics
* Grafana dashboards
* Infrastructure automation
* Cloud deployment
* Infrastructure as Code

---

## 👩‍💻 Author

**Eya Lachhab**

DevOps / Automation Engineer

Interested in **Cloud, DevOps, Automation, CI/CD and Generative AI**.

---

> 🚧 **CloudPulse is an ongoing personal project.**
>
> The architecture and features are being developed incrementally to explore real-world DevOps and cloud engineering practices.