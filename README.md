# 🏭 Smart Factory Digital Twin & Predictive Maintenance Platform

![Project Status](https://img.shields.io/badge/Status-Backend%20Development-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# Overview

The **Smart Factory Digital Twin & Predictive Maintenance Platform** is an Industry 4.0 engineering project that simulates a modern manufacturing environment.

The platform combines Industrial IoT, backend engineering, machine learning, data visualization, and engineering management practices to demonstrate how smart factories monitor equipment, predict failures, and improve operational efficiency.

This project is being developed as an **8-week portfolio project** following professional software engineering workflows including Agile planning, Git version control, technical documentation, and sprint management.

---

# Objectives

- Develop a Smart Factory Digital Twin
- Simulate industrial machine data
- Build REST APIs using FastAPI
- Implement MQTT communication
- Store sensor data in PostgreSQL
- Predict equipment failures using Machine Learning
- Visualize KPIs using Grafana
- Containerize the application using Docker

---

## 📈 Project Progress

| Module | Status |
|---------|--------|
| Planning | ✅ Completed |
| Documentation | ✅ Completed |
| GitHub Setup | ✅ Completed |
| FastAPI Backend | ✅ Completed |
| Modular Routing | ✅ Completed |
| API Versioning | ✅ Completed |
| Pydantic Schemas | ✅ Completed |
| PostgreSQL Integration | ✅ Completed |
| SQLAlchemy ORM | ✅ Completed |
| Database Services | ✅ Completed |
| CRUD (Read) | ✅ Completed |
| CRUD (Create/Update/Delete) | 🚧 In Progress |
| MQTT Integration | ⏳ Upcoming |
| Dashboard | ⏳ Upcoming |
| Machine Learning | ⏳ Upcoming |
| Deployment | ⏳ Upcoming |

**Overall Progress:** **50%**
---

# Technology Stack

## Backend

- Python
- FastAPI
- Uvicorn

## Frontend (Upcoming)

- React
- Tailwind CSS

## Database

- PostgreSQL

## Messaging

- MQTT (Mosquitto)

## Machine Learning

- Scikit-Learn
- Pandas
- NumPy

## Dashboard

- Grafana

## DevOps

- Docker
- GitHub Actions

---
## Current Features

- FastAPI REST API
- API Versioning
- Modular Routers
- Environment Variables
- Logging
- PostgreSQL Integration
- SQLAlchemy ORM
- Database Sessions
- Service Layer
- Machine API
- Sensor API
- Swagger Documentation

---
# Current Project Structure

```text
SmartFactory-DigitalTwin
│
backend
│
├── app
│   ├── api
│   ├── core
│   ├── database
│   │   ├── base.py
│   │   ├── connection.py
│   │   ├── dependencies.py
│   │   └── session.py
│   │
│   ├── models
│   │   ├── machine.py
│   │   └── sensor.py
│   │
│   ├── schemas
│   ├── services
│   └── main.py
│
├── create_tables.py
├── test_connection.py
└── requirements.txt
└── README.md
│
├── data
├── database
├── deployment
├── docs
├── frontend
├── models
├── mqtt
├── scripts
├── simulation
├── src
├── tests
│
├── README.md
├── CHANGELOG.md
├── PROJECT_ROADMAP.md
└── LICENSE
```
## 🗄 Database Architecture

The application now uses PostgreSQL as its primary database and SQLAlchemy ORM for database interactions.

### Database

- PostgreSQL 18
- SQLAlchemy ORM
- psycopg2 Driver

### Tables

- machines
- sensors

### Backend Flow

Client

↓

FastAPI Router

↓

Dependency Injection

↓

Service Layer

↓

SQLAlchemy ORM

↓

PostgreSQL Database
---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome endpoint |
| GET | `/api/v1/health` | Health check |
| GET | `/api/v1/machines` | Retrieve machine information |
| GET | `/api/v1/sensors` | Retrieve sensor information |
```

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/Sumukharyan/SmartFactory-DigitalTwin.git
```

---

## Navigate to Backend

```bash
cd SmartFactory-DigitalTwin/backend
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Windows CMD

```cmd
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Development Server

```bash
uvicorn app.main:app --reload
```

---

## Open API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# Project Roadmap

### Week 1

- Repository Setup ✅
- Documentation ✅
- FastAPI Setup ✅
- First REST API ✅

### Week 2

- Modular API Architecture
- Environment Configuration
- Logging
- Error Handling

### Week 3

- PostgreSQL Integration
- SQLAlchemy
- CRUD Operations

### Week 4

- MQTT Integration
- Machine Simulation

### Week 5

- Machine Learning
- Predictive Maintenance

### Week 6

- Grafana Dashboard
- Analytics

### Week 7

- Docker
- Deployment

### Week 8

- Testing
- Documentation
- Final Portfolio

### ✅ Completed

- Project Planning
- GitHub Setup
- Documentation
- FastAPI Setup
- Backend Architecture
- APIRouter
- Configuration
- Logging
- API Versioning
- Pydantic Schemas
- Swagger Documentation

### 🚧 Next

- PostgreSQL
- SQLAlchemy
- CRUD Operations
- Database Models

### ⏳ Upcoming

- MQTT
- Digital Twin
- Machine Learning
- Grafana
- Docker
- CI/CD
---

# Documentation

Project documentation is maintained in **Obsidian** and includes:

- Project Vision
- Requirements
- Sprint Planning
- Kanban Board
- Risk Register
- Architecture Notes
- Learning Notes
- Daily Development Journal
- Engineering Decisions

---

# Skills Demonstrated

- Backend Development
- REST API Design
- Python Programming
- Git & GitHub
- Software Architecture
- Engineering Documentation
- Agile Sprint Planning
- Engineering Management Practices

---

# Future Enhancements

- User Authentication
- Role-Based Access Control
- Live MQTT Communication
- Real-Time Dashboard
- Docker Compose Deployment
- Kubernetes Support
- Cloud Deployment
- CI/CD Pipeline

---

# Author

**R Sumukh Aryan**

Bachelor of Engineering (Electronics & Communication Engineering)


---

# License

This project is licensed under the MIT License.
