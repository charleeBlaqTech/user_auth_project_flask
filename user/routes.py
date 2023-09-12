from flask import Flask, redirect, request, render_template, url_for, session
from functools import wraps
from app import app, db
from user.models import User



def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper



@app.route('/', methods=['GET'])
@login_required
def home():
    return render_template('home.html')




@app.route('/user/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        return User().signup()
    else:
        return render_template('register.html')




@app.route('/user/login', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        return User().signin()



@app.route('/logout', methods=['GET'])
@login_required
def logout():
        return User().signout()
