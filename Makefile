# Makefile for Calculator CI/CD Project

.PHONY: help install test test-coverage lint docker-build docker-run docker-test clean

# Default target
help:
	@echo "Available commands:"
	@echo "  install       - Install dependencies"
	@echo "  test          - Run unit tests"
	@echo "  test-coverage - Run tests with coverage"
	@echo "  lint          - Run code linting"
	@echo "  docker-build  - Build Docker image"
	@echo "  docker-run    - Run Docker container"
	@echo "  docker-test   - Run tests in Docker"
	@echo "  clean         - Clean up temporary files"

# Install dependencies
install:
	pip install -r requirements.txt

# Run unit tests
test:
	python -m unittest test_calculator.py -v
	pytest test_calculator.py -v

# Run tests with coverage
test-coverage:
	pytest test_calculator.py --cov=calculator --cov-report=html --cov-report=xml -v

# Run linting
lint:
	flake8 calculator.py test_calculator.py --max-line-length=100 --ignore=E203,W503

# Build Docker image
docker-build:
	docker build -t calculator-app .

# Run Docker container
docker-run:
	docker run -p 8000:8000 calculator-app

# Run tests in Docker
docker-test:
	docker run calculator-app python -m pytest test_calculator.py -v

# Clean up temporary files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf .pytest_cache/
	rm -rf .tox/
	rm -rf dist/
	rm -rf build/



