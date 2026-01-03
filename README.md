# 🚀 Python DevOps CI/CD Pipeline

## 📌 Overview

This project demonstrates an **end-to-end CI/CD pipeline** for a containerized Python application using modern DevOps tools. It showcases the complete workflow from **source code management to automated build, container image publishing, and Kubernetes deployment**.

This repository was created as a **hands-on learning project** to gain practical exposure to **CI/CD pipelines, Docker, Jenkins, and Kubernetes**.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **CI/CD Tool:** Jenkins
* **Containerization:** Docker
* **Container Registry:** Docker Hub
* **Container Orchestration:** Kubernetes
* **Version Control:** Git & GitHub

---

## ⚙️ CI/CD Pipeline Workflow

1. Source code is pushed to the GitHub repository
2. Jenkins pipeline is triggered automatically
3. Docker image is built from the Python application
4. Image is tagged using the Jenkins build number
5. Docker image is pushed securely to Docker Hub
6. Kubernetes deployment is updated using rolling updates

---

## 🧩 Jenkins Pipeline Stages

* **Checkout Code** – Pulls the latest source code from GitHub
* **Build Docker Image** – Builds a Docker image for the Python app
* **Push to Docker Hub** – Pushes the image using Jenkins-managed credentials
* **Deploy to Kubernetes** – Updates the running deployment using `kubectl set image`

---

## 🐳 Docker

* Application is packaged into a Docker image
* Ensures consistency across development and deployment environments
* Uses versioned image tags for traceability

---

## ☸️ Kubernetes Deployment

* Application is deployed as a Kubernetes Deployment
* Rolling updates are used to ensure minimal downtime
* Image updates are applied dynamically without recreating resources

---

## 📂 Project Structure

```
.
├── Dockerfile
├── Jenkinsfile
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔐 Security & Best Practices

* Docker Hub credentials are securely managed using Jenkins credentials
* No sensitive information is hard-coded
* CI/CD pipeline follows separation of build and deployment responsibilities

---

## 🎯 Learning Outcomes

* Hands-on experience with Jenkins CI/CD pipelines
* Practical understanding of Docker image creation and publishing
* Exposure to Kubernetes deployments and rolling updates
* Experience integrating multiple DevOps tools into a single workflow

---

## 🚧 Scope for Improvements

* Add automated testing stages to the pipeline
* Use Helm charts for Kubernetes deployments
* Integrate monitoring and logging (Prometheus / Grafana)
* Implement GitHub Actions as an alternative CI/CD pipeline

---

## 📌 Disclaimer

This project is intended for **learning and demonstration purposes only** and does not represent a production-ready system.

---

## 👤 Author

**Tharaka Bandara**
GitHub: [https://github.com/tharaka9](https://github.com/tharaka9)
