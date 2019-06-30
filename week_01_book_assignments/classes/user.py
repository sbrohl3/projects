class User():
    """A class to represent a user"""

    def __init__(self, first_name, last_name, address, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone = phone
        self.login_attempt = 0

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name + "\t" + self.address + "\t" + self.email + "\t" + self.phone)

    def greet_user(self):
        print("Hello " + self.first_name.title() + ", welcome to the program!")

    def increment_login_attempts(self):
        self.login_attempt += 1
    
    def reset_login_attempts(self):
        self.login_attempt = 0
