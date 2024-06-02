from flask_app.config.mysqlconnection import connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash,request
from flask_app.models.user import User


class Recipe:
    db_name = 'recipes_users'
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.date=data['date']
        self.time_takes=data['time_takes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    @classmethod
    def create(cls, data):
        query = '''
        INSERT INTO recipes (name, description, instructions, date, time_takes, user_id) 
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(time_takes)s, %(user_id)s);
        '''
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def getAllRecipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db_name).query_db(query)
        recipes = []
        if results:
            for recipe in results:
                recipes.append(recipe)
        return recipes

    @classmethod
    def get_recipe_by_id(cls, recipe_id):
        query = "SELECT * FROM recipes WHERE id = %(recipe_id)s;"
        data = {
            'recipe_id': recipe_id
            }
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if results:
            return results[0]
        return False

    
    
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id= %(recipe_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes set name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, time_takes = %(time_takes)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_users_recipe(cls, data):
        query = "delete from recipes where recipes.user_id = %(user_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    



    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Recipe name should be at least 3 characters!", 'name')
            is_valid = False
        if not data['description']:
            flash("Write something in the description!", 'recipeDes')
            is_valid = False
        if len(data['instructions']) < 1:
            flash("You need to give instructions", 'recipeIns')
            is_valid = False
        if len(data['date']) < 3:
            flash("Pick a date", 'recipeDate')
            is_valid = False
        if 'time_takes' not in data or data['time_takes'] not in ['Yes', 'No']:
            flash("Pick an option for the time", 'recipeTime')
            is_valid = False
        return is_valid
    