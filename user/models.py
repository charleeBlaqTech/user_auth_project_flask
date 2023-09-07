from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from app import db

class User:

    def signup(self):

        if bool(db.users.find_one({"email": request.form.get('email')})):
            return "USER WITH THIS EMAIL ALREADY EXIST"
        else:

            if request.form.get('password') == request.form.get('passwordConfirm') and bool(request.form.get('isCreator')):
                user_schema= {
                    "fullname": request.form.get('fullname'),
                    "email": request.form.get('email'),
                    "password": request.form.get('password'),
                    "role": request.form.get('isCreator')
                }
                result= db.users.insert_one(user_schema)
                if bool(result):
                     return 200
            elif request.form.get('password') == request.form.get('passwordConfirm') and not bool(request.form.get('isCreator')):
                user_schema= {
                    "fullname": request.form.get('fullname'),
                    "email": request.form.get('email'),
                    "password": request.form.get('password'),
                    "role": "advertiser"
                }
                result = db.users.insert_one(user_schema)
                if bool(result):
                    return 200
            else:
                return "Password not match"
            
    def signin(self):
        if bool(request.form.get('password')) and bool(request.form.get('useremail')):
            if not bool(db.users.find_one({"email": request.form.get('useremail')})):
                return "USER WITH THIS EMAIL DOES NOT EXIST"
            else:
                result= db.users.find_one({"email":request.form.get('useremail')})
                if bool(result):
                    return result
        else:
            return "inputs cannot be empty"


       
        
