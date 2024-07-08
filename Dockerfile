# Use Python 3.8 slim version as base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000", "--debug"]
