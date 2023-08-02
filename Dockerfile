# Use an official Python runtime as a parent image
FROM python:3.11.4 as base

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory files (i.e., the app) to the Docker container at /app
ADD . /app

# Install system dependencies
RUN apt-get update && xargs -a packages.txt apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV NAME membership-report

# Light version
FROM base as light

# Change requirements.txt to remove the heavy dependencies for the light version
COPY requirements-light.txt ./requirements.txt

# Install any needed packages specified in requirements-light.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py when the container launches
ENTRYPOINT ["python", "main.py"]

# Full version
FROM base as full

# Run main.py when the container launches
ENTRYPOINT ["python", "main.py"]
