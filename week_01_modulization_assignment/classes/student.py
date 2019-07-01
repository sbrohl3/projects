from classes.student import Person

class Student(Person):
    """A simple Student class"""

    def __init__(self):
        self.IDnum = IDnum
        self.name = name
        self.email = email
        self.program_of_study = program_of_study
        college_records.append(self.IDnum, self.name, self.email, self.program_of_study)
        

    def displayInformation(self):
        print("\nStudent Information: ")
        print("Student ID: " + self.IDnum)
        print("Name: " + self.name)
        print("Email: " + self.email)
        print("Program of Study: " + self.program_of_study)