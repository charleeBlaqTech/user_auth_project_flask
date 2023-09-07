from flask import Flask, redirect, request, render_template, jsonify
from app import app
from user.models import User





@app.route('/', methods=['GET'])
def home():
    return render_template('register.html')



@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/user/register', methods=['POST'])
def register():
    return User().signup()
    # if request.method == "POST":

    #     return make_response('you want to make a post request')
    # else:
    #     return User().signup();