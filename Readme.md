# 📦 Dockerized Flask–MySQL Application with CI

A backend application built using **Flask** and **MySQL**, containerized with **Docker** and orchestrated using **Docker Compose**.  
The project also includes a **CI pipeline using GitHub Actions** to automatically build the Docker image on every code push.

This project demonstrates backend development, containerization, and basic DevOps practices.

---

## 🛠 Tech Stack

- **Backend:** Python (Flask)
- **Database:** MySQL
- **Containerization:** Docker
- **Orchestration:** Docker Compose
- **CI:** GitHub Actions
- **Version Control:** Git & GitHub

---

## 📁 Project Structure
dockerized-flask-mysql-app
│
├── app/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── .github/
│ └── workflows/
│ └── docker-ci.yml
│
├── docker-compose.yml
├── .env
└── README.md

---

## ⚙️ Features

- Flask backend with REST endpoints
- MySQL database running in a separate container
- Multi-container setup using Docker Compose
- Environment-based configuration using `.env`
- Health check and database connectivity endpoints
- CI pipeline to automatically build Docker images on every push

---

## 🌐 API Endpoints

| Endpoint | Description |
|--------|-------------|
| `/` | Root endpoint |
| `/health` | Application health check |
| `/db` | Database connectivity check |

---

## ▶️ How to Run Locally

### Prerequisites
- Docker
- Docker Compose

## 🔁 CI Pipeline (GitHub Actions)

This project uses GitHub Actions for Continuous Integration.

What the CI does:

Triggers on every push to the main branch

Checks out the repository

Builds the Docker image using the Dockerfile

This ensures that Docker builds do not break as the code evolves.

## 📌 Learning Outcomes

Through this project, I gained hands-on experience in:

Containerizing backend applications

Managing multi-service applications with Docker Compose

Debugging container and networking issues

Using environment variables for configuration

Setting up CI pipelines using GitHub Actions

Understanding real-world DevOps workflows

## 🚀 Future Improvements

Add automated tests to CI pipeline

Push Docker image to Docker Hub

Deploy application to AWS EC2

Add monitoring and logging

## 👤 Author

Hirakjyoti Das

GitHub: https://github.com/hirakjyoti-das

LinkedIn: https://www.linkedin.com/in/hirakjyoti-das/