
## 10-1: Learning Python

with open("text_files/learning_python.txt") as learning_python:
    contents = learning_python.read()
    print(contents + "\n\n")

with open("text_files/learning_python.txt") as learning_python:  
    for line in learning_python:
        print(line.rstrip())

print("\n\n")
with open("text_files/learning_python.txt") as learning_python:  
    lines = learning_python.readlines()

for line in lines:
    print(line.strip())
 

## 10-2: Learning C

print("\n\n")
with open("text_files/learning_python.txt") as learning_python:
    for line in learning_python:
        modded_line = line.replace("Python", "C")
        print(modded_line.strip())


## 10-3: Guest

print("\n\n")
with open("text_files/guest_list.txt", "w") as guest_list:
    guest = input("What is your name: ")
    guest_list.write(guest)

## 10-4: Guest Book

print("\n\n")
program_run = True

while program_run == True:
    with open("text_files/guest_book.txt", "a") as guest_book:
        guest = input("What is your name: ")
        print("Hello, " + guest + ", thank you for visiting! \n")
        guest_book.write(guest + "\n")
        response = False
        while response == False: 
            cont_program = input("Do you want to add another guest to the guest book? Y/N")
            if cont_program.capitalize() == "Y":
                response = True
                program_run = True
                
            elif cont_program.capitalize() == "N":
                response = True
                program_run = False
                
            else:
                print("Wrong input \n")
                response = False

## 10-5: Programming Poll

program_run = True

while program_run == True:
    with open("text_files/programming_poll.txt", "a") as programming_poll:
        response = input("Why do you like programming? ")
        programming_poll.write(response + "\n")
        exit_response = False
        while exit_response == False: 
            cont_program = input("Do you want to let someone else respond? Y/N")
            if cont_program.capitalize() == "Y":
                exit_response = True
                program_run = True
                
            elif cont_program.capitalize() == "N":
                exit_response = True
                program_run = False
                
            else:
                print("Wrong input \n")
                exit_response = False


## 10-6: Addition

try:
    first_number = input("What is your first number: ")
    second_number = input("What is your second number: ")
    # Add first number to second number
    answer = int(first_number) + int(second_number)

except ValueError:
    print("One of your numbers is not an integer.")

else:
    print(first_number," + ",second_number," = ",answer)


## 10-7: Addition Calculator

program_run = True

while program_run == True:
    try:
        first_number = input("What is your first number: ")

        second_number = input("What is your second number: ")
        
        # Add first number to second number
        answer = int(first_number) + int(second_number)

    except ValueError:
        print("One of your numbers is not an integer.")

    else:
        print(first_number," + ",second_number," = ",answer)

    exit_response = False
    while exit_response == False: 
        cont_program = input("Do you want to continue entering in more numbers? Y/N")
        if cont_program.capitalize() == "Y":
            exit_response = True
            program_run = True
            
        elif cont_program.capitalize() == "N":
            exit_response = True
            program_run = False
            
        else:
            print("Wrong input \n")
            exit_response = False


## 10-8: Cats and Dogs

files = ["cats.txt", "dogs.txt"]

for file in files:
    try:
        with open("text_files/" + file) as file_obj:
            print(file_obj.read())

    except FileNotFoundError:
        print("The file you are referring to is not found.")


## 10-9: Silent Cats and Dogs

files = ["cats.txt", "dogs.txt"]

for file in files:
    try:
        with open("text_files/" + file) as file_obj:
            print(file_obj.read())

    except FileNotFoundError:
        pass

## 10-10: Common Words

books = ["the_masque_of_the_red_death.txt", "the_cask_of_the_amontillado.txt", "the_variable_man.txt"]

for book in books:
    with open("text_files/" + book) as book_obj:
        print("The word 'the' appears in this book", book_obj.read().lower().count("the"), "times")
    
    
## 10-11: Favorite Number

import json

favorite_number = input("What is your favorite number: ")

with open("text_files/favorite_numbers.json", "w") as favorite_numbers_obj:
    json.dump(favorite_number, favorite_numbers_obj)
    
with open("text_files/favorite_numbers.json") as favorite_numbers_obj:
    numbers = json.load(favorite_numbers_obj)
    print("I know your favorite number! It's " + str(numbers) + ".")


## 10-12: Favorite Number Remembered

import json

try:
    with open("text_files/favorite_numbers.json") as favorite_numbers_obj:
        numbers = json.load(favorite_numbers_obj)
        print("I know your favorite number! It's " + str(numbers) + ".")
except:
    favorite_number = input("What is your favorite number: ")
    with open("text_files/favorite_numbers.json", "w") as favorite_numbers_obj:
        json.dump(favorite_number, favorite_numbers_obj)


## 10-13: Verify User

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open("text_files/" + filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open("text_files/" + filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username == None:
        username = get_new_username()
        print("Welcome " + str(username) + ".")
  
    else:
        verify_user = input("Hello, " + str(username.title()) + " is this your correct username? Y/N ")
        if verify_user.capitalize() == "Y":
            print("Thank you for verifying! Welcome back to the program, " + str(username) + ".")
        else:
            username = get_new_username()
            print("Welcome " + str(username) + ".")
  
greet_user()