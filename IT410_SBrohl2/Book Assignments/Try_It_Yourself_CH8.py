## Try it Yourself Excercises - Chapter 8
## IT 410 - Walsh College
## 06/02/2019
## BROHL, STEVEN


## Try it Yourself 8-1: Message
############################################

def display_message():
    print("\nI am learning about functions in this chapter!")

display_message()


## Try it Yourself 8-2: Favorite Book
############################################

def favorite_book(title):
    print("\nOne of my favorite books is " + title + ".")

favorite_book("Neuromancer")


## Try it Yourself 8-3: T-Shirt
############################################

def make_shirt(size, message):
    print("\nT-shirt Size: " + size)
    print("Message on the T-shirt: " + message)

make_shirt("Extra Large", "Loch Network Security Services")
make_shirt(size="Large", message="Walsh College")


## Try it Yourself 8-4: Large Shirt
############################################

def make_shirt(size="Large", message="I love Python"):
    print("\nT-shirt Size: " + size)
    print("Message on the T-shirt: " + message)
    
make_shirt()
make_shirt("Medium")
make_shirt("Extra Large", "Walsh College")


## Try it Yourself 8-5: Cities
############################################

def describe_city(city, country="America"):
    print("\n" + city + " is in " + country + ".")

describe_city("New York")
describe_city("Detroit")
describe_city("Reykjavik","Iceland")


## Try it Yourself 8-6: City Names
############################################

def city_country(passed_list):
    for values in passed_list:
        print("\n\"" + values["city"] + ", " + values["country"] + "\"")

city_country_list = [{"city": "Detroit", "country": "America"}, {"city": "Roseville" , "country": "Michigan"}, {"city": "Alger" , "country": "Michigan"}]
city_country(city_country_list)


## Try it Yourself 8-7: Album
############################################

def make_album(artist, title, numtracks=0):
    music_dict = []
    music_dict.append({"artist": artist, "title": title, "numtracks": numtracks})
    
    return print(music_dict)

print("\n")
artist = "Alan Parsons"
title = "Eye in the Sky"
make_album(artist, title)

artist = "Tom Petty"
title = "Full Moon Fever"
make_album(artist, title)

artist = "FM Attack"
title = "Stellar"
numtracks = 15
make_album(artist, title, numtracks)


## Try it Yourself 8-8: User Albums
############################################

def make_album(artist, title, numtracks=0):
    music_dict = []
    music_dict.append({"artist": artist, "title": title, "numtracks": numtracks})
    
    return print(music_dict)

print("\n")
program = 0
while program < 3:
    artist = input("\nWho is your favorite music artist: ")
    title = input("Name one of their albums: ")
    program += 1
    make_album(artist, title)


## Try it Yourself 8-9: Magicians
############################################

def show_magicians(passed_list):
    print("\n")
    for magician in magicians:
        print(magician)

magicians = ["Merlin", "Houdini", "Blaine", "Angel"]
show_magicians(magicians)


## Try it Yourself 8-10: Great Magicians
############################################

def make_great(magicians):
    modded_magicians = []
    while magicians:
        current_magician = magicians.pop()
        current_magician =  current_magician + " the Great"
        modded_magicians.append(current_magician)
    for magician in modded_magicians:
        magicians.append(magician)

def show_magicians(passed_list):
    print("\n")
    for magician in magicians:
        print(magician)

magicians = ["Merlin", "Houdini", "Blaine", "Angel"]
make_great(magicians)
show_magicians(magicians)


## Try it Yourself 8-11: Unchanged Magicians
############################################

def make_great(magicians, modded_magicians):
    modded_magicians_list = []
    while magicians:
        current_magician = magicians.pop()
        current_magician =  current_magician + " the Great"
        modded_magicians_list.append(current_magician)
    for magician in modded_magicians_list:
        modded_magicians.append(magician)

def show_magicians(passed_list1, passed_list2):
    print("\n")
    for magician in passed_list1:
        print(magician)
    print("\n")
    for magician in passed_list2:
        print(magician)


magicians = ["Merlin", "Houdini", "Blaine", "Angel"]
modded_magicians = []
make_great(magicians[:], modded_magicians)
show_magicians(magicians, modded_magicians)




