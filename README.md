# Prometheus-Grafana-Monitoring
# 📊 Monitoring Dockerized Flask App with Prometheus & Grafana

This project sets up real-time monitoring for a Dockerized Flask application using **Prometheus** and **Grafana**. It features custom metrics exposed via a Python exporter and visualized through a Grafana dashboard.

---

## 📦 Stack

- **Flask** (Python) - Web app exposing custom metrics
- **Prometheus** - Metrics collection
- **Grafana** - Metrics visualization
- **Docker Compose** - Easy orchestration

---

## 📁 Project Structure
prometheus-grafana-monitoring/
├── app/
│   ├── app.py
│   ├── exporter.py
│   └── Dockerfile
├── prometheus/
│   └── prometheus.yml
├── grafana/
│   └── provisioning/
│       ├── datasources/
│       │   └── datasource.yml
│       └── dashboards/
│           ├── dashboard.yml
│           └── custom-dashboard.json
├── docker-compose.yml
├── .env
└── README.md
