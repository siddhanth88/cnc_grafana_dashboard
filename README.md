# cnc_grafana_dashboard
🚀 Features

1. 📊 Real-time dashboards for multiple CNC machines (spindle speed, power state).
    - Pointer: Enables live monitoring of CNC machine metrics.

2. 🗄️ PostgreSQL backend for structured logging of CNC data.
    - Pointer: Stores CNC data efficiently for analysis and reporting.

3. 🐳 Dockerized setup for reproducible deployment.
    - Pointer: Simplifies installation and ensures consistent environments.

4. 🔔 Extensible for anomaly detection & alerting (future upgrade).
    - Pointer: Designed for future integration of smart alerts.

5. 🎨 Custom Grafana dashboards with thresholds and machine-wise views.
    - Pointer: Visualizes data with tailored dashboards per machine.


🏗️ Tech Stack

- Backend: Python, PostgreSQL
  - Pointer: Handles data ingestion and storage.

- Visualization: Grafana
  - Pointer: Provides interactive dashboards.

- Deployment: Docker, Docker Compose
  - Pointer: Manages application containers and orchestration.

- Data Source: MTConnect streams (demo + configurable)

  - Pointer: Supplies CNC machine data via standard protocol.
