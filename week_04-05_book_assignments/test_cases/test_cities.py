import unittest
from functions.city_functions import *

class test_city_country(unittest.TestCase):
    """This class is used to test the city_functions.py"""

    def test_city_country(self):
        """Does a location like Landshut, Germany work?"""
        formatted_location = get_formatted_location("Landshut", "Germany")
        self.assertEqual(formatted_location, "Landshut, Germany")


    def test_city_country_pop(self):
        """Does a location like santiago, chile work with a default population of 5000000?"""
        formatted_location = get_formatted_location_and_pop("santiago", "chile", city_pop="5000000")
        self.assertEqual(formatted_location, "santiago, chile - population 5000000")
