
class Restaurant():
    """A class to represent a restaurant"""
    
    def __init__(self, restaurant_name, cusine_type):
        self.number_served = 0
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " makes the best " + self.cusine_type + "\n")

    def customers_served(self):
        print(self.restaurant_name + " has served " + str(self.number_served) + " customers.\n")

    def open_restaurant(self):
        print(self.restaurant_name + " is open. \n")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served):
        self.number_served += served

