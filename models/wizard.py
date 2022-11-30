from full_stack.config.mysqlconnection import connectToMySQL

class Wizard:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.type = data["type"]
        self.power = data["power"]


@classmethod
def get_all(cls):
    query = "SELECT * FROM wizards;"
    results = connectToMySQL('wizards_db').query_db(query)
    wizards = []
    for wizard in results:
        wizards.append(cls(wizard))
    return wizards