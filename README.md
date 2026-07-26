# 🏭 Smart Factory Digital Twin

A Smart Factory Digital Twin built using **FastAPI, PostgreSQL, SQLAlchemy, and MQTT** to simulate Industrial IoT communication. The project demonstrates how multiple machines and sensors communicate in real time, store data in a database, and expose REST APIs for future analytics and dashboard visualization.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)
![Status](https://img.shields.io/badge/Progress-Day%205-success)


---

# 📌 Project Overview

This project simulates an Industry 4.0 manufacturing environment where multiple factory machines continuously generate sensor data.

The backend receives this data through MQTT, stores it in PostgreSQL, and exposes REST APIs using FastAPI.

Current implementation includes:

- FastAPI Backend
- PostgreSQL Database
- SQLAlchemy ORM
- REST APIs
- MQTT Communication
- Multi-Sensor Simulation
- Multi-Machine Simulation
- Real-Time Database Updates

---

# 🚀 Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python 3.13 |
| Backend | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| MQTT Broker | Mosquitto |
| MQTT Client | Paho MQTT |
| API Documentation | Swagger UI |
| Version Control | Git & GitHub |
| IDE | Visual Studio Code |

---

# 🏗 Project Architecture

```
                   Smart Factory

     Temperature Sensor
     Pressure Sensor
     Humidity Sensor
     Vibration Sensor
     Machine Status

             │

             ▼

        MQTT Publisher

             │

             ▼

      Mosquitto Broker

             │

             ▼

       MQTT Subscriber

             │

             ▼

        Service Layer

             │

             ▼

      SQLAlchemy ORM

             │

             ▼

      PostgreSQL Database

             │

             ▼

         FastAPI APIs

             │

             ▼

      Swagger Documentation
```

---

# 📂 Project Structure

```
backend/

app/

├── api/
├── database/
│   ├── base.py
│   ├── session.py
│   └── init_db.py
│
├── models/
│   ├── machine.py
│   └── sensor.py
│
├── schemas/
│   ├── machine.py
│   └── sensor.py
│
├── routers/
│   ├── machine.py
│   └── sensor.py
│
├── services/
│   ├── machine_service.py
│   └── mqtt_service.py
│
├── mqtt/
│   ├── publisher.py
│   ├── subscriber.py
│   └── topics.py
│
└── main.py
```

---

# ⚙ Features Implemented

## Backend

- FastAPI project setup
- Layered architecture
- API routing
- Dependency Injection
- Swagger Documentation

---

## Database

- PostgreSQL integration
- SQLAlchemy ORM
- Machine model
- Sensor model
- Database session management

---

## REST APIs

### Machine APIs

- Create Machine
- Get All Machines
- Get Machine by ID
- Update Machine
- Delete Machine

### Sensor APIs

- Create Sensor
- Get All Sensors
- Get Sensor by ID
- Update Sensor
- Delete Sensor

---

## MQTT Integration

Implemented real-time communication using MQTT.

### Publisher

Publishes

- Temperature
- Pressure
- Humidity
- Vibration
- Machine Status

---

### Subscriber

Receives MQTT messages

Stores sensor values in PostgreSQL

Updates machine status automatically

---

# 🏭 Factory Simulation

## Machines

- CNC Machine
- Robot Arm
- Conveyor Belt

---

## Sensor Types

- Temperature
- Pressure
- Humidity
- Vibration

---

## Machine Status

Random simulation of

- Running
- Idle
- Maintenance
- Fault

---

# 📡 MQTT Topics

```
factory/temperature

factory/pressure

factory/vibration

factory/humidity

factory/machine_status
```

---

# 📦 Sample MQTT Payload

```json
{
    "machine": "Robot Arm",
    "status": "Running"
}
```

---

# 🌐 REST API Endpoints

## Machines

| Method | Endpoint |
|----------|-----------|
| GET | /api/v1/machines |
| GET | /api/v1/machines/{id} |
| POST | /api/v1/machines |
| PUT | /api/v1/machines/{id} |
| DELETE | /api/v1/machines/{id} |

---

## Sensors

| Method | Endpoint |
|----------|-----------|
| GET | /api/v1/sensors |
| GET | /api/v1/sensors/{id} |
| POST | /api/v1/sensors |
| PUT | /api/v1/sensors/{id} |
| DELETE | /api/v1/sensors/{id} |

---

# 📈 Current Workflow

```
Factory Simulation

        │

        ▼

MQTT Publisher

        │

        ▼

Mosquitto Broker

        │

        ▼

MQTT Subscriber

        │

        ▼

Service Layer

        │

        ▼

PostgreSQL

        │

        ▼

FastAPI REST APIs

        │

        ▼

Swagger UI
```

---

# 📊 Project Progress

| Module | Status |
|----------|--------|
| Project Setup | ✅ |
| FastAPI Backend | ✅ |
| PostgreSQL | ✅ |
| SQLAlchemy | ✅ |
| Models | ✅ |
| CRUD APIs | ✅ |
| Swagger | ✅ |
| MQTT Publisher | ✅ |
| MQTT Subscriber | ✅ |
| Multi-Sensor Simulation | ✅ |
| Multi-Machine Simulation | ✅ |
| Database Integration | ✅ |
| REST APIs | ✅ |
| Analytics Layer | ⏳ |
| Dashboard | ⏳ |
| Docker | ⏳ |
| Machine Learning | ⏳ |

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with

- REST API Development
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- MQTT Protocol
- Publish–Subscribe Architecture
- Industrial IoT Communication
- Layered Backend Architecture
- Database Design
- JSON Messaging
- Real-Time Data Processing

---

# 🚀 Upcoming Development

## Phase 2

- Factory Analytics APIs
- Machine Health Monitoring
- Live Statistics
- KPI Calculations

---

## Phase 3

- React Dashboard
- Live Charts
- Factory Overview
- Machine Cards
- Sensor Visualization

---

## Phase 4

- Docker Deployment
- Authentication
- Role-Based Access
- Logging
- Testing

---

## Phase 5

- Machine Learning
- Predictive Maintenance
- Anomaly Detection
- Equipment Failure Prediction

---

# 📅 Development Timeline

| Day | Progress |
|------|----------|
| Day 1 | Project Setup & Architecture |
| Day 2 | PostgreSQL Integration |
| Day 3 | SQLAlchemy Models |
| Day 4 | REST API Development |
| Day 5 | CRUD Operations |
| Day 6 | MQTT Integration |
| Day 7 | Multi-Machine Factory Simulation |

---

# 📌 Current Status

**Version:** v0.7.0

**Completion:** Approximately **70%**

Current capabilities include:

- Real-time factory simulation
- Multiple machines
- Multiple sensors
- MQTT communication
- PostgreSQL integration
- REST APIs
- Swagger documentation

The next milestone is building an analytics layer that summarizes live factory data and powers a dashboard for monitoring machine health and production status.

---

## 👨‍💻 Author

**R. Sumukh Aryan**

Electronics and Communication Engineering

Smart Factory | Industrial IoT | Embedded Systems | FastAPI | PostgreSQL | MQTT
