# 🏭 Smart Factory Digital Twin

> An Industry 4.0 Digital Twin platform built using FastAPI, PostgreSQL, SQLAlchemy, and MQTT (Upcoming) for real-time factory monitoring and predictive maintenance.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)
![Status](https://img.shields.io/badge/Progress-Day%205-success)

---

# 📖 Project Overview

This project simulates a **Smart Factory Digital Twin** capable of monitoring industrial machines and sensors using modern backend technologies.

The objective is to build a production-ready backend that will eventually support:

- Real-time machine monitoring
- Sensor data acquisition
- MQTT communication
- Predictive maintenance
- Analytics dashboard
- Machine Learning
- Docker deployment

This repository follows industry-standard backend architecture and software engineering practices.

---

# 🚀 Current Features

## Backend

- FastAPI
- Modular Project Structure
- API Versioning
- Dependency Injection
- Environment Configuration
- Logging
- Swagger Documentation

---

## Database

- PostgreSQL
- SQLAlchemy ORM
- Database Sessions
- ORM Models
- Service Layer
- CRUD Operations

---

## Machine APIs

- ✅ Create Machine
- ✅ Read All Machines
- ✅ Read Machine by ID
- ✅ Update Machine
- ✅ Delete Machine

---

## Sensor APIs

- ✅ Create Sensor
- ✅ Read All Sensors
- ✅ Read Sensor by ID
- ✅ Update Sensor
- ✅ Delete Sensor

---

## API Features

- Response Models
- Path Parameters
- HTTP Status Codes
- Exception Handling
- Swagger Testing

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn

## Database

- PostgreSQL
- SQLAlchemy
- psycopg2-binary

## Documentation

- Markdown
- Obsidian

## Version Control

- Git
- GitHub

## Development Tools

- VS Code
- pgAdmin

---

# 📂 Project Structure

```
smart-factory-digital-twin/
│
├── backend/
│
│   ├── app/
│   │
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │
│   ├── core/
│   │
│   ├── database/
│   │
│   ├── models/
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │
│   └── main.py
│
├── docs/
│
├── README.md
│
└── .gitignore
```

---

# 🏗 Architecture

```
Client

      │

Swagger UI

      │

FastAPI Router

      │

Dependency Injection

      │

Service Layer

      │

SQLAlchemy ORM

      │

PostgreSQL
```

---

# 🌐 Available APIs

## Health

| Method | Endpoint |
|---------|----------|
| GET | /api/v1/health |

---

## Machines

| Method | Endpoint |
|---------|----------|
| GET | /api/v1/machines |
| GET | /api/v1/machines/{id} |
| POST | /api/v1/machines |
| PUT | /api/v1/machines/{id} |
| DELETE | /api/v1/machines/{id} |

---

## Sensors

| Method | Endpoint |
|---------|----------|
| GET | /api/v1/sensors |
| GET | /api/v1/sensors/{id} |
| POST | /api/v1/sensors |
| PUT | /api/v1/sensors/{id} |
| DELETE | /api/v1/sensors/{id} |

---

# 🗄 Database

Database Name

```
smart_factory
```

Tables

```
machines

sensors
```

---

# ⚙ Technologies Learned

## FastAPI

- APIRouter
- Dependency Injection
- Response Models
- Path Parameters
- HTTPException
- Status Codes

---

## SQLAlchemy

- ORM Models
- Database Sessions
- CRUD Operations
- Query
- Filter
- Commit
- Refresh
- Delete

---

## PostgreSQL

- Database Creation
- Table Creation
- Data Persistence
- pgAdmin

---

# 📈 Current Progress

Planning               ██████████ 100%

Documentation          ██████████ 100%

Backend                ██████████ 100%

Database               ██████████ 100%

REST APIs              ██████████ 100%

MQTT                   ███████░░░ 70%

Simulation             ███░░░░░░░ 30%

Dashboard              ░░░░░░░░░░ 0%

Machine Learning       ░░░░░░░░░░ 0%

Deployment             ░░░░░░░░░░ 0%

Overall Project        ███████░░░ 70%

---

# 🏆 Completed Milestones

## Sprint 1

- Project Planning
- Repository Setup
- FastAPI Installation
- Project Structure
- Configuration Module
- Logging
- PostgreSQL Integration
- SQLAlchemy Setup
- Database Models
- Service Layer
- Database Read APIs

---

## Sprint 2 (Current)

- Machine CRUD
- Sensor CRUD
- RESTful API Design
- Exception Handling
- Swagger API Testing

---

# 📅 Roadmap

## Phase 1 ✅

Backend Foundation

- FastAPI
- PostgreSQL
- SQLAlchemy
- CRUD APIs

---

## Phase 2 🚧

Real-Time Communication

- MQTT Broker
- MQTT Publisher
- MQTT Subscriber
- Sensor Simulation
- Machine Simulation

---

## Phase 3

Dashboard

- React
- Charts
- Live Factory Status
- Analytics

---

## Phase 4

Machine Learning

- Predictive Maintenance
- Failure Detection
- Equipment Health Prediction

---

## Phase 5

Deployment

- Docker
- Docker Compose
- CI/CD
- Cloud Deployment

---

# 📊 Overall Progress

```
Planning               ██████████ 100%

Documentation          ██████████ 100%

Backend                ██████████ 100%

Database               ██████████ 100%

REST APIs              ██████████ 100%

MQTT                   ░░░░░░░░░░   0%

Simulation             ░░░░░░░░░░   0%

Dashboard              ░░░░░░░░░░   0%

Machine Learning       ░░░░░░░░░░   0%

Deployment             ░░░░░░░░░░   0%

Overall Progress       ██████░░░░ 60%
```

---

# 🎯 Learning Outcomes

Through this project, I have gained practical experience in:

- Backend API Development
- RESTful API Design
- FastAPI Framework
- SQLAlchemy ORM
- PostgreSQL Database Design
- Layered Software Architecture
- Dependency Injection
- Error Handling
- API Testing using Swagger
- Git and GitHub Workflow

---

# 🚀 Next Steps

The next milestone is to transform the backend into a **real-time Smart Factory** by integrating MQTT.

Upcoming features include:

- MQTT Broker
- Sensor Data Streaming
- Machine State Simulation
- Live Dashboard
- WebSocket Support
- Predictive Maintenance
- Docker Deployment

---

# 👨‍💻 Author

**R Sumukh Aryan**

Bachelor of Engineering (Electronics and Communication Engineering)

Building Industry 4.0 projects using FastAPI, PostgreSQL, Embedded Systems, IoT, and Artificial Intelligence.
