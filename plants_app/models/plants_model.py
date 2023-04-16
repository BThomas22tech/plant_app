from plants_app.config.mysqlconnection import connectToMySQL

from flask import flash


class Plants:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.days_to_maturity = data['days_to_maturity']
        self.when_planted = data['when_planted']
        self.date_to_harvest = None
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']


# @classmethod
#     def save(cls, data):
#         query = "INSERT INTO plants (name, email,password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, now(),now());"
#         return connectToMySQL('dragrace').query_db(query, data)


    @classmethod
    def get_all_plants(cls):
        query = "select * from plants;"
        results = connectToMySQL('plants_inventory').query_db(query)
        plants = []
        for result in results:
            result = cls(results[0])
            plants.append(result)
        print(plants)
        return plants
