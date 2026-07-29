
# 🏭 Smart Factory Digital Twin

A full-stack Industrial IoT (IIoT) monitoring platform that simulates a real-time smart factory using **React**, **FastAPI**, **PostgreSQL**, and **MQTT**.

The project provides live machine monitoring, predictive health analysis, historical sensor visualization, alert management, and professional report generation.


![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)

---

## 📸 Dashboard Preview

> Add screenshots here after deployment.

```
Dashboard

✔ Factory Overview
✔ Live Sensor Monitoring
✔ Factory Floor
✔ Machine Details
✔ Analytics Charts
✔ Activity Feed
✔ Alerts
✔ CSV Export
✔ PDF Export
```

---

# 🚀 Features

## 🏭 Factory Monitoring

- Live industrial dashboard
- Real-time MQTT sensor updates
- Factory overview cards
- Factory floor visualization
- Machine status monitoring
- Automatic dashboard refresh (5 seconds)

---

## 📊 Sensor Monitoring

Monitor live values of

- 🌡 Temperature
- ⚙ Pressure
- 💧 Humidity
- 📳 Vibration

---

## ❤️ Machine Health Analytics

Each machine receives a dynamic health score based on

- Temperature
- Pressure
- Humidity
- Vibration
- Operating Status

Health Levels

| Score | Condition |
|--------|-----------|
| 95-100 | Excellent |
| 80-94 | Healthy |
| 60-79 | Warning |
| 0-59 | Critical |

---

## 🚨 Smart Alert System

Automatically detects

- High Temperature
- High Vibration
- Low Pressure
- High Pressure
- Machine Fault
- Maintenance Required

Features

- Live Alerts Panel
- Toast Notifications
- Critical Fault Highlighting

---

## 🏭 Factory Floor

Interactive machine cards displaying

- Machine Name
- Machine Status
- Health Score
- Health Progress Bar
- Sensor Values
- Condition
- Last Updated

---

## 🔍 Machine Search & Filter

Search machines by name

Filter machines by

- Running
- Idle
- Maintenance
- Fault

---

## 📈 Historical Analytics

Real-time charts

- Temperature
- Pressure
- Humidity
- Vibration

Historical sensor visualization using Chart.js.

---

## 📋 Machine Details Panel

Click any machine to view

- Complete Sensor Values
- Machine Health
- Condition
- Trend Chart
- Alert Summary
- Recent Events
- Last Updated Time

---

## 📑 Report Generation

Generate professional reports.

### Export CSV

Downloads

- Machine Status
- Sensor Values
- Health
- Condition

### Export PDF

Professional report including

- Factory Summary
- Machine Table
- Health Status
- Report Timestamp

---

## ⚡ Live Dashboard

Dashboard updates every

```
5 Seconds
```

using FastAPI APIs.

---
## 📊 Analytics Dashboard

The analytics module provides real-time insights into factory operations.

### Features

- Live KPI Dashboard
- Machine-wise Analytics
- Temperature Trend Analysis
- Pressure Monitoring
- Humidity Monitoring
- Vibration Trend Analysis
- Machine Health Score
- Factory Health Overview
- Predictive Maintenance
- Remaining Useful Life (RUL)
- Failure Probability Estimation
- AI Maintenance Recommendation
- Real-time Auto Refresh

---

# 🏗 System Architecture

```
                    MQTT Simulator
                           │
                           ▼
                  MQTT Subscriber
                     (FastAPI)

                           │
                           ▼
                  Analytics Engine

                           │
                           ▼
                    PostgreSQL

                           │
                           ▼
                    REST APIs

                           │
                           ▼
                  React Dashboard
```

---

# 🛠 Tech Stack

## Frontend

- React
- Axios
- Chart.js
- React Toastify
- jsPDF
- jsPDF AutoTable
- PapaParse

---

## Backend

- FastAPI
- SQLAlchemy
- Pydantic
- MQTT
- Uvicorn

---

## Database

- PostgreSQL

---

## Communication

- MQTT

---

# 📂 Project Structure

```
Smart-Factory-Digital-Twin/

│
├── backend/
│
│   ├── analytics/
│   ├── database/
│   ├── models/
│   ├── mqtt/
│   ├── routes/
│   ├── services/
│   └── main.py
│
├── frontend/
│
│   ├── components/
│   │
│   ├── Header
│   ├── OverviewCards
│   ├── SensorCards
│   ├── AlertsPanel
│   ├── FactoryFloor
│   ├── MachineDetails
│   ├── MachineTable
│   ├── ActivityFeed
│   ├── TemperatureChart
│   ├── PressureChart
│   ├── HumidityChart
│   ├── VibrationChart
│   ├── ExportCSV
│   ├── ExportPDF
│   └── ReportSummary
│
│
├── README.md
│
└── package.json
```

---

# 📡 API Endpoints

## Analytics

```
GET /analytics/overview
```

Returns

- Total Machines
- Running
- Idle
- Maintenance
- Fault
- Average Temperature
- Average Health

---

```
GET /analytics/live
```

Returns

Current factory sensor values.

---

```
GET /analytics/machine-health
```

Returns

- Machine Health
- Condition
- Sensor Data

---

```
GET /analytics/history
```

Returns historical sensor readings.

---

## Alerts

```
GET /alerts/
```

Returns active alerts.

---

# 🧠 Health Calculation

Machine health is calculated dynamically using

- Temperature
- Pressure
- Humidity
- Vibration
- Current Machine Status

The score is normalized between

```
0 – 100
```

---

# 📊 Dashboard Components

- Header
- Overview Cards
- Sensor Cards
- Alerts Panel
- Search Bar
- Status Filter
- Factory Floor
- Machine Details
- Activity Feed
- Machine Table
- Temperature Chart
- Pressure Chart
- Humidity Chart
- Vibration Chart
- CSV Export
- PDF Export

---

# 🚀 Installation

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 📦 Required Packages

## Backend

```text
fastapi
uvicorn
sqlalchemy
psycopg2
paho-mqtt
pydantic
```

---

## Frontend

```bash
npm install axios

npm install chart.js react-chartjs-2

npm install react-toastify

npm install jspdf jspdf-autotable

npm install papaparse
```

---

# 🎯 Current Progress

## Backend

- ✅ REST APIs
- ✅ PostgreSQL Integration
- ✅ MQTT Subscriber
- ✅ Analytics Engine
- ✅ Health Calculation
- ✅ Alert Generation

---

## Frontend

- ✅ Dashboard
- ✅ Live Monitoring
- ✅ Factory Overview
- ✅ Machine Details
- ✅ Historical Charts
- ✅ Search
- ✅ Filters
- ✅ Toast Notifications
- ✅ CSV Export
- ✅ PDF Export

---

# 🔜 Upcoming Features

- Analytics Page
- Historical Reports
- Machine Performance Trends
- Docker Support
- User Authentication
- Cloud Deployment
- Live MQTT Status Monitoring
- Predictive Maintenance Dashboard

---

## Dashboard

### Analytics Dashboard
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/af00f3d5-6d90-4ce8-aaae-35d66053b5a1" />

### Predictive Maintenance

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ff3968a6-e5b8-4d04-a0ae-00c27e21cdff" />



# 👨‍💻 Author

**R Sumukh Aryan**

Electronics & Communication Engineering

Industrial IoT | Embedded Systems | Full Stack Development

---

# ⭐ If you like this project

Give the repository a ⭐ on GitHub.
