from flask import Flask



app = Flask(__name__)
#All Of The Projects
from app import mainRoutes
from app.routes import jokesAPI