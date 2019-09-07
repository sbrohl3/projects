## Try it Yourself Excercises - Chapter 3
## IT 410 - Walsh College
## 05/13/2019
## BROHL, STEVEN


## Try it Yourself 3-1: Names
############################################
names = ["Karl","Tyler","Jeremy","Ryan"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print("\n")

## Try it Yourself 3-2: Greetings
############################################
names = ["Karl","Tyler","Jeremy","Ryan"]
print("Hello " + names[0].title() + ", welcome to the program!")
print("Hello " + names[1].title() + ", welcome to the program!")
print("Hello " + names[2].title() + ", welcome to the program!")
print("Hello " + names[3].title() + ", welcome to the program!")
print("\n")

## Try it Yourself 3-3: Your own list
############################################
fav_transport = ["car","bike","boat","motorcycle"]
print("I will never own a Harley Davidson", fav_transport[3] + ".")  
print("My favorite ",fav_transport[0], "is the Pontiac G8" + ".")
print("One day I will have my own ",fav_transport[2],"and I will sail the ocean!")
print("I love riding my mountain", fav_transport[1],"when the weather is nice!\n") 

## Try it Yourself 3-4: Guest List
############################################

guests = ["Philip K. Dick","H.P. Lovecraft","William Gibson"]
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[1].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.\n")


## Try it Yourself 3-5: Changing Guest List
############################################

## Creating a list of guests and printing to screen their invites
guests = ["Philip K. Dick","H.P. Lovecraft","William Gibson"]
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[1].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.\n")

## Printing to screen those guests that cannot make it
print("I'm afraid ",guests[0]," cannot make it to dinner.")
print("I'm afraid ",guests[2]," cannot make it to dinner.\n")

## Deleting and replacing guests that cannot make it
del(guests[0])
guests.insert(0, "Bruce Sterling")
del(guests[2])
guests.insert(2, "Richard Morgan")

## Printing to screen new invites for guests that can make it
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.\n")


## Try it Yourself 3-6: More Guests
############################################

## Creating a list of guests and printing to screen their invites
guests = ["Philip K. Dick","H.P. Lovecraft","William Gibson"]
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[1].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.\n")

## Printing to screen those guests that cannot make it
print("I'm afraid ",guests[0]," cannot make it to dinner.")
print("I'm afraid ",guests[2]," cannot make it to dinner.\n")

## Deleting and replacing guests that cannot make it
del(guests[0])
guests.insert(0, "Bruce Sterling")
del(guests[2])
guests.insert(2, "Richard Morgan")

## Printing to screen new invites for guests that can make it
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.\n")

## Informing guests we have new dinner table
print("Attention all guests: We are getting a bigger dinner table\n")

## Adding new guests with "insert" and "append" attributes
guests.insert(0, "Quentin Tarantino")
guests.insert(2, "Ridley Scott")
guests.append("James Cameron")

## Print to screen the new invites
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[1].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.")
print(guests[3].title() + ", you are invited to join me for dinner.")
print(guests[4].title() + ", you are invited to join me for dinner.")
print(guests[5].title() + ", you are invited to join me for dinner.\n")

## Try it Yourself 3-7: Shrinking Guest List
############################################

## Creating a list of guests and printing to screen their invites
guests = ["Philip K. Dick","H.P. Lovecraft","William Gibson"]
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[1].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.\n")

## Printing to screen those guests that cannot make it
print("I'm afraid ",guests[0]," cannot make it to dinner.")
print("I'm afraid ",guests[2]," cannot make it to dinner.\n")

## Deleting and replacing guests that cannot make it
del(guests[0])
guests.insert(0, "Bruce Sterling")
del(guests[2])
guests.insert(2, "Richard Morgan")

## Printing to screen new invites for guests that can make it
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.\n")

## Informing guests we have new dinner table
print("Attention all guests: We are getting a bigger dinner table!\n")

## Adding new guests with "insert" and "append" attributes
guests.insert(0, "Quentin Tarantino")
guests.insert(2, "Ridley Scott")
guests.append("James Cameron")

## Print to screen the new invites
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[1].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.")
print(guests[3].title() + ", you are invited to join me for dinner.")
print(guests[4].title() + ", you are invited to join me for dinner.")
print(guests[5].title() + ", you are invited to join me for dinner.\n")

## Printing a message to state only two guests may now attend dinner
print("Unfortunately, we did not get the table we wanted. Only two guests may come to dinner now.\n")

## Removing four guests and informing them there is no room for them
guest = guests.pop()
print("Hi " + guest.title() + ", sorry I have to cancel your invite. We did not get the table we wanted in time.")

guest = guests.pop()
print("Hi " + guest.title() + ", sorry I have to cancel your invite. We did not get the table we wanted in time.")

guest = guests.pop()
print("Hi " + guest.title() + ", sorry I have to cancel your invite. We did not get the table we wanted in time.")

guest = guests.pop()
print("Hi " + guest.title() + ", sorry I have to cancel your invite. We did not get the table we wanted in time.\n")

## Inviting the last two guests
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[1].title() + ", you are invited to join me for dinner.\n")

