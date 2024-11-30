Microservices Project - Docker & Kubernetes
Project Overview

This project involves creating and deploying a set of microservices in two stages:

    Dockerized Microservices:
        Each service (User, Product, Order) was created in separate folders, containerized with Docker, and tested using Docker Compose.

    Kubernetes Deployment:
        The services were then re-deployed using Kubernetes with NodePort services for external access, replacing the initial Docker Compose setup.

    Cleanup:
        After testing everything, a cleanup script was created to remove all Kubernetes resources (Deployments, Services, PVC).
