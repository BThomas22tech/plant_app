from plants_app.config.mysqlconnection import connectToMySQL

from flask import flash


class Plants:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.days_to_maturity = data['days_to_maturity']
        self.when_planted = data['when_planted']
        self.date_to_harvest = data['date_to_harvest']
        self.number_of_packets = data['number_of_packets']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']


    @classmethod
    def save(cls, plant_data):
        query = "INSERT INTO plants (name, days_to_maturity,when_planted, date_to_harvest, number_of_packets,created_at, updated_at) VALUES (%(name)s, %(days_to_maturity)s, %(when_planted)s, %(date_to_harvest)s, %(number_of_packets)s, current_timestamp(),current_timestamp());"
        return connectToMySQL('plants_inventory').query_db(query, plant_data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM plants WHERE plants.id = %(id)s";
        return connectToMySQL('plants_inventory').query_db(query, data)
    
    @classmethod
    def get_all_plants(cls):
        query = "select * from plants;"
        results = connectToMySQL('plants_inventory').query_db(query)
        plants = []
        for result in results:
            result = cls(result)
            plants.append(result)
        return plants
    
    @classmethod
    def get_one_plant(cls,data):
        query = "select * from plants where plants.id =%(id)s;"
        results = connectToMySQL('plants_inventory').query_db(query,data)
        print(results)
        results = cls(results[0])
        return results
    
    @classmethod
    def edit_plants(cls, data):
        query = "UPDATE plants SET name = %(name)s, days_to_maturity = %(days_to_maturity)s, when_planted = %(when_planted)s, date_to_harvest = %(date_to_harvest)s, number_of_packets = %(number_of_packets)s,updated_at=current_timestamp() WHERE plants.id = %(id)s";
        return  connectToMySQL('plants_inventory').query_db(query,data)