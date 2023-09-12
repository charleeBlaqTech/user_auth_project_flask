from flask import Flask,redirect, request,session,url_for,render_template
from datetime import datetime, timedelta
import bcrypt
from app import db


class User:

    def start_session(self,user):
        del user['password']
        del user['_id']
        session['logged_in']= True
        session['user']= user
        return user


    def signup(self):

        if bool(db.users.find_one({"email": request.form.get('email').strip()})):
            return render_template('register.html', ERROR="USER WITH THIS EMAIL ALREADY EXIST")
        else:

            if request.form.get('password').strip() == request.form.get('passwordConfirm').strip() and bool(request.form.get('isCreator')):
                byte_password= request.form.get('password').encode("utf-8")
                user_schema= {
                    "fullname": request.form.get('fullname'),
                    "email": request.form.get('email'),
                    "password": bcrypt.hashpw(byte_password, bcrypt.gensalt()),
                    "role": request.form.get('isCreator')
                }
                result= db.users.insert_one(user_schema)
                if bool(result):
                    self.start_session(user_schema)
                    return redirect('/')
            elif request.form.get('password').strip() == request.form.get('passwordConfirm').strip() and not bool(request.form.get('isCreator')):
                byte_password= request.form.get('password').encode("utf-8")
                user_schema= {
                    "fullname": request.form.get('fullname'),
                    "email": request.form.get('email'),
                    "password": bcrypt.hashpw(byte_password, bcrypt.gensalt()),
                    "role": "advertiser"
                }
                result = db.users.insert_one(user_schema)
                if bool(result):
                    self.start_session(user_schema)
                    return redirect('/')
            else:
                return render_template('register.html', ERROR="Password not match")
      
            
    def signin(self):
        if not request.form.get('password').strip() == "" and not request.form.get('useremail').strip()  == "":
            if not bool(db.users.find_one({"email": request.form.get('useremail')})):
                return render_template('login.html', ERROR="USER WITH THIS EMAIL DOES NOT EXIST")
            else:
                result= db.users.find_one({"email":request.form.get('useremail')})
                if bool(result):
                    password= request.form.get('password').strip().encode("utf-8")
                    if bool(bcrypt.checkpw(password, result['password'])):
                        # set session here
                        self.start_session(result)
                        return redirect('/')
                    else:
                        return render_template('login.html', ERROR="password/email not correct or user not exist")
                else:
                    return render_template('login.html', ERROR="password/username not matched")
        else:
            return  render_template('login.html', ERROR="inputs cannot be empty")

    def signout(self):
        session.clear()
        return redirect(url_for('login'))
       
        
