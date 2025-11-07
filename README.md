# CI/CD Pipeline for Python Calculator Application

A simple Python calculator application with a complete CI/CD pipeline using GitHub Actions, Docker, and AWS EC2 deployment.

## 🧮 Features

- **Basic Arithmetic Operations**: Add, subtract, multiply, divide, and power
- **Comprehensive Testing**: Unit tests with both unittest and pytest
- **Docker Containerization**: Ready for deployment
- **CI/CD Pipeline**: Automated testing, building, and deployment
- **Security Scanning**: Vulnerability scanning with Trivy
- **Code Quality**: Linting with flake8

## 📁 Project Structure

```
├── calculator.py              # Main calculator application
├── test_calculator.py         # Comprehensive unit tests
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker container configuration
├── docker-compose.yml         # Local development setup
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions CI/CD pipeline
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd cicd-pipeline-python-calculator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the calculator**
   ```bash
   python calculator.py
   ```

4. **Run tests**
   ```bash
   # Using unittest
   python -m unittest test_calculator.py -v
   
   # Using pytest
   pytest test_calculator.py -v
   
   # With coverage
   pytest test_calculator.py --cov=calculator --cov-report=html
   ```

### Docker Development

1. **Build and run with Docker Compose**
   ```bash
   # Run the application
   docker-compose up calculator-app
   
   # Run tests
   docker-compose up calculator-test
   
   # Run linting
   docker-compose up calculator-lint
   ```

2. **Build Docker image manually**
   ```bash
   docker build -t calculator-app .
   docker run -p 8001:8000 calculator-app
   ```

## 🔧 CI/CD Pipeline

The pipeline includes the following stages:

### 1. **Test Stage**
- **Python Setup**: Uses Python 3.11
- **Dependency Caching**: Caches pip dependencies for faster builds
- **Linting**: Code quality checks with flake8
- **Unit Tests**: Runs both unittest and pytest
- **Coverage**: Generates coverage reports
- **Artifacts**: Uploads test results and coverage reports

### 2. **Build Stage**
- **Docker Build**: Builds Docker image using Buildx
- **Multi-platform**: Supports multiple architectures
- **Caching**: Uses GitHub Actions cache for faster builds
- **Registry**: Pushes to Docker Hub

### 3. **Deploy Stage** (Main branch only)
- **AWS Integration**: Uses AWS credentials
- **EC2 Deployment**: Deploys to EC2 instance
- **Health Checks**: Verifies deployment success
- **Rollback**: Automatic cleanup of old containers

### 4. **Security Stage**
- **Vulnerability Scanning**: Uses Trivy scanner
- **SARIF Reports**: Uploads security scan results
- **CodeQL Integration**: Integrates with GitHub security features

## 🔐 Required Secrets

Configure these secrets in your GitHub repository:

### Docker Hub
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password/token

### AWS
- `AWS_ACCESS_KEY_ID`: AWS access key
- `AWS_SECRET_ACCESS_KEY`: AWS secret key

### EC2
- `EC2_USER`: EC2 instance username (e.g., `ubuntu`, `ec2-user`)
- `EC2_HOST`: EC2 instance public IP or hostname

## 📊 Testing

### Test Coverage

The application includes comprehensive tests covering:

- ✅ **Positive numbers**: All operations with positive integers and decimals
- ✅ **Negative numbers**: All operations with negative values
- ✅ **Edge cases**: Zero, large numbers, decimal precision
- ✅ **Error handling**: Division by zero, invalid inputs
- ✅ **Power operations**: Exponentiation with various inputs

### Running Tests

```bash
# All tests
pytest test_calculator.py -v

# With coverage
pytest test_calculator.py --cov=calculator --cov-report=html

# Specific test class
pytest test_calculator.py::TestCalculator -v

# Specific test method
pytest test_calculator.py::TestCalculator::test_add_positive_numbers -v
```

## 🐳 Docker Commands

```bash
# Build image
docker build -t calculator-app .

# Run container
docker run -p 8000:8000 calculator-app

# Run tests in container
docker run calculator-app python -m pytest test_calculator.py -v

# Interactive shell
docker run -it calculator-app /bin/bash

# View logs
docker logs calculator-app
```

## 🚀 Deployment

### Manual Deployment to EC2

1. **Prepare EC2 instance**
   ```bash
   # Install Docker
   sudo yum update -y
   sudo yum install -y docker
   sudo systemctl start docker
   sudo systemctl enable docker
   sudo usermod -a -G docker ec2-user
   ```

2. **Deploy application**
   ```bash
   # Pull and run
   docker pull your-username/calculator-app:latest
   docker run -d --name calculator-app -p 8000:8000 your-username/calculator-app:latest
   ```

3. **Verify deployment**
   ```bash
   curl http://your-ec2-ip:8000/health
   ```

### Automated Deployment

The CI/CD pipeline automatically deploys to EC2 when:
- Code is pushed to the `main` branch
- All tests pass
- Docker image is built successfully
- Security scan passes

## 📈 Monitoring and Logs

### Health Checks

The application includes health checks:
- **Docker Health Check**: Built into the Dockerfile
- **Application Health**: Python-based health verification
- **Deployment Health**: Post-deployment verification

### Logging

```bash
# View application logs
docker logs calculator-app

# Follow logs in real-time
docker logs -f calculator-app

# View specific log entries
docker logs --since 1h calculator-app
```

## 🔧 Configuration

### Environment Variables

- `PYTHONPATH`: Python module path
- `PYTHONUNBUFFERED`: Disable Python output buffering
- `AWS_REGION`: AWS region for deployment

### Customization

- **Port**: Change port mapping in docker-compose.yml
- **Dependencies**: Add packages to requirements.txt
- **Tests**: Add new test cases to test_calculator.py
- **Pipeline**: Modify .github/workflows/ci-cd.yml

## 🐛 Troubleshooting

### Common Issues

1. **Tests failing**
   ```bash
   # Check Python version
   python --version
   
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

2. **Docker build failing**
   ```bash
   # Check Docker daemon
   docker --version
   
   # Clean Docker cache
   docker system prune -a
   ```

3. **Deployment issues**
   ```bash
   # Check EC2 connectivity
   ssh -i your-key.pem ec2-user@your-ec2-ip
   
   # Check Docker on EC2
   docker ps
   ```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Support

For issues and questions:
- Create an issue in the GitHub repository
- Check the troubleshooting section
- Review the CI/CD pipeline logs

---

**Happy Calculating! 🧮✨**



