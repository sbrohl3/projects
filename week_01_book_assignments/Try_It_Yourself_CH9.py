
## 9-10 Imported Restaurant
## 06/30/2019
## Brohl, Steven

from classes.restaurant import Restaurant

restaurant = Restaurant("Steverino's Pizza", "Pizza") 
restaurant.customers_served()

restaurant.set_number_served(50)
restaurant.customers_served()

restaurant.increment_number_served(25)
restaurant.customers_served()




## 9-11 Imported Admin
## 06/30/2019
## Brohl, Steven

from classes.usertype import Admin

admin = Admin("Steven", "Brohl", "1234 Some Street", "sbrohl2@mail.walshcollege.edu", "586-123-4567")
admin.describe_user()
admin.privileges.privileges = ["can add post", "can delete user", "can ban user"]
admin.privileges.show_privileges()




## 9-12 Multiple Modules
## 06/30/2019
## Brohl, Steven

from classes.admin import Admin

admin = Admin("Steven", "Brohl", "1234 Some Street", "sbrohl2@mail.walshcollege.edu", "586-123-4567")
admin.describe_user()
admin.privileges.privileges = ["can add post", "can delete user", "can ban user"]
admin.privileges.show_privileges()




## 9-13 OrderedDict Rewrite
## 07/01/2019
## Brohl, Steven

from collections import OrderedDict
## After many hours on this problem I cannot find a way to use duplicate key names. 
## I had to remove the key names "term" and "definition",
## then I had to place all of my values in a list of tuples in order to get a dictionary I could loop through,
## How can I complete this problem using unique key values?

glossary = OrderedDict([("tuple", "A datatype that holds an ordered collection of values that can be of any type."), ("print", "A function used to display the output of a program."),("while loop", "Permits code to execute repeadetly until a certain condition is met."), ("list", "A datatype that holds an ordered collection of values."), ("integer", "Is positive or negative whole number."), ("function", "A block of code that only runs when it is called."), ("classes", "Represent real-world things and situations."), ("object", "An instance of a class."), ("for loops", "Used for iteracting over a squence."), ("argument", "A value passed to a function or method when calling a function.")])

for key, value in glossary.items():
    print("\n" + key.title() + "- " + value)




## 9-14 Multiple Modules
## 06/30/2019
## Brohl, Steven

from classes.dice import Die

## Rolling a six sided die ten times
rolls = []
num_rolls = 0

while num_rolls < 10:  
    rolls.append(Die().roll_die())
    num_rolls += 1

print("\nResults of rolling a six sided die ten times: ")
print(rolls)


## Rolling a ten sided die ten times
rolls = []
num_rolls = 0

while num_rolls < 10:  
    rolls.append(Die(sides=10).roll_die())
    num_rolls += 1

print("\nResults of rolling a ten sided die ten times: ")
print(rolls)

## Rolling a 20 sided die ten times
rolls = []
num_rolls = 0

while num_rolls < 10:  
    rolls.append(Die(sides=20).roll_die())
    num_rolls += 1

print("\nResults of rolling a twenty sided die ten times: ")
print(rolls)