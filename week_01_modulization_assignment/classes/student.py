## Importing the Person class so the Student class can inherit it
from classes.person import Person

class Student(Person):
    """A simple Student class"""

    def __init__(self, IDnum=0, name='', email='', program_of_study=''):
        ## A constructor for instantiating variables to be used in the Student class
        self.IDnum = IDnum
        self.name = name
        self.email = email
        self.program_of_study = program_of_study

    def displayInformation(self):
        ## A method for displaying student information
        print("\nStudent Information: ")
        print("Student ID: " + self.IDnum)
        print("Name: " + self.name)
        print("Email: " + self.email)
        print("Program of Study: " + self.program_of_study)
        
