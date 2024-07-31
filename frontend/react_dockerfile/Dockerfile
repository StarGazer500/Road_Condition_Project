FROM node:14 AS build
# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json into the container
COPY ./package*.json /app/

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . /app/

# Build the React application
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy built files from the previous stage
COPY --from=build /app/build /usr/share/nginx/html

# Copy Nginx configuration file
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Command to run Nginx
CMD ["nginx", "-g", "daemon off;"]



