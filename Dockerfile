# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN apt-get update -y && apt-get install -y \
  build-essential \
  libssl-dev zlib1g-dev \
  libbz2-dev \
  libreadline-dev \
  default-libmysqlclient-dev \
  pkg-config \
  wget \
  curl \
  git

# Copy the requirements file into the container
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose the port the FastAPI app will run on
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
