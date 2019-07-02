
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
## FIXED IT!

glossary = OrderedDict()

glossary["tuple"] = "A datatype that holds an ordered collection of values that can be of any type."
glossary["print"] = "A function used to display the output of a program."
glossary["while loop"] = "Permits code to execute repeadetly until a certain condition is met."
glossary["list"] = "A datatype that holds an ordered collection of values."
glossary["integer"] = "Is positive or negative whole number."
glossary["function"] = "A block of code that only runs when it is called."
glossary["classes"] = "Represent real-world things and situations."
glossary["object"] = "An instance of a class."
glossary["for loops"] = "Used for iteracting over a squence."
glossary["argument"] = "A value passed to a function or method when calling a function."

for key, value in glossary.items():
    print("\n" + key.title() + " - " + value)




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