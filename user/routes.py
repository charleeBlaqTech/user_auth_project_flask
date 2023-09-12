from flask import Flask, redirect, request, render_template, url_for, make_response
from app import app
from user.models import User





@app.route('/', methods=['GET'])
def home():
    return render_template('register.html')





@app.route('/user/register', methods=['POST'])
def register():
    data_result= User().signup()
    if data_result == 200:
        return redirect(url_for('login'))
    else:
        return render_template('register.html', ERROR= data_result);




@app.route('/user/login', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        response_result= User().signin()
            
        if response_result['status'] == 200:
            return render_template('home.html', DATA=response_result["user_name"])
        else:
            return render_template('login.html', ERROR=response_result["ERROR_MESSAGE"])

        