## Removing the last two names on the guest list
del guests[0]
del guests[0]

## Ensuring there are no guests in the guest list
print(guests,"\n")


## Try it Yourself 3-8: Seeing the World
############################################ 

## Putting locations I want to visit into a list
places = ["Landshut","Tokoyo","Hong Kong","Seoul","London"]

## Printing the list as-is
print(places)

## Sorting the list and printing again
print(sorted(places))

## Printing my list again as-is
print(places)

## Printing my list in reverse
places.reverse()
print(places)

## Reversing my list back to normal
places.reverse()
print(places)

## Using sort to permanently sort my list
places.sort()
print(places)

## Using Sort to sort my list in reverse alphabetical order
places.sort(reverse= True)
print(places,"\n")


## Try it Yourself 3-9: Dinner Guests
############################################

## Creating a list of guests and printing to screen their invites
guests = ["Philip K. Dick","H.P. Lovecraft","William Gibson"]
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[1].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.\n")

## Number of guests currently invited
print("You have",len(guests),"guests currently attending your dinner\n")

## Printing to screen those guests that cannot make it
print("I'm afraid ",guests[0]," cannot make it to dinner.")
print("I'm afraid ",guests[2]," cannot make it to dinner.\n")

## Number of guests currently invited
print("You have",len(guests),"guests currently attending your dinner\n")

## Deleting and replacing guests that cannot make it
del(guests[0])
guests.insert(0, "Bruce Sterling")
del(guests[2])
guests.insert(2, "Richard Morgan")

## Printing to screen new invites for guests that can make it
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.\n")

## Number of guests currently invited
print("You have",len(guests),"guests currently attending your dinner\n")

## Informing guests we have new dinner table
print("Attention all guests: We are getting a bigger dinner table!\n")

## Adding new guests with "insert" and "append" attributes
guests.insert(0, "Quentin Tarantino")
guests.insert(2, "Ridley Scott")
guests.append("James Cameron\n")

## Print to screen the new invites
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[1].title() + ", you are invited to join me for dinner.")
print(guests[2].title() + ", you are invited to join me for dinner.")
print(guests[3].title() + ", you are invited to join me for dinner.")
print(guests[4].title() + ", you are invited to join me for dinner.")
print(guests[5].title() + ", you are invited to join me for dinner.\n")

## Number of guests currently invited
print("You have",len(guests),"guests currently attending your dinner\n")

## Printing a message to state only two guests may now attend dinner
print("Unfortunately, we did not get the table we wanted. Only two guests may come to dinner now.\n")

## Removing four guests and informing them there is no room for them
guest = guests.pop()
print("Hi " + guest.title() + ", sorry I have to cancel your invite. We did not get the table we wanted in time.")

guest = guests.pop()
print("Hi " + guest.title() + ", sorry I have to cancel your invite. We did not get the table we wanted in time.")

guest = guests.pop()
print("Hi " + guest.title() + ", sorry I have to cancel your invite. We did not get the table we wanted in time.")

guest = guests.pop()
print("Hi " + guest.title() + ", sorry I have to cancel your invite. We did not get the table we wanted in time.\n")

## Inviting the last two guests
print(guests[0].title() + ", you are invited to join me for dinner.")
print(guests[1].title() + ", you are invited to join me for dinner.")

## Number of guests currently invited
print("\nYou have",len(guests),"guests currently attending your dinner\n")

## Removing the last two names on the guest list
del guests[0]
del guests[0]

## Ensuring there are no guests in the guest list
print(guests)

## Number of guests currently invited
print("\nYou have",len(guests),"guests currently attending your dinner\n")


## Try it Yourself 3-10: Every Function
############################################

## Storing a list of countries and printing it to screen
countries = ["America","Russia","China","Germany","England","Canada"]
print(countries)

## Accessing an item in the list and printing it to screen
print("\nI am printing a country from the list to screen:",countries[4].title(),"\n")

## Changing an item in a list
countries[5] = "Australia"
print(countries,"\n")

## Adding a country to the list
countries.append("France")

## Inserting into the list
countries.insert(3, "Belgium")

## Removing a country from the list
del countries[5]
print(countries)

## Removing a country from the list using the pop method
popped_country = countries.pop(4)
print(countries)
print(popped_country)

## Removing a country from the list by value
countries.remove("France")
print(countries)

## Organizing the list permanently with sort
countries.sort()
print(countries)

## Organizing the list with a temporary sort
print(sorted(countries))

## Organizing the list permanently with sort in reverse order
countries.sort(reverse = True)
print(countries)

## Printing the list in reverse order
countries.reverse()
print(countries)

## Finding the length of a list
print("\nThe length of the list is",len(countries),"countries.")







