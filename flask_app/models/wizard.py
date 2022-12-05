from flask_app.config.mysqlconnection import connectToMySQL

class Wizard:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.type = data["type"]
        self.power = data["power"]
        self.created_at = data["created_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM wizards;"
        results = connectToMySQL('wizards_db').query_db(query)
        wizards = []
        for wizard in results:
            wizards.append(cls(wizard))
        return wizards

    @classmethod
    def get_one(cls,data):
        # (id) refers to key "id" in server.py, whose value is user input wizard_id
        query = "SELECT * FROM wizards WHERE id = %(id)s;"
        results = connectToMySQL('wizards_db').query_db(query,data)
        return cls(results[0])

    @classmethod
    def create_one(cls,data):
        # (id) refers to key "id" in server.py, whose value is user input wizard_id
        query = "INSERT INTO wizards (Name, Type, Power) VALUES (%(Name)s,%(Type)s,%(Power)s);"
        wizard_id = connectToMySQL('wizards_db').query_db(query,data)
        return wizard_id

    @classmethod
    def update_one(cls,data):
        query = "UPDATE wizards SET name = %(name)s, type = %(type)s, power = %(power)s;, updated_at = NOW() WHERE id = %(id)s"
        wizard_id = connectToMySQL('wizards_db').query_db(query,data)
        return wizard_id

    @classmethod
    def delete_one(cls,data):
        query = "DELETE FROM wizards WHERE id = %(id)s;"
        wizard_id = connectToMySQL('wizards_db').query_db(query,data)
        return wizard_id

    