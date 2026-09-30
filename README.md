# 🚦 TrafficOps

## Cloud-Native Smart Traffic Management & Incident Response Platform

TrafficOps is a cloud-native traffic management platform designed to collect, process, store, and visualize traffic events in a distributed architecture.

The project combines **Python, FastAPI, RabbitMQ, PostgreSQL, Docker, Kubernetes, Helm, Terraform, Jenkins, Trivy, and Argo CD** to demonstrate a complete DevOps-oriented application architecture.

The current implementation provides a working backend architecture and a Traffic Network Control Center dashboard. Future iterations will extend the platform with **machine learning, AI/agentic AI, real traffic data, predictive traffic analysis, and automated incident response**.

---

## 🏗️ Architecture

```text
                    Traffic Network Control Center
                              Dashboard
                                 │
                                 ▼
                         ┌──────────────┐
                         │   FastAPI    │
                         │     API      │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │   RabbitMQ   │
                         │ Message Bus  │
                         └──────┬───────┘
                                │
                                ▼
                      ┌───────────────────┐
                      │  Event Processor  │
                      │     Service       │
                      └─────────┬─────────┘
                                │
                                ▼
                         ┌──────────────┐
                         │  PostgreSQL  │
                         │   Database   │
                         └──────────────┘


                    Traffic Event Sources
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
          Simulator    Traffic API    IoT / Camera
              │             │             │
              └─────────────┴─────────────┘
                            │
                            ▼
                          FastAPI

------
## 🎯 Project Objectives

TrafficOps is designed to demonstrate how a real-world traffic management platform can be built using modern cloud-native and DevOps practices.

Main objectives
Collect traffic events from multiple sources
Provide a centralized traffic management API
Process events asynchronously
Store processed traffic information
Visualize traffic network conditions
Containerize application components
Prepare the application for Kubernetes deployment
Implement CI/CD automation
Implement infrastructure as code
Add security scanning to the pipeline
Introduce ML-based traffic prediction in future versions
Introduce AI/agentic incident analysis in future versions
-----
## 🚀 Current Features
Backend
FastAPI REST API
Health check endpoint
Traffic event ingestion
RabbitMQ event publishing
Event processor service
PostgreSQL persistence
Sensor simulator
Dockerized services
Dashboard

TrafficOps includes a dedicated Traffic Network Control Center dashboard.

Current dashboard sections include:

Network overview
Pune
Mumbai
Nashik
Lonavala
Traffic network visualization
Route utilization
Traffic distribution
Traffic event explorer
Traffic simulation controls
Platform service status

The dashboard is currently a presentation layer and will be progressively connected to live backend data.
-------
## 🧰 Technology Stack

Application
Technology	Purpose
Python	Backend development
FastAPI	REST API
Uvicorn	ASGI server
Pydantic	Data validation
RabbitMQ	Message broker
PostgreSQL	Persistent database
DevOps
Technology	Purpose
Git	Version control
GitHub	Source code management
Docker	Containerization
Docker Compose	Local multi-container orchestration
Kubernetes	Container orchestration
Helm	Kubernetes package management
Terraform	Infrastructure as Code
Jenkins	CI/CD
Trivy	Container security scanning
Argo CD
