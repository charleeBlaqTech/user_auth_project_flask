from flask import Flask 
from dotenv import load_dotenv
import pymongo
import os

load_dotenv();


app         = Flask(__name__);
app.config['SECRET_KEY'] = os.getenv("SECRET-KEY");
client      = pymongo.MongoClient(os.getenv('MONGO_URI_ATLAS'))
# db          = client.login_system_DB  local database
db          = client.login_system_python_DB


# ROUTES
from user.routes import *


