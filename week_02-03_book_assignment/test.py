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