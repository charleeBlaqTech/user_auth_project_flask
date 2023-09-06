from flask import Flask , request, render_template, redirect, url_for, jsonify, make_response
from dotenv import load_dotenv
import pymongo
import os

# import jwt
# from flask_bcrypt import Bcrypt 
# from flask_jwt_extended import JWTManager,
load_dotenv();


app         = Flask(__name__);
app.config['SECRET_KEY'] = os.getenv("SECRET-KEY");
client      = pymongo.MongoClient('localhost', 27017)
db          = client.login_system_DB

# jwt_extd= JWTManager(app)

# ROUTES
from user.routes import *


