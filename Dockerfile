# Use Python base image
FROM python:3.8-slim

# Install dependencies for PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Flask app
CMD ["python", "app.py"]
