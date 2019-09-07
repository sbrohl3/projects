## Try it Yourself Excercises - Chapter 4
## IT 410 - Walsh College
## 05/13/2019
## BROHL, STEVEN


## Try it Yourself 4-1: Pizzas
############################################v

## Declared a new variable list for types of favorite pizzas then printed the list using a for loop
fav_pizza = ["Pepperoni","Supreme","BLT"]
for pizza in fav_pizza:
    print(pizza)
print("\n")

## Added a sentence in the for loop print statement and then added a print statement outside of the for loop    
for pizza in fav_pizza:
    print("I like",pizza,"pizza.")
print("\nI really love pizza!\n")


## Try it Yourself 4-2: Animals
############################################

## Declared a new variable list for types of animals then printed the list using a for loop
animals = ["Bird","Dog","Cat"]
for animal in animals:
    print("A",animal,"would make for a great pet!")
## Added a print statement outside of the for loop 
print("\nAny of these animals would make a great pet!\n")


## Try it Yourself 4-3: Counting to Twenty
############################################

## Created a for loop to print all of the numbers from 1 to 20
print("A for loop to print all numbers from 1 to 20")
for numbers in range(1,21):
    print(numbers)
print("\n")


## Try it Yourself 4-4: One Million
############################################

## Creating a list from 1 to 1000000 and printing it to screen with a for loop
print("A list from one to one million:")
for numbers in range(1,1000001):
    print(numbers)
print("\n")

## Try it Yourself 4-5: Summing a Million
############################################

## Creating a list from 1 to 1000000
numbers = list(range(1,1000001))
## min, max, and sum of the list
print("The minimum number in the list is:",min(numbers))
print("The maximum number in the list is:",max(numbers))
print("The sum of all numbers in the list is:",sum(numbers))
print("\n")


## Try it Yourself 4-6: Odd Numbers
############################################

## Creating a for loop from 1 to 20 to print all odd numbers
print("All odd numbers for a list from 1 - 20")
for numbers in range(1,21,2):
    print(numbers)
print("\n")


## Try it Yourself 4-7: Three
############################################

## Creating a for loop from 3 to 30 to print all multiples of 3
numbers = list(range(3,31,3))
print("All multiples of 3, between 3 and 30")
for number in numbers:
    print(number)
print("\n")


## Try it Yourself 4-8: Cubes
############################################

## Creating an empty list called cubes which will be populated by the first ten cubes
cubes = []
print("First 10 cubes")
for number in range(1,11):
    cube = number**3
    cubes.append(cube)
print(cubes)
print("\n")


## Try it Yourself 4-9: Cube Comprehension
############################################

## Generating the first ten cubes in a list and then printing them to screen
cubes = [number**3 for number in range(1,11)]
print("First 10 cubes using comprehension")
print(cubes)
print("\n")


## Try it Yourself 4-10: Slices
############################################

## Creating a for loop from 3 to 30 to print all multiples of 3
numbers = list(range(3,31,3))
print("All multiples of 3, between 3 and 30")
for number in numbers:
    print(number)

print("\n")
print("The first three items in the list are: ",numbers[0:3])
print("Three items from the middle of the list are: ",numbers[3:6])
print("The last three items in the list are: ",numbers[6:9])
print("\n")


## Try it Yourself 4-11: My Pizza, Your Pizza
############################################

## Declared a new variable list for types of favorite pizzas then printed the list using a for loop
fav_pizza = ["Pepperoni","Supreme","BLT"]
for pizza in fav_pizza:
    print(pizza.title())
print("\n")

## Added a sentence in the for loop print statement and then added a print statement outside of the for loop    
for pizza in fav_pizza:
    print("I like",pizza,"pizza.")
print("\nI really love pizza!\n")

## Copying fav_pizza into the variable list friend_pizzas
friend_pizzas = fav_pizza[:]

## Appending new pizzas to the lists
fav_pizza.append("Hawaiin")
friend_pizzas.append("Meat Lover's")

## Creating a for loop and printing each list
print("\nMy favorite pizzas are: ")
for pizza in fav_pizza:
    print("\t--",pizza.title())

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print("\t--",pizza.title())


## Try it Yourself 4-12: More Loops
############################################

## Declared a new variable list for types of foods
my_foods = ['pizza', 'falafel', 'carrot cake']

## Copying my_foods into the variable list friend_foods
friend_foods = my_foods[:]

## Creating a for loop and printing each list
print("\nMy favorite foods are:")
for food in my_foods:
    print("\t--",food.title())

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print("\t--",food.title())


## Try it Yourself 4-13: Buffet
############################################

## Declaring a tuple called "menu"
menu = ("Chicken","Pizza","French Fries","Steak")

## Using a for loop to print out all of the values in the menu list
print("\nPlease order from one of the following items: ")
for food in menu:
    print("\t--",food.title())
    
## Declaring a new tuple called "menu" with two updated values
menu = ("Chicken","Pizza","Steamed Vegetables","Chicken Noodle Soup")

## Using a for loop to print out all of the values in the menu list
print("\nPlease order from one of the following items: ")
for food in menu:
    print("\t--",food.title())
