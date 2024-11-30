# Microservices Project - Docker & Kubernetes

## Project Overview

This project involves creating and deploying a set of microservices in two stages:

### 1. Dockerized Microservices

Each service (User, Product, Order) was created in separate folders, containerized with Docker, and tested using Docker Compose.

### 2. Kubernetes Deployment

The services were then re-deployed using Kubernetes with **NodePort** services for external access, replacing the initial Docker Compose setup.

### 3. Cleanup

After testing everything, a cleanup script was created to remove all Kubernetes resources (Deployments, Services, PVC).

---

## Folder Structure

├── user-service/ │ ├── Dockerfile │ └── app.py ├── product-service/ │ ├── Dockerfile │ └── app.py ├── order-service/ │ ├── Dockerfile │ └── app.py ├── mongo/ │ ├── docker-compose.yml │ └── mongo-data/ ├── k8s/ │ ├── deployment.yaml │ └── service.yaml └── cleanup.yaml
