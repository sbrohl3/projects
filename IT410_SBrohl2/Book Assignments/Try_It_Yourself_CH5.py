## Try it Yourself Excercises - Chapter 5
## IT 410 - Walsh College
## 05/19/2019
## BROHL, STEVEN


## Try it Yourself 5-1: Conditional Tests
############################################

## 1 - True
name = "steven"
print("Is name == \"Steven\"? I predict True.")
print(name.title() == "Steven")

## 2 - False
print("Is name == \"Bob\"? I predict False.")
print(name.title() == "Bob")

## 3 - True
lastname = "brohl"
print("\nIs lastname == \"Brohl\"? I predict True.")
print(lastname.title() == "Brohl")

## 4 - False
print("Is lastname == \"Smith\"? I predict False.")
print(lastname.title() == "Smith")

## 5 - True
car = "pontiac"
print("\nIs car == \"Pontiac\"? I predict True.")
print(car.title() == "Pontiac")

## 6 - False
print("Is car == \"Toyota\"? I predict False.")
print(car.title() == "Toyota")

## 7 - True
city = "roseville"
print("\nIs city == \"Roseville\"? I predict True.")
print(city.title() == "Roseville")

## 8 - False
print("Is city == \"Warren\"? I predict False.")
print(city.title() == "Warren")

## 9 - True
state = "michigan"
print("\nIs state == \"Michigan\"? I predict True.")
print(state.title() == "Michigan")

## 10 - False
print("Is state == \"Ohio\"? I predict False.")
print(state.title() == "Ohio")
print("\n")


## Try it Yourself 5-2: More Conditional Tests
############################################

## Equality of strings - True
course1 = "it410"
print("Course1 == Course1 - True")
print(course1 == course1)

## Inequality of strings - False
course1 = "it410"
print("Course1 != Course1 - False")
print(course1 != course1)
print("\n")

## Test using the Lower() Function - True
name = "Steven"
print("Steven.lower == \"steven\" - True")
print(name.lower() == "steven")

## Test using the Lower() Function - False
print("Steven.lower == \"Steven\" - False")
print(name.lower() == "Steven")
print("\n")

## Numerical Test - Equality - True
age = 18
print("Age is equal to 18 - True")
print(age == 18)

## Numerical Test - Equality - False
print("Age is equal to 21 - False")
print(age == 21)
print("\n")

## Numerical Test - Inequality - True
age = 18
print("Age is not equal to 21 - True")
print(age != 21)

## Numerical Test - Inequality - False
print("Age is not equal to 18 - False")
print(age != 18)
print("\n")

## Numerical Test - Greater Than - True
number = 15
print("The number variable is greater than 10 - True")
print(number > 10)

## Numerical Test - Greater Than - False
print("The number variable is greater than 20 - False")
print(number > 20)
print("\n")

## Numerical Test - Less Than - True
number = 5
print("The number variable is less than 10 - True")
print(number < 10)

## Numerical Test - Less Than - False
print("The number variable is less than 4 - False")
print(number < 4)
print("\n")

## Numerical Test - Greater Than or Equal to - True
number = 10
print("The number variable is greater than or equal to 10 - True")
print(number >= 10)

## Numerical Test - Greater Than or Equal to -False
print("The number variable is greater than 15 - False")
print(number >= 15)
print("\n")

## Numerical Test - Less Than or Equal to - True
number = 10
print("The number variable is less than or equal to 10 - True")
print(number <= 10)

## Numerical Test - Less Than or Equal to - False
print("The number variable is less than 8 - False")
print(number <= 8)
print("\n")

## AND - True
number1 = 17
number2 = 22
print("Number 1 is greater than or equal to 16 AND Number 2 is greater than or equal to 21 - True")
print(number1 >= 16 and number2 >= 21)

## AND - False
print("Number 1 is greater than or equal to 16 AND Number 2 is greater than or equal to 23 - False")
print(number1 >= 16 and number2 >= 23)
print("\n")

