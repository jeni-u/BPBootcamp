
from flask_app.config.mysqlconnection import MySQLConnection
from .ninja import Ninja

class Dojo:
    db = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = MySQLConnection(cls.db).query_db(query)
        dojos = []
        for row in results:
            dojos.append( cls(row) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return MySQLConnection(cls.db).query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results = MySQLConnection(cls.db).query_db(query, data)
        dojo = cls(results[0])
        for i in results:
            row = {
                'id': i['ninjas.id'],
                'first_name': i['first_name'],
                'last_name': i['last_name'],
                'age': i['age'],
                'created_at': i['ninjas.created_at'],
                'updated_at': i['ninjas.updated_at'],
            }
            dojo.ninjas.append( Ninja(row))
        return dojo
