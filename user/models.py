from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import bcrypt
from app import db


class User:

    def signup(self):

        if bool(db.users.find_one({"email": request.form.get('email')})):
            return "USER WITH THIS EMAIL ALREADY EXIST"
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
                     return 200
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
                    return 200
            else:
                return "Password not match"
      
            
    def signin(self):
        if not request.form.get('password').strip() == "" and not request.form.get('useremail').strip()  == "":
            if not bool(db.users.find_one({"email": request.form.get('useremail')})):
                return {
                            'ERROR_MESSAGE': "USER WITH THIS EMAIL DOES NOT EXIST", 
                            "status": 400
                        }
            else:
                result= db.users.find_one({"email":request.form.get('useremail')})
                if bool(result):
                    password= request.form.get('password').strip().encode("utf-8")
                    if bool(bcrypt.checkpw(password, result['password'])):
                        return {
                            'user_name': result['fullname'], 
                            "status": 200
                        }
                    else:
                        return {
                            'ERROR_MESSAGE': "password/email not correct or user not exist", 
                            "status": 400
                        }
                else:
                    return {
                            'ERROR_MESSAGE': "password/username not matched", 
                            "status": 400
                        }
        else:
            return  {
                        'ERROR_MESSAGE': "inputs cannot be empty", 
                        "status": 400
                    }


       
        
