from classes.user import User

class Admin(User):
    """A class to represent an Admin"""

    def __init__(self, first_name, last_name, address, email, phone):
        super().__init__(first_name, last_name, address, email, phone)
        self.privileges = Privileges()

class Privileges():
    """A simple class to store privileges"""

    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("User privileges: ")
        for privilege in self.privileges:
            print(privilege.title())