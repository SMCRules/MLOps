# Use official Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH so src/ works
ENV PYTHONPATH=/app

# Default command (run tests for now)
CMD ["pytest", "-q"]
