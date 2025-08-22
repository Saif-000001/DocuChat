# Backend Dockerfile

# Use slim Python 3.12 image as base (lightweight and stable)
FROM python:3.12.3-slim

# Set working directory inside the container
WORKDIR /app

# Install required system dependencies for common Python packages
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \        
    libsm6 \              
    libxext6 \            
    libxrender-dev \      
    libgl1-mesa-glx \     
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Copy all project files into the container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port (8000 by default)
EXPOSE 8000

# Start FastAPI server using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
