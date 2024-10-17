# FastAPI LLM Project

This project is a FastAPI application designed to serve as a backend for a language model API. The application is containerized using Docker and uses Gunicorn with Uvicorn workers to handle HTTP requests.

## Project Structure

- `Dockerfile`: Defines the Docker image for the application.
- `requirements.txt`: Lists the Python dependencies required for the application.
- `main.py`: The main entry point for the FastAPI application.

## Dockerfile

The Dockerfile sets up the environment for the FastAPI application:

```dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI app with Gunicorn
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "main:app"]