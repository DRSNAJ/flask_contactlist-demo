# Containerized Contact List

This dynamic web application uses Flask to create a REST API connected to an SQLite database and React for the frontend development. It is fully containerized with Docker and orchestrated using Kubernetes, suitable for robust deployment. The project includes testing with PyTest and a CI/CD pipeline with Jenkins.

### Technologies Used
Docker, Kubernetes, NGINX, Git, Jenkins, PyTest, DockerHub, Postman, Flask, React, Python

## DevOps Project Diagram
Below is a detailed diagram illustrating the architecture and flow of the Contact List DevOps Project:

![diagram-export-05-06-2024-14_25_42](https://github.com/DRSNAJ/flask_contactlist-demo/assets/50520759/f85df8b9-001c-49bf-8d9d-01f2c57db7ad)

1. **GitHub**: The source code for the project is hosted on GitHub.
2. **Git**: Code changes are managed using Git.
3. **Jenkins CI/CD Pipeline**: Jenkins is used to automate the CI/CD pipeline.
4. **DockerHub**: The Docker images for the frontend and backend are stored on DockerHub.
5. **Kubernetes on Minikube**: Kubernetes is used to orchestrate the containers on Minikube for local development.
6. **NGINX with Reverse Proxy**: NGINX acts as a reverse proxy to manage the traffic between the frontend and backend.
7. **React Frontend**: The user interface is developed using React.
8. **Flask Backend**: The backend API is developed using Flask.
9. **SQLite Database**: Data is stored in an SQLite database.

The workflow involves pushing the code to GitHub, where Jenkins picks it up, runs tests, and if successful, builds Docker images and pushes them to DockerHub. Kubernetes pulls these images and deploys them, managing the containerized environment.

This setup ensures a robust and scalable deployment, adhering to best practices in DevOps and software development.
