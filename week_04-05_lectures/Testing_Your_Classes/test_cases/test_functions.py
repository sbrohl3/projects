import unittest
from functions.function_library import *

class NamePartTestCase(unittest.TestCase):
    """Test for functions in the function_library.py file"""

    def test_valid_name_part(self):
        """Here is a bunch of values I think should work"""
        valid_names_to_test = ["Tom", "tom", " Tom", "Tom ", " tom", "tom "]
        
        for name in valid_names_to_test:
            self.assertTrue(validate_name_part(name))
        
    def test_invalid_name_part(self):
        """Here is a bunch of values I think should not work"""
        invalid_names_to_test = ["Tom'", "123", " Tom 123", "Tom#", "    "]
        
        for name in invalid_names_to_test:
            self.assertFalse(validate_name_part(name))

