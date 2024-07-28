# Use the official Ubuntu base image
FROM ubuntu:24.04

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update and install necessary packages
RUN apt update && apt upgrade -y && \
    apt install -y python3 python3-venv python3-pip gdal-bin python3-gdal && \
    apt autoremove -y && \
    apt clean

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY backend/requirements.txt /app/

# Install Python packages specified in requirements.txt
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY backend /app/

# Copy and set the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
