from flask import Flask     # Importing our framework Flask
from models import db
from flask_cors import CORS     # This module is used to allow Cross Origin Resource Shariing because we want our database and frontend to live on separate servers 

class ConfigApp:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # linking our app to the location that the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Not tracking modifications on our database
    
class TestConfig(ConfigApp):    
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    
def createApp(app_config = ConfigApp):
    app = Flask(__name__) # initiating our flask app
    CORS(app) # enabling cross origin resource sharing in our app
    app.config.from_object(app_config)
    db.init_app(app)
    
    return app, db
