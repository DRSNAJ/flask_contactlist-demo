from flask import Flask     # Importing our framework Flask
from flask_sqlalchemy import SQLAlchemy     # ORM used to interface with our SQL db
from flask_cors import CORS     # This module is used to allow Cross Origin Resource Shariing because we want our database and frontend to live on separate servers 

app = Flask(__name__) # initiating our flask app
CORS(app) # enabling cross origin resource sharing in our app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # linking our app to the location that the database is stored in
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Not tracking modifications on our database
db = SQLAlchemy(app) # initializing a database for our app

