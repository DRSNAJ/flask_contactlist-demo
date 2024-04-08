# using a base image of Node to build our React frontend
FROM node:18 as Build

# setting docker working dir all following instructions will happen here
WORKDIR /frontend

# copying the reqiorements file into the docker working directory
COPY ./fontend/package*.json ./ 

# Installing dependencies (adding node modules folder)
RUN npm install 

# copying everything from current local directory to the docker working directory
COPY /fontend .

ENV VITE_REACT_APP_API_URL = http://127.0.0.1:5000

FROM nginx:stable-alpine

COPY --from=Build frontend/build /usr/share/nginx/html

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]

