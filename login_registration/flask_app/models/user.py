from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    schema = 'login_registration_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    @classmethod
    def save_user(cls, data):
        query = "INSERT into users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(cls.schema).query_db(query,data)

    @classmethod
    def get_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.schema).query_db(query, data)
        if results:
            return results[0]
        return False

    @classmethod
    def get_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(cls.schema).query_db(query, data)
        if results:
            return results[0]
        return False
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users "
        results = connectToMySQL(cls.schema).query_db(query)
        users = []
        if results:
            for row in users:
                users.append( cls(row) )
        return users

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(cls.schema).query_db(query,data)

    @staticmethod
    def validate_register(user):
        is_valid = True
        user_in_db = User.get_email(user)
        if user_in_db:
            flash("Email is already been taken","userEmail")
            is_valid =  False
        if len(user['first_name']) < 3:
            is_valid = False
            flash("First Name must be at least 3 characters.","userFirst")
        if len(user['last_name']) < 3:
            is_valid = False
            flash("Last Name must be at least 3 characters.", "userLast")
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.","userPass")
        if user['password'] != user['confirm_password']:
            flash("Password must match!","userConfirmPass")
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.")
        if not EMAIL_REGEX.match(user['email']): 
            flash("Email is not correct!")
            is_valid = False
        return is_valid