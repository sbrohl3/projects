## Try it Yourself Excercises - Chapter 6
## IT 410 - Walsh College
## 05/25/2019
## BROHL, STEVEN


## Try it Yourself 6-1: Person
############################################

person_info = {"first_name": "karl", "last_name": "perpignon", "age": 24, "city":"roseville"}

print("Name: " + person_info["first_name"].title() + " " + person_info["last_name"].title())
print("Age: " + str(person_info["age"]))
print("City: " + person_info["city"].title())


## Try it Yourself 6-7: People
############################################

## Declaring empty list called people
people = []

## Declaring 3 dictionaries with different info
person_info = {"first_name": "karl", "last_name": "perpignon", "age": 24, "city":"roseville"}
people.append(person_info)

person_info = {"first_name": "tyler", "last_name": "prutz", "age": 23, "city":"roseville"}
people.append(person_info)

person_info = {"first_name": "mike", "last_name": "riehl", "age": 25, "city":"clinton township"}
people.append(person_info)

## Looping through the list people and printing everything about each person
for person in people:
    print("\nName: " + person["first_name"].title() + " " + person["last_name"].title())
    print("Age: " + str(person["age"]))
    print("City: " + person["city"].title())

## Try it Yourself 6-8: Pets
############################################

## Declaring an empty list called pets
pets = []

## Declaring 3 dictionaries with different pet info
pet_info = {"animal_type": "bird","name": "blue","age": 15,"owner_name": "tyler"}
pets.append(pet_info)

pet_info = {"animal_type": "dog","name": "kaiser","age": 8,"owner_name": "steven"}
pets.append(pet_info)

pet_info = {"animal_type": "dog","name": "bella","age": 9,"owner_name": "steven"}
pets.append(pet_info)

## Looping through the list pets and printing everything about each pet
for pet in pets:
    print("\nHere is what I know about " + pet["name"].title() + ":")
    for data_type, data in pet.items():
        print(data_type.title() + ": " + str(data).title())

## Try it Yourself 6-9: Favorite Places
############################################

favorite_places = [{"name": "steven","favorite_places": ["landshut","berlin","munich"]},
                  {"name": "karl","favorite_places": ["reykjavik","new york city","nashville"]},
                   {"name": "tyler","favorite_places": ["tokyo","pigeon forge","knoxville"]}]

for items in favorite_places:
    print("\n" + items["name"].title() + "'s favorite places are:") 
    for places in items["favorite_places"]:
        print("- " + places.title())
