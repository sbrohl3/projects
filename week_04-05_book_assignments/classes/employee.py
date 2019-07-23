class Employee():
    """ A class to represent an Employee"""

    def __init__(self, first_name, last_name, salary):
        """A constructor for the Employee Class"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, add_salary=5000):
        """ A method for increasing employee salary"""
        self.salary += add_salary
        return(print(self.first_name, self.last_name, self.salary))