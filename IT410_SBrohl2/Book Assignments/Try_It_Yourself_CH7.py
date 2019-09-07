## Try it Yourself Excercises - Chapter 7
## IT 410 - Walsh College
## 05/25/2019
## BROHL, STEVEN


## Try it Yourself 7-1: Rental Car
############################################

car = input("What kind of car would you like? ")
print("Let me see if I can find you a " + car)

## Try it Yourself 7-2: Restaurant Seating
############################################

print("\n")
group_size = input("How many people are in your Dinner group? ")
group_size = int(group_size)

if group_size > 8:
    print("I'm sorry, but you will have to wait for another table to open up.")
else:
    print("Your table is ready.")

## Try it Yourself 7-3: Multiples of Ten
############################################

print("\n")
number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")

## Try it Yourself 7-4: Pizza Toppings
############################################

program_running = True

while program_running == True:
    toppings = input("\nEnter a topping or type quit to exit: ")
    if toppings != "quit":
        print("I will add " + toppings + " onto your pizza.")
    elif toppings == "quit":
        program_running = False

## Try it Yourself 7-5: Movie Tickets
############################################

age_check = True

print("\n")
while age_check == True:
    age = input("Enter your age or type quit: ")
    if age == "quit":
        age_check = False
        break
    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10")
    elif age > 12:
        print("Your ticket is $15")

## Try it Yourself 7-6: Three Exits
############################################

## Active variable to control how long the loop runs
active = True

print("\n")
## Conditional test to stop the loop
while active == True:
    age = input("Enter your age or type quit: ")
    if age == "quit":
        print("Now exiting program.")
        ## Break statement to break the loop
        break
    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10")
    elif age > 12:
        print("Your ticket is $15")

## Try it Yourself 7-8: Deli
############################################

sandwich_orders = ["ham","salami","bologna","corn beef"]
finished_sandwiches = []

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I am currently making a " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
    
## Try it Yourself 7-9: No Pastrami
############################################

sandwich_orders = ["ham","pastrami","salami","bologna","corn beef","pastrami","turkey","pastrami"]
finished_sandwiches = []

print("\nSorry, we are all out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I am currently making a " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

## Try it Yourself 7-10: Dream Vacation
############################################

responses_list = []
running = True


print("\n")
while running:
    name = input("What is your name: ")
    place = input("If you could visit one place in the world where would it be? ")
    responses_list.append({"name": name, "place": place})
    repeat = input("Would you like to let another person respond? yes/no: ")
    if repeat == "no":
        running = False

for response in responses_list:
    print("\n" + response["name"].title() + "'s dream vacation is in " + response["place"].title() + ".") 


        