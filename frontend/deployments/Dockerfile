# Using a base image of Node.js to build our React frontend
FROM node:18 as Build

# Setting the Docker working directory; all following instructions will happen here
WORKDIR /frontend

# Copying the package.json and package-lock.json files into the Docker working directory
COPY package*.json ./ 

# Installing dependencies (this will create the node_modules folder)
RUN npm install 

# Copying everything from the current local directory to the Docker working directory
COPY . .

# Building the React application
RUN npm run build

# Using a base image of Nginx to serve the built React frontend
FROM nginx:stable-alpine

# Exposing port 80 for the Nginx server
EXPOSE 80

# Copying the built files from the build stage to the Nginx default public directory
COPY --from=Build /frontend/build /usr/share/nginx/html

# Copying the Nginx configuration file
COPY default.conf /etc/nginx/conf.d/default.conf

