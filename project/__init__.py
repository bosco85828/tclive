from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from project.routes.tc_api import TcliveResource 
from dotenv import load_dotenv
from datetime import timedelta
import os 




def created_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(TcliveResource,'/domain',)

    return app

