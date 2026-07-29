# 🏭 Smart Factory Digital Twin Dashboard

![React](https://img.shields.io/badge/React-19-blue?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![MQTT](https://img.shields.io/badge/MQTT-IoT-orange)
![Industry 4.0](https://img.shields.io/badge/Industry-4.0-success)
![License](https://img.shields.io/badge/License-MIT-green)

A complete **Industry 4.0 Smart Factory Digital Twin Dashboard** built using **FastAPI**, **React**, **PostgreSQL**, and **MQTT**.

The project simulates a manufacturing environment where multiple machines continuously generate sensor data. The dashboard visualizes real-time production metrics, machine health, analytics, historical trends, reports, and an interactive digital twin of the factory floor.

This project demonstrates concepts commonly used in modern Industrial IoT (IIoT) platforms such as:

- Siemens MindSphere
- Azure IoT Central
- AWS IoT SiteWise
- Bosch IoT Suite
- PTC ThingWorx

---

## Current Progress

✔ Day 1–22 Completed

Modules implemented:

- Dashboard
- Analytics
- Reports
- Factory Floor Digital Twin
- Machine Health Monitoring
- Predictive Maintenance
- Industrial Dashboard UI

# 📖 Project Overview

Modern manufacturing plants generate enormous amounts of operational data through sensors, PLCs, and industrial controllers.

This project recreates a smart factory where machine data is collected, stored, analyzed, and visualized through an interactive web dashboard.

The application consists of four major modules:

- Dashboard
- Analytics
- Reports
- Factory Floor Digital Twin

The backend simulates sensor values using MQTT and stores them inside PostgreSQL.

The frontend periodically retrieves data using REST APIs and presents it through modern charts, KPIs, machine cards, and interactive dashboards.

---

## Objectives

- Learn Full Stack Development
- Learn FastAPI
- Learn PostgreSQL
- Learn SQLAlchemy
- Learn MQTT
- Learn React
- Learn Industrial IoT
- Learn Digital Twin Concepts
- Build a Portfolio Project

# ✨ Features

## Dashboard

- Live KPI Cards
- Sensor Monitoring
- Machine Status
- Factory Overview
- Auto Refresh

---

## Analytics

- Historical Trends
- Machine Selector
- Health Score
- Temperature Charts
- Pressure Charts
- Humidity Charts
- Vibration Charts
- Factory Insights
- Predictive Maintenance

---

## Reports

- Production Summary
- Performance Metrics
- Export Ready Tables

---

## Factory Floor

- Interactive Digital Twin
- Machine Cards
- Live Status
- Health Bars
- Live Monitoring
- Responsive Layout
- Analytics Integration
- Fault Animation

---

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- MQTT Simulator
- REST APIs
- Automatic Sensor Updates

---

## Frontend

- React
- Axios
- React Router
- Recharts
- Responsive UI

# 🛠️ Technology Stack

The Smart Factory Digital Twin is built using a modern full-stack architecture.

| Layer | Technology | Purpose |
|--------|------------|---------|
| Frontend | React | User Interface |
| Routing | React Router | Client-side Routing |
| HTTP Client | Axios | API Communication |
| Charts | Recharts | Data Visualization |
| Backend | FastAPI | REST API Development |
| ORM | SQLAlchemy | Database ORM |
| Database | PostgreSQL | Persistent Storage |
| IoT Communication | MQTT | Sensor Simulation |
| Version Control | Git & GitHub | Source Control |
| Language | Python | Backend Development |
| Language | JavaScript | Frontend Development |
| Styling | CSS3 | User Interface Design |

---

## Why These Technologies?

### React

- Component-based architecture
- Fast rendering
- Reusable UI components
- Large ecosystem

### FastAPI

- High performance
- Automatic API documentation
- Easy integration with SQLAlchemy
- Async support

### PostgreSQL

- Reliable relational database
- ACID compliance
- Excellent analytics support

### MQTT

- Lightweight IoT messaging protocol
- Real-time sensor communication
- Industry standard for IoT applications

### Recharts

- Interactive charts
- React-based visualization
- Responsive dashboards

# 🏗️ System Architecture

The project follows a layered architecture where sensor data flows from simulated machines to the frontend dashboard.

```text
                   +---------------------+
                   | Factory Machines    |
                   | (Simulation)        |
                   +----------+----------+
                              |
                              |
                           MQTT Broker
                              |
                              |
                    +---------v----------+
                    | MQTT Subscriber    |
                    +---------+----------+
                              |
                              |
                    +---------v----------+
                    | FastAPI Backend    |
                    | Business Logic     |
                    +---------+----------+
                              |
                              |
                       SQLAlchemy ORM
                              |
                              |
                    +---------v----------+
                    | PostgreSQL         |
                    +---------+----------+
                              |
                       REST API Requests
                              |
                    +---------v----------+
                    | React Frontend     |
                    +---------+----------+
                              |
                              |
                  Dashboard / Analytics /
                  Reports / Factory Floor
```

---

## Architecture Overview

### Sensor Layer

Machine sensors continuously generate:

- Temperature
- Pressure
- Humidity
- Vibration

---

### Communication Layer

Sensor values are transmitted using MQTT.

---

### Backend Layer

FastAPI performs:

- Data validation
- Database operations
- Health score calculations
- Analytics generation
- Report generation

---

### Database Layer

PostgreSQL stores:

- Machine information
- Sensor history
- Machine status
- Analytics data

---

### Frontend Layer

React retrieves data using REST APIs and displays:

- Live dashboards
- Charts
- Reports
- Factory Floor Digital Twin

# 📂 Project Structure

```text
smart-factory-digital-twin/

│
├── backend/
│   │
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── simulator.py
│   ├── mqtt_client.py
│   ├── main.py
│   │
│   ├── routers/
│   │     ├── dashboard.py
│   │     ├── analytics.py
│   │     └── reports.py
│   │
│   └── services/
│
├── frontend/
│   │
│   ├── src/
│   │
│   ├── components/
│   │     ├── Header.jsx
│   │     ├── DashboardCards.jsx
│   │     ├── SensorCards.jsx
│   │     ├── AnalyticsCards.jsx
│   │     ├── TemperatureChart.jsx
│   │     ├── PressureChart.jsx
│   │     ├── HumidityChart.jsx
│   │     ├── VibrationChart.jsx
│   │     ├── MachineCard.jsx
│   │     ├── FactoryFloor.jsx
│   │     └── HealthBar.jsx
│   │
│   ├── pages/
│   │     ├── Dashboard.jsx
│   │     ├── Analytics.jsx
│   │     ├── Reports.jsx
│   │     └── FactoryFloorPage.jsx
│   │
│   ├── services/
│   │     └── api.js
│   │
│   ├── App.jsx
│   └── index.css
│
├── docs/
│
├── README.md
│
└── requirements.txt
```

# ⚙️ Installation Guide

## Clone Repository

```bash
git clone https://github.com/yourusername/smart-factory-digital-twin.git

cd smart-factory-digital-twin
```

---

# Backend Setup

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the backend.

```bash
uvicorn main:app --reload
```

Backend URL

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

---

# Frontend Setup

Navigate to frontend.

```bash
cd frontend
```

Install packages.

```bash
npm install
```

Run React.

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# PostgreSQL

Create a PostgreSQL database.

Example

```
smart_factory
```

Update your database connection inside

```
database.py
```

---

# MQTT

Start an MQTT broker.

Run the simulator.

```bash
python simulator.py
```

The simulator continuously publishes machine sensor values to MQTT topics.

# ⚙️ Backend Documentation

The backend is built using **FastAPI**, a modern Python framework for developing high-performance REST APIs.

The backend is responsible for:

- Receiving sensor data
- Storing machine history
- Calculating machine health
- Providing analytics
- Serving reports
- Exposing REST APIs for the frontend

---

## Backend Responsibilities

### Dashboard APIs

Provide live factory information including:

- Active machines
- Production statistics
- Sensor values
- Machine status

---

### Analytics APIs

Generate historical data and statistics including:

- Temperature history
- Pressure history
- Humidity history
- Vibration history
- Machine health
- Factory insights

---

### Reports APIs

Generate production reports including:

- Machine utilization
- Average sensor values
- Production summaries
- Export-ready report data

---

## Backend Technologies

- FastAPI
- SQLAlchemy
- PostgreSQL
- MQTT
- Pydantic
- Uvicorn

---

## Backend Folder Structure

```text
backend/

├── main.py
├── database.py
├── models.py
├── schemas.py
├── simulator.py
├── mqtt_client.py
│
├── routers/
│     ├── dashboard.py
│     ├── analytics.py
│     └── reports.py
│
└── services/
```

---

# 🎨 Frontend Documentation

The frontend is developed using **React**.

It provides a responsive industrial dashboard for monitoring factory operations.

---

## Frontend Modules

### Dashboard

Displays:

- KPI Cards
- Sensor Cards
- Machine Overview
- Live Factory Status

---

### Analytics

Displays:

- Historical Charts
- Health Score
- Machine Selector
- Predictive Maintenance
- Factory Insights

---

### Reports

Displays:

- Summary Tables
- Production Reports
- Export Options

---

### Factory Floor

Displays:

- Interactive Digital Twin
- Machine Cards
- Health Bars
- Live Status
- Analytics Navigation

---

## Frontend Technologies

- React
- React Router
- Axios
- Recharts
- CSS3

---

## React Component Structure

```text
components/

Header.jsx

DashboardCards.jsx

SensorCards.jsx

AnalyticsCards.jsx

TemperatureChart.jsx

PressureChart.jsx

HumidityChart.jsx

VibrationChart.jsx

MachineSelector.jsx

AnalyticsSummary.jsx

MachineCard.jsx

FactoryFloor.jsx

HealthBar.jsx
```

---

# 🗄️ Database Design

The application uses PostgreSQL as the primary database.

---

## Stored Information

Each machine stores:

- Machine Name
- Status
- Temperature
- Pressure
- Humidity
- Vibration
- Timestamp

Historical records are maintained for analytics and reporting.

---

## Database Flow

```text
MQTT

↓

FastAPI

↓

SQLAlchemy

↓

PostgreSQL

↓

REST APIs

↓

React Dashboard
```

---

## Machine Health Calculation

Health score is calculated using sensor values.

Factors considered:

- Temperature
- Pressure
- Humidity
- Vibration

Health ranges:

| Score | Condition |
|--------|-----------|
| 70–100 | Healthy |
| 40–69 | Warning |
| 0–39 | Critical |

---

# 📡 MQTT Workflow

The project simulates Industrial IoT communication using MQTT.

---

## Workflow

```text
Machine Simulator

↓

MQTT Publisher

↓

MQTT Broker

↓

MQTT Subscriber

↓

FastAPI

↓

Database

↓

REST API

↓

React Dashboard
```

---

## Published Sensor Values

The simulator continuously publishes:

- Temperature
- Pressure
- Humidity
- Vibration
- Machine Status

These values are stored inside PostgreSQL for analytics and reporting.

---

# 🌐 API Documentation

The frontend communicates with the backend using REST APIs.

---

## Dashboard APIs

### Get Dashboard Data

```http
GET /dashboard
```

Returns:

- Factory overview
- Production metrics
- Active machines

---

### Get Machine List

```http
GET /machines
```

Returns all available machines.

---

## Analytics APIs

### Analytics Overview

```http
GET /analytics/overview
```

Returns:

- Average Temperature
- Average Pressure
- Average Humidity
- Average Vibration

---

### Machine Health

```http
GET /analytics/machine-health
```

Returns:

- Machine Name
- Status
- Health Score
- Current Sensor Values

---

### Machine History

```http
GET /analytics/history/{machine}
```

Returns historical sensor readings for the selected machine.

---

### Current Machine Data

```http
GET /analytics/machine/{machine}
```

Returns the latest machine information.

---

## Reports APIs

### Reports

```http
GET /reports
```

Returns production reports.

---

### Export Reports

```http
GET /reports/export
```

Returns export-ready report data.

---

# 🔄 Data Flow

```text
Machine Sensors
      │
      ▼
 MQTT Publisher
      │
      ▼
 MQTT Broker
      │
      ▼
 FastAPI Subscriber
      │
      ▼
 PostgreSQL Database
      │
      ▼
 REST APIs
      │
      ▼
 React Frontend
      │
      ▼
 Dashboard
 Analytics
 Reports
 Factory Floor
```

---

## Error Handling

The backend includes:

- API validation
- Exception handling
- Database error handling
- HTTP status codes
- Invalid request validation

The frontend provides:

- Loading indicators
- Error messages
- Empty state handling
- Automatic refresh
- API retry through polling

# 📊 Dashboard Module

The Dashboard serves as the central monitoring interface of the Smart Factory Digital Twin. It provides operators with a real-time overview of factory operations, machine status, and production metrics.

---

## Dashboard Features

### KPI Cards

The dashboard displays key factory metrics through KPI cards, including:

- Total Machines
- Running Machines
- Fault Machines
- Machines Under Maintenance

These cards provide an instant overview of the current factory condition.

---

### Live Sensor Monitoring

The dashboard continuously monitors the following sensor values:

- Temperature (°C)
- Pressure (kPa)
- Humidity (%)
- Vibration (mm/s)

Sensor values are updated automatically every few seconds.

---

### Factory Status

Each machine reports its operational state.

Supported statuses include:

- Running
- Idle
- Maintenance
- Fault

Color-coded indicators make it easy to identify machine conditions at a glance.

---

### Dashboard Objectives

The Dashboard helps operators:

- Monitor factory health
- Detect abnormal machine behavior
- View live production statistics
- Identify machines requiring attention

---

# 📈 Analytics Module

The Analytics module provides detailed insights into machine performance using historical sensor data.

Unlike the Dashboard, which focuses on live monitoring, Analytics emphasizes trends and performance analysis.

---

## Analytics Features

### Machine Selection

Users can choose any machine from the dropdown menu.

Changing the machine updates every chart automatically.

---

### Historical Charts

The Analytics page includes separate charts for:

- Temperature
- Pressure
- Humidity
- Vibration

Charts are generated using Recharts.

---

### Machine Health Score

Each machine receives a calculated health score.

Health is determined using:

- Temperature
- Pressure
- Humidity
- Vibration

Health Categories

| Score | Condition |
|--------|-----------|
| 70–100 | Healthy |
| 40–69 | Warning |
| 0–39 | Critical |

---

### Current Machine Panel

Displays the selected machine along with:

- Machine Name
- Current Status
- Health Score

---

### Analytics Summary

Provides factory-wide averages including:

- Average Temperature
- Average Pressure
- Average Humidity
- Average Vibration

---

### Factory Insights

Displays useful observations such as:

- Hottest machine
- Highest vibration
- Most stable machine
- Average factory health

---

### Predictive Maintenance

Provides maintenance recommendations based on current sensor conditions.

Examples include:

- Schedule inspection
- Replace bearings
- Monitor vibration levels
- Check cooling system

---

### Automatic Refresh

Analytics data refreshes automatically every 5 seconds to ensure current information is displayed.

---

# 📑 Reports Module

The Reports module summarizes production and machine performance into an organized format suitable for review and export.

---

## Reports Features

### Production Summary

Displays overall production statistics including:

- Machine Count
- Running Machines
- Downtime
- Fault Count

---

### Performance Metrics

Provides machine-level performance information such as:

- Average Temperature
- Pressure
- Humidity
- Vibration
- Health Score

---

### Export Support

The reports module supports future export functionality for:

- CSV
- Excel
- PDF

This allows production managers to archive and share operational data.

---

### Report Objectives

The Reports page enables users to:

- Analyze historical performance
- Generate management reports
- Track machine utilization
- Monitor factory efficiency

---

# 🏭 Factory Floor (Digital Twin)

The Factory Floor is the most interactive component of the project.

It provides a visual Digital Twin of the manufacturing environment where each machine is represented as an interactive card.

---

## Factory Floor Features

### Interactive Machine Cards

Each machine is displayed using an individual card.

Every card shows:

- Machine Name
- Machine Status
- Health Score
- Temperature
- Pressure
- Humidity
- Vibration

---

### Machine Health Visualization

Health is displayed using an animated progress bar.

Health colors include:

- Green (Healthy)
- Orange (Warning)
- Red (Critical)

---

### Status Badges

Machines are visually categorized using status badges.

Supported statuses:

- Running
- Idle
- Maintenance
- Fault

Each status uses a unique color for quick identification.

---

### Live Monitoring

The Factory Floor refreshes automatically every 5 seconds.

Updated information includes:

- Temperature
- Pressure
- Humidity
- Vibration
- Health Score
- Machine Status

---

### Fault Detection

Machines in the Fault state display:

- Red status badge
- Highlighted border
- Pulsing animation

This makes critical machines immediately visible.

---

### Factory Header

The page includes:

- Factory title
- Live system indicator
- Last refresh information

---

### Analytics Integration

Clicking a machine card automatically opens the Analytics page.

Example:

```text
/factory-floor
```

↓

```text
/analytics?machine=Robot%20Arm
```

The selected machine is automatically loaded into all analytics charts.

---

### Responsive Design

The Factory Floor adapts to:

- Desktop
- Laptop
- Tablet
- Mobile devices

Cards automatically reorganize into responsive layouts based on screen size.

---

### UI Design Principles

The interface follows modern Industry 4.0 dashboard principles:

- White information cards
- Industrial color palette
- Rounded components
- Responsive grid layout
- Animated status indicators
- Interactive hover effects
- Consistent spacing
- Professional typography

---

# 🔄 Module Integration

The four application modules work together to provide a complete smart factory experience.

```text
Dashboard
     │
     ▼
Factory Overview
     │
     ▼
Analytics
     │
     ▼
Reports
     │
     ▼
Factory Floor Digital Twin
```

Users can seamlessly navigate between modules without losing context, creating an integrated monitoring and analytics workflow.

---

# 🎯 Key Achievements (Days 1–22)

By the end of Day 22, the project includes:

- ✅ Full-stack web application
- ✅ FastAPI backend
- ✅ PostgreSQL database
- ✅ SQLAlchemy ORM
- ✅ MQTT-based sensor simulation
- ✅ Live dashboard
- ✅ Historical analytics
- ✅ Interactive charts
- ✅ Reporting module
- ✅ Digital Twin factory floor
- ✅ Machine health scoring
- ✅ Predictive maintenance insights
- ✅ Responsive industrial UI
- ✅ Automatic data refresh
- ✅ Professional React component architecture

# 📅 Development Timeline (Days 1–22)

The project was developed incrementally, with each day focusing on a specific concept or feature.

| Day | Milestone |
|-----|-----------|
| Day 1 | Project Planning, Architecture Design, GitHub Setup |
| Day 2 | FastAPI Installation and Project Structure |
| Day 3 | PostgreSQL Database Configuration |
| Day 4 | SQLAlchemy Models and Database Connectivity |
| Day 5 | Initial REST API Development |
| Day 6 | Machine Data Models and CRUD Operations |
| Day 7 | MQTT Integration and Sensor Simulation |
| Day 8 | Data Storage and API Testing |
| Day 9 | Dashboard API Development |
| Day 10 | Backend Refinement and Live Data Integration |
| Day 11 | React Project Setup |
| Day 12 | Dashboard UI Components |
| Day 13 | KPI Cards and Sensor Cards |
| Day 14 | API Integration with React |
| Day 15 | Live Dashboard Updates |
| Day 16 | Analytics Module Development |
| Day 17 | Historical Charts using Recharts |
| Day 18 | Reports Module Development |
| Day 19 | Machine Health Calculation |
| Day 20 | Predictive Maintenance and Factory Insights |
| Day 21 | Analytics Improvements and Auto Refresh |
| Day 22 | Interactive Factory Floor Digital Twin |

---

# 🎯 Project Highlights

By Day 22, the Smart Factory Digital Twin includes:

- ✅ Full Stack Architecture
- ✅ RESTful Backend APIs
- ✅ PostgreSQL Database
- ✅ SQLAlchemy ORM
- ✅ MQTT-Based IoT Simulation
- ✅ React Dashboard
- ✅ Analytics Dashboard
- ✅ Historical Sensor Visualization
- ✅ Reports Module
- ✅ Interactive Factory Floor
- ✅ Digital Twin Visualization
- ✅ Machine Health Monitoring
- ✅ Predictive Maintenance
- ✅ Responsive Design
- ✅ Live Data Updates
- ✅ Professional UI Inspired by Industry 4.0 Platforms

---

# 🎓 Learning Outcomes

This project provided hands-on experience with modern full-stack and Industrial IoT technologies.

## Backend

- FastAPI Development
- REST API Design
- SQLAlchemy ORM
- PostgreSQL Integration
- API Routing
- Error Handling
- Data Validation

---

## Frontend

- React Fundamentals
- Component-Based Architecture
- State Management
- React Router
- Axios API Calls
- Responsive Design
- Recharts Integration

---

## Database

- Relational Database Design
- SQL Queries
- Data Persistence
- Historical Data Storage

---

## Industrial IoT

- MQTT Protocol
- Sensor Data Simulation
- Digital Twin Concepts
- Machine Health Monitoring
- Predictive Maintenance

---

## Software Engineering

- Modular Architecture
- Git Version Control
- Debugging
- Documentation
- Full-Stack Integration

---

# 📸 Screenshots

Include screenshots of the following pages:

## Dashboard

- Factory Overview
- KPI Cards
- Live Sensor Monitoring

---

## Analytics

- Temperature Chart
- Pressure Chart
- Humidity Chart
- Vibration Chart
- Health Summary

---

## Reports

- Production Summary
- Machine Performance
- Export View

---

## Factory Floor

- Interactive Machine Cards
- Live Status
- Health Bars
- Fault Animation

---

## Mobile Responsive View

Show the application on:

- Desktop
- Tablet
- Mobile

---

# 🚀 Future Roadmap

The following features are planned for future development.

## Day 23–30

- Machine Search
- Machine Details Drawer
- Better Report Filtering
- Advanced Factory Statistics

---

## Day 31–40

- WebSocket Integration
- Real-Time Notifications
- MQTT Live Streaming
- Alarm System

---

## Day 41–50

- User Authentication
- Role-Based Access Control
- User Management
- Audit Logs

---

## Day 51–60

- Docker Deployment
- Kubernetes Support
- CI/CD Pipeline
- Cloud Deployment
- Dark Mode
- OEE Dashboard
- Energy Consumption Analytics
- AI-Based Failure Prediction

---

# 🤝 Contributing

Contributions are welcome!

To contribute:

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature/new-feature
```

3. Commit your changes.

```bash
git commit -m "feat: add new feature"
```

4. Push the branch.

```bash
git push origin feature/new-feature
```

5. Open a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project in accordance with the license terms.

---

# 👨‍💻 Author

**R Sumukh Aryan**

**Electronics and Communication Engineer**

**Areas of Interest**

- Embedded Systems
- Industrial IoT (IIoT)
- Smart Manufacturing
- Industry 4.0
- Digital Twins
- Full-Stack Development
- Data Analytics

---

# ⭐ Acknowledgements

Special thanks to the open-source community and the developers behind:

- FastAPI
- React
- PostgreSQL
- SQLAlchemy
- MQTT
- Recharts

Their tools and documentation made this project possible.

---

# 🌟 Final Summary

The **Smart Factory Digital Twin Dashboard** is a portfolio-ready Industry 4.0 application that demonstrates the integration of modern web technologies with Industrial IoT concepts.

The project combines:

- Real-time machine monitoring
- Historical analytics
- Predictive maintenance
- Interactive digital twin visualization
- Responsive full-stack web development

Through this project, practical experience was gained in backend development, frontend engineering, database design, API integration, and industrial data visualization, resulting in a comprehensive demonstration of full-stack software engineering skills.
