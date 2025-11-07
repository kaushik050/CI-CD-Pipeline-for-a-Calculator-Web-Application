# ABSTRACT

## CI/CD Pipeline for Python Calculator Application

This project demonstrates the implementation of a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Python-based calculator web application. The project encompasses the entire software development lifecycle, from application development to automated cloud deployment, showcasing modern DevOps practices and industry-standard tools.

The core application is a Python calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division, and exponentiation) through both a command-line interface and a web-based interface built with Flask. The application is structured using object-oriented principles, with comprehensive unit testing implemented using both Python's unittest framework and pytest, ensuring high code quality and reliability through automated test coverage reporting.

The project implements containerization using Docker, enabling consistent deployment across different environments. A Dockerfile defines the container configuration with security best practices, including non-root user execution and built-in health checks. Docker Compose is utilized for local development, providing an orchestrated environment for running the application, tests, and code quality checks.

The CI/CD pipeline is automated through GitHub Actions and consists of four primary stages: (1) **Testing Stage** - automatically runs code linting with flake8, executes comprehensive unit tests, and generates test coverage reports on every code push; (2) **Build Stage** - builds Docker images using Docker Buildx with multi-platform support and pushes them to Docker Hub registry; (3) **Deployment Stage** - automatically deploys the application to Amazon Web Services (AWS) EC2 instances when code is merged to the main branch, including automated health verification; and (4) **Security Stage** - performs vulnerability scanning using Trivy and integrates with GitHub's security features.

The deployment architecture leverages AWS EC2 for cloud hosting, providing scalability, reliability, and cost-effective infrastructure. The automated deployment process handles container lifecycle management, including stopping old containers, pulling latest images, and performing post-deployment health checks to ensure successful deployments.

Key technologies and tools integrated include Python 3.11, Flask web framework, unittest and pytest for testing, Docker and Docker Compose for containerization, GitHub Actions for CI/CD automation, AWS EC2 for cloud deployment, Trivy for security scanning, and flake8 for code quality enforcement.

This project serves as a comprehensive example of modern software engineering practices, demonstrating how automated pipelines can significantly improve code quality, reduce deployment time, minimize human error, and ensure security standards are maintained throughout the development process. The implementation showcases best practices that are applicable to enterprise-scale applications, making it a valuable learning resource for understanding DevOps principles and modern software deployment methodologies.

---

**Keywords:** CI/CD, DevOps, Python, Docker, GitHub Actions, AWS EC2, Flask, Automated Testing, Containerization, Cloud Deployment, Security Scanning

