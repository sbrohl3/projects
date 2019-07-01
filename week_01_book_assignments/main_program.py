## 8-15 Printing Functions Models
## 06/30/2019
## Brohl, Steven

import functions.printing_functions as print_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_functions.print_models(unprinted_designs, completed_models)
print_functions.show_completed_models(completed_models)




## 8-16 Imports
## 06/30/2019
## Brohl Steven

import functions.show_magicians as show_magicians

## List of Magicians
magicians = ["Merlin", "Houdini", "Blaine", "Angel"]

show_magicians.show_magicians(magicians)




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
## 06/30/2019
## Brohl, Steven

from collections import OrderedDict



glossary_list = ("term": "tuple", "definition": "A datatype that holds an ordered collection of values that can be of any type."),("term": "print", "definition": "A function used to display the output of a program."),("term": "while loop", "definition": "Permits code to execute repeadetly until a certain condition is met."),("term": "list", "definition": "A datatype that holds an ordered collection of values."),("term": "integer", "definition": "Is positive or negative whole number."),("term": "function", "definition": "A block of code that only runs when it is called."),("term": "classes", "definition": "Represent real-world things and situations."),("term": "object", "definition": "An instance of a class."),("term": "for loops","definition": "Used for iteracting over a squence."),("term": "argument", "definition": "A value passed to a function or method when calling a function.")

glossary = OrderedDict(glossary_list)
print(glossary)





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