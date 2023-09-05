from flask import Flask , request, render_template, redirect, url_for, jsonify, make_response
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
# import jwt
# from flask_bcrypt import Bcrypt 
# from flask_jwt_extended import JWTManager,


load_dotenv();

app = Flask(__name__);
app.config['SECRET_KEY'] = os.getenv("SECRET-KEY");
# jwt_extd= JWTManager(app)



@app.route('/')
def home():
    # if not session.get('logged_in'):
    #     MESSAGE= "You are not logged in pls do"
    #     return render_template("login.html", MESSAGE);
    return render_template('home.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        # MESSAGE= "You are not logged in pls do"
        # if request.form.get('username') and request.form.get('password') == "12345":
        #     session['logged_in']= True
        #     token = jwt.encode({
        #         'user': request.form.get('username'),
        #         'expiration': str(datetime.utcnow() + timedelta(seconds=120))
        #     }, app.config['SECRET_KEY'])
        #     return jsonify({'token': token.decode('utf-8')})
        #     return render_template("home.html");
        # else:
        #     return redirect(url_for('login'));
        return make_response('you want to make a post request')
    else:
        return render_template('login.html');



@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        # MESSAGE= "You are not logged in pls do"
        # if request.form.get('username') and request.form.get('password') == "12345":
        #     session['logged_in']= True
        #     token = jwt.encode({
        #         'user': request.form.get('username'),
        #         'expiration': str(datetime.utcnow() + timedelta(seconds=120))
        #     }, app.config['SECRET_KEY'])
        #     return jsonify({'token': token.decode('utf-8')})
        #     return render_template("home.html");
        # else:
        #     return redirect(url_for('login'));
        return make_response('you want to make a post request')
    else:
        return render_template('register.html');





if __name__ == "__main__":
    app.run(debug=True) 