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

```bash

prometheus-grafana-monitoring/
├── app/                #app files
│   ├── app.py
│   ├── exporter.py
│   └── Dockerfile
├── prometheus/         #Prometheus files
│   └── prometheus.yml
├── grafana/            #Grafana files
│   └── provisioning/
│       ├── datasources/
│       │   └── datasource.yml
│       └── dashboards/
│           ├── dashboard.yml
│           └── custom-dashboard.json
├── docker-compose.yml  #Docker files
├── .env
└── README.md
