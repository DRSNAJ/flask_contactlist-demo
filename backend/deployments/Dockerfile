
# Defining the base image
FROM python:3.11-slim

# Setting the working directroty
WORKDIR /backend

# defining the requiremets file containing all the dependencies relative to the WORKDIR
COPY ./requirements.txt requirements.txt

# Running the install on the dependencies 
RUN pip install -r requirements.txt

# copying our source files 
COPY . .

# Exposing the port for our API to be accesses publically 
EXPOSE 5000

CMD [ "gunicorn", "wsgi:app", "-b 0.0.0.0:5000", "-w 2", "-t 30" ]