## OR - True
number1 = 3
number2 = 43
print("Number 1 is greater than or equal to 2 OR Number 2 is greater than or equal to 43 - True")
print(number1 >= 4 or number2 >= 43)

## OR - False
print("Number 1 is greater than or equal to 1 OR Number 2 is greater than or equal to 43 - True")
print(number1 >= 15 or number2 >= 45)
print("\n")

## Test whether an item is in a list - True
names = ["bob","steve","ted","alex"]
print("Is the name steve in the list? - True")
print("steve" in names)

## Test whether an item is in a list - False
print("Is the name Jack in the list? - False")
print("jack" in names)
print("\n")

## Test whether an item is not in a list - True
names = ["bob","steve","ted","alex"]
print("The name James is not in the list? - True")
print("james" not in names)

##  Test whether an item is not in a list - False
print("The name Steve is not in the list? - False")
print("steve" not in names)
print("\n")


## Try it Yourself 5-3: Alien Colors #1
############################################

## Passed Condition
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!\n")
## Failed Condition
alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points!\n")


## Try it Yourself 5-4: Alien Colors #2
############################################

## If color is green
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!\n")
else:
    print("You just earned 10 points!\n")

## If color is not green
alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points!\n")
else:
    print("You just earned 10 points!\n")


## Try it Yourself 5-5: Alien Color #3
############################################

## If color is Green
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!\n")
elif alien_color == "yellow":
    print("You just earned 10 points!\n")
else:
    print("You just earned 15 points!\n")

## If color is Yellow
alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points!\n")
elif alien_color == "yellow":
    print("You just earned 10 points!\n")
else:
    print("You just earned 15 points!\n")

## If color is Red
alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points!\n")
elif alien_color == "yellow":
    print("You just earned 10 points!\n")
else:
    print("You just earned 15 points!\n")


## Try it Yourself 5-6: Stages of Life
############################################

## Using If-Elif-Else chain to print a statement between a certain number
age = 24
if age < 2:
    print("This person is a baby.\n")
elif age < 4:
    print("This person is a toddler.\n")
elif age < 13:
    print("This person is a kid.\n")
elif age < 20:
    print("This person is a teenager.\n")
elif age < 65:
    print("This person is an adult.\n")
else: 
    print("This person is an elder.\n")


## Try it Yourself 5-7: Favroite Fruit
############################################

## Creating a list of favorite fruits
favorite_fruits = ["bananas","apples","oranges"]

## if statements to check if certain fruits are in my list
## 1
if "bananas" in favorite_fruits:
    print("You really like bananas!\n")

## 2
if "kiwis" in favorite_fruits:
    print("You really like kiwis!\n")

## 3
if "mangoes" in favorite_fruits:
    print("You really like mangoes!\n")

## 4
if "apples" in favorite_fruits:
    print("You really like apples!\n")

## 5
if "oranges" in favorite_fruits:
    print("You really like oranges!\n")



## Try it Yourself 5-8: Hello Admin
############################################

users = ["steven","karl","tyler","jeremy","admin"]

for name in users:
    if name == "admin":
        print("Hello Admin, would you like to see a status report?\n")
    else:
        print("Hello " + name.title() +", thank you for logging in again.\n")


## Try it Yourself 5-9: No Users
############################################

users = []

for name in users:
    if name == "admin":
        print("Hello Admin, would you like to see a status report?\n")
    else:
        print("Hello " + name.title() +", thank you for logging in again.\n")
else: 
    print("We need to find some users!\n")


## Try it Yourself 5-10: Checking Usernames
############################################

current_users = ["John","Alan","STEWART","ted","sue"]
new_users = ["SUE","Shelly","sam","Ted","Timothy"]
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user.title() + ", this username has been taken! Please enter a new username.\n")
    else:
        print(new_user.title() + ", this username is available!\n")


## Try it Yourself 5-11: Ordinal Numbers
############################################

numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
print("\n")

