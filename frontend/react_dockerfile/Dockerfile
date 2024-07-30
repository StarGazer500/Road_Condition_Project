# Use the official Ubuntu base image
FROM ubuntu:24.04


# Set the working directory
WORKDIR /app


# Install Node.js and npm
RUN apt update && apt install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt install -y nodejs && \
    apt autoremove -y && \
    apt clean


# Copy the package.json and package-lock.json into the container
COPY ./package*.json /app/

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . /app/

# Build the React application
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

