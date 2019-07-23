import unittest
from classes.employee import Employee

class test_employees(unittest.TestCase):
    """This class is used to test the employee.py Class"""

    def setUp(self):
        """Stores test employee information for testing purposes"""
        self.employee = Employee("Steven", "Brohl", 85000)
    
    def test_give_default_raise(self):
        """Tests the default raise ammount for the give_raise method within Employee""" 
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 90000)

    def test_give_custom_raise(self):
        """Tests a custom raise ammount for the give_raise method within Employee""" 
        self.employee.give_raise(2000)
        self.assertEqual(self.employee.salary, 87000)


## python -m unittest test_cases.test_employees