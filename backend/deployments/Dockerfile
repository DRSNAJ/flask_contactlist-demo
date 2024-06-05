# Defining the base image
FROM python:3.11-slim

# Setting the working directory
WORKDIR /backend

# Copying the requirements file containing all the dependencies relative to the WORKDIR
COPY ./requirements.txt requirements.txt

# Running the install on the dependencies
RUN pip install -r requirements.txt

# Copying our source files
COPY . .

# Exposing the port for our API to be accessed publicly
EXPOSE 5000

# Defining the command to run the application using Gunicorn with the specified configuration
CMD [ "gunicorn", "wsgi:app", "-b 0.0.0.0:5000", "-w 2", "-t 30" ]