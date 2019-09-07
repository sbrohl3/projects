## Lecture: Working with Dictionaries Lecture
## IT 410 - Walsh College
## 05/25/2019
## BROHL, STEVEN

pizza_prefs = [{'name':'sandeep', 'toppings':'mushrooms','pizza_type': 'round'},
               {'name':'kylie', 'toppings':['ham', 'pineapple'], 'pizza_type': 'square'},
               {'name':'lisa', 'toppings':['mushrooms','pepperoni'],'pizza_type': 'square'},
               {'name':'dan', 'toppings':['ham','sausage','pepperoni'],'pizza_type': 'square'}]

print(pizza_prefs)

for person in pizza_prefs:

    mushrooms_found = False
    
    if type(person['toppings']) is str:
        if(person['toppings']) == "mushrooms":
            mushrooms_found = True
    elif type(person['toppings']) is list:
        if('mushrooms' in person['toppings']):
            mushrooms_found = True

    if mushrooms_found:
        pizza_prefs.remove(person)

print(pizza_prefs)