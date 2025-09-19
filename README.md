# aws-ecs-api-demo

Overview

This repository provides a lightweight AWS reference architecture that demonstrates service-to-service communication using ECS Fargate containers backed by a PostgreSQL database.


The deployment consists of:

Service A → A containerized API that returns a string to the client.

Service B → A containerized API that retrieves the string from the database.

PostgreSQL (RDS) → Seeded with the classic "hello world" message.

Automation scripts → Build, push, and deploy to AWS with minimal effort.

Architecture Flow

A client sends a request to Service A (via an Application Load Balancer).

Service A calls Service B.

Service B queries the Postgres database.

The database returns the string "hello world", which flows back to the client.


Features

🐳 Containerized APIs with Docker

☁️ AWS ECS Fargate deployment

🗄️ RDS Postgres with seeded data

⚡ Infrastructure-as-Code (CloudFormation / Terraform options)

🛠️ Automation scripts for builds, pushes, and seeding


Use Cases

Learn how services communicate within a VPC private subnet.

Demonstrate container-to-database integration in AWS.

Provide a starting point for observability, monitoring, and scaling experiments.
