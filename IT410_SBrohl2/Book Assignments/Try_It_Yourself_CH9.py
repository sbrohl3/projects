## Try it Yourself Excercises - Chapter 9
## IT 410 - Walsh College
## 06/10/2019
## BROHL, STEVEN


## Try it Yourself 9-1: Restaurant
############################################

class Restaurant():
    """A class to represent a restaurant"""
    
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " makes the best " + self.cusine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

restaurant = Restaurant("Steverino's Pizza", "Pizza") 
print(restaurant.restaurant_name)
print(restaurant.cusine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
    

## Try it Yourself 9-2: Three Restaurants
############################################

class Restaurant():
    """A class to represent a restaurant"""
    
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " makes the best " + self.cusine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

restaurant = Restaurant("Steverino's Pizza", "Pizza")
restaurant.describe_restaurant()
restaurant1 = Restaurant("Mr. Paul's Chop House", "Prime Rib")
restaurant1.describe_restaurant() 
restaurant2 = Restaurant("Johnny Nood King's", "Ramen Noodles") 
restaurant2.describe_restaurant()
restaurant3 = Restaurant("Ima's", "Udon Noodles")  
restaurant3.describe_restaurant()

## Try it Yourself 9-3: Users
############################################

class User():
    """A class to represent a user"""

    def __init__(self, first_name, last_name, address, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone = phone

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name + "\t" + self.address + "\t" + self.email + "\t" + self.phone)

    def greet_user(self):
        print("Hello " + self.first_name.title() + ", welcome to the program!")

user = User("Steven", "Brohl", "1234 Some Street", "sbrohl2@mail.walshcollege.edu", "586-123-4567")
user.describe_user()
user.greet_user()
user1 = User("Bill", "Gates", "1985 Redmond Ln.", "bgates@microsoft.com", "888-321-3425")
user1.describe_user()
user1.greet_user()
user2 = User("Linus", "Torvalds", "443 IEEE St.", "ltorvalds@linux.com", "818-432-4451")
user2.describe_user()
user2.greet_user()
user3 = User("Steve", "Jobs", "3389 Apple Ave.", "sjobs@apple.com", "823-445-3389")
user3.describe_user()
user3.greet_user()



## Try it Yourself 9-4: Number Served
############################################

class Restaurant():
    """A class to represent a restaurant"""
    
    def __init__(self, restaurant_name, cusine_type):
        self.number_served = 0
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " makes the best " + self.cusine_type)

    def customers_served(self):
        print(self.restaurant_name + " has served " + str(self.number_served) + " customers.")

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served):
        self.number_served += served

restaurant = Restaurant("Steverino's Pizza", "Pizza") 
restaurant.customers_served()

restaurant.set_number_served(50)
restaurant.customers_served()

restaurant.increment_number_served(25)
restaurant.customers_served()

## Try it Yourself 9-5: Login Attempts
############################################

class User():
    """A class to represent a user"""

    def __init__(self, first_name, last_name, address, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone = phone
        self.login_attempt = 0

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name + "\t" + self.address + "\t" + self.email + "\t" + self.phone)

    def greet_user(self):
        print("Hello " + self.first_name.title() + ", welcome to the program!")

    def increment_login_attempts(self):
        self.login_attempt += 1
    
    def reset_login_attempts(self):
        self.login_attempt = 0
    

user = User("Steven", "Brohl", "1234 Some Street", "sbrohl2@mail.walshcollege.edu", "586-123-4567")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempt)
user.reset_login_attempts()
print(user.login_attempt)

## Try it Yourself 9-6: Ice Cream Stands
############################################

class Restaurant():
    """A class to represent a restaurant"""
    
    def __init__(self, restaurant_name, cusine_type):
        self.number_served = 10
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " makes the best " + self.cusine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open.")

    def customers_served(self):
        print(self.restaurant_name + " has served " + str(self.number_served) + " customers.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served):
        self.number_served += served

class IceCreamStand(Restaurant):
    """A class to represent an IceCream Stand"""
    
    def __init__(self, restaurant_name, cusine_type):
        super().__init__(restaurant_name, cusine_type)
        self.flavors = []

    def display_flavors(self):
            print(self.restaurant_name + " serves these flavors:") 
            for flavor in self.flavors:
                print(flavor.title())

IceCreamStand = IceCreamStand("Steve's Ice cream", "Ice cream")
IceCreamStand.describe_restaurant()
IceCreamStand.flavors = ["chocolate" , "vanilla" , "strawberry", "superman"]
IceCreamStand.display_flavors()


## Try it Yourself 9-7: Admin
###########################################

class User():
    """A class to represent a user"""

    def __init__(self, first_name, last_name, address, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone = phone
        self.login_attempt = 0

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name + "\t" + self.address + "\t" + self.email + "\t" + self.phone)

    def greet_user(self):
        print("Hello " + self.first_name.title() + ", welcome to the program!")

    def increment_login_attempts(self):
        self.login_attempt += 1
    
    def reset_login_attempts(self):
        self.login_attempt = 0

class Admin(User):
    """A class to represent an Admin"""

    def __init__(self, first_name, last_name, address, email, phone):
        super().__init__(first_name, last_name, address, email, phone)
        privileges = []

    def show_privileges(self):
        print("User privileges: ")
        for privilege in self.privileges:
            print(privilege.title())

admin = Admin("Steven", "Brohl", "1234 Some Street", "sbrohl2@mail.walshcollege.edu", "586-123-4567")
admin.describe_user()
admin.privileges = ["can add post", "can delete user", "can ban user"]
admin.show_privileges()


## Try it Yourself 9-8: Privileges
############################################

class User():
    """A class to represent a user"""

    def __init__(self, first_name, last_name, address, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone = phone
        self.login_attempt = 0

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name + "\t" + self.address + "\t" + self.email + "\t" + self.phone)

    def greet_user(self):
        print("Hello " + self.first_name.title() + ", welcome to the program!")

    def increment_login_attempts(self):
        self.login_attempt += 1
    
    def reset_login_attempts(self):
        self.login_attempt = 0

class Admin(User):
    """A class to represent an Admin"""

    def __init__(self, first_name, last_name, address, email, phone):
        super().__init__(first_name, last_name, address, email, phone)
        self.privileges = Privileges()

class Privileges():
    """A simple class to store privileges"""

    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("User privileges: ")
        for privilege in self.privileges:
            print(privilege.title())

admin = Admin("Steven", "Brohl", "1234 Some Street", "sbrohl2@mail.walshcollege.edu", "586-123-4567")
admin.describe_user()
admin.privileges.privileges = ["can add post", "can delete user", "can ban user"]
admin.privileges.show_privileges()

## Try it Yourself 9-9: Battery Upgrade
############################################

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Checks the battery size and sets capacity to 85"""
        if self.battery_size < 85:
            self.battery_size = 85


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

 
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()