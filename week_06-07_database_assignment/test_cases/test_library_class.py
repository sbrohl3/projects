import unittest
from classes.library import library

class TestLibraryClass(unittest.TestCase):
    """Test the library Class"""

    def setUp(self):
        """An instance of the Library class for testing all the other class functions"""
        self.library = library()

    def test_valid_book_title(self):
        """Here are some book_title checks I know will validate to True"""
        valid_title_to_test = ["\"Time Out Of Joint\"", "\'Neuromancer\'", "The Man in the High Castle ", "Martian Time Slip", "A scanner DaRkLy", " Clans of Alphane Moon\'"]
        
        for title in valid_title_to_test:
            self.library.book_title = title
            self.assertTrue(self.library.validateBookTitle())


    def test_valid_Author(self):
        """Here are some author name checks I know will validate to True"""
        valid_names_to_test = ["PKD", "Philip K. Dick", "WillIam Gibson", "H.G. Wells", "George OrWell ", "AlDoUs HUxLey"]
        
        for name in valid_names_to_test:
            self.library.book_author = name
            self.assertTrue(self.library.validateAuthorName())

    def test_invalid_Author(self):
        """Here are some author name checks I know will not validate to True"""
        invalid_names_to_test = ["!PKD@ ", " ##Philip K. Dick", " ^&William Gibson ", "!!!George Orwell", "@ld0u$ Huxley!"]
        
        for name in invalid_names_to_test:
            self.library.book_author = name
            self.assertFalse(self.library.validateAuthorName())

    def test_valid_ISBN(self):
        """Here are some ISBN number checks I know will validate to True"""
        valid_numbers_to_test = ["978-120312", "781-123421", "999654-2111242", "978-1246473", "525-12-125", "425-3113-1212"]
        
        for number in valid_numbers_to_test:
            self.library.isbn = number
            self.assertTrue(self.library.validateISBN())

    def test_invalid_ISBN(self):
        """Here are some ISBN number checks I know will not validate to True"""
        invalid_numbers_to_test = ["124246468412451", "978-124512125413", "952-852-15561-!2312", "!123@2554221412", "!@#125441252221", "@31352565251aa!"]
        
        for number in invalid_numbers_to_test:
            self.library.isbn = number
            self.assertFalse(self.library.validateISBN())

    def test_valid_copies_purchased(self):
        """Here are some int checks I know will validate to True"""
        valid_number_types_to_test = [13, 10, 20]
        
        for number_type in valid_number_types_to_test:
            self.library.num_copies_purchased = number_type
            self.assertTrue(self.library.validateNumCopies())
                 
    def test_invalid_copies_purchased_type(self):
        """Here are some int checks I know will validate to False"""
        valid_number_types_to_test = ["asdad", "123asdad", "122!! ", "!!@@sdad ", " asdada!", " 12223!!$", "123adasd", "12fgg!!", "123fasdas"]
        
        for number_type in valid_number_types_to_test:
            self.library.num_copies_purchased = number_type
            self.assertFalse(self.library.validateNumCopies())
   
    def test_valid_copies_checked(self):
        """Here are some int checks I know will validate to True"""
        valid_number_types_to_test = ["0", "0", "0"]
        
        for number_type in valid_number_types_to_test:
            self.library.num_copies_checked = number_type
            self.assertTrue(self.library.validateNumCopiesChecked())
    
    def test_invalid_copies_checked(self):
        """Here are some int checks I know will not validate to True"""
        invalid_number_types_to_test = ["!5", "3@31", "25^^$sdf"]
        
        for number_type in invalid_number_types_to_test:
            self.library.num_copies_checked = number_type
            self.assertFalse(self.library.validateNumCopiesChecked())

    def test_valid_copies_checked2(self):
        """Here are some int checks I know will validate to True"""
        valid_number_types_to_test = ["0", "0", "0"]
        
        for number_type in valid_number_types_to_test:
            self.library.num_copies_checked = number_type
            self.assertTrue(self.library.validateNumCopiesChecked2())

    def test_invalid_copies_checked2(self):
        """Here are some int checks I know will not validate to True"""
        invalid_number_types_to_test = ["!5", "3@31", "25^^$sdf"]
        
        for number_type in invalid_number_types_to_test:
            self.library.num_copies_checked = number_type
            self.assertFalse(self.library.validateNumCopiesChecked2())

    def test_valid_retail_prices(self):
        """Here are some float checks I know will validate to True"""
        valid_number_types_to_test = [5.99, 3.99, 25.99]
        
        for number_type in valid_number_types_to_test:
            self.library.retail_price = number_type
            self.assertTrue(self.library.validateRetailPrice())

    def test_invalid_retail_prices(self):
        """Here are some float checks I know will not validate to True"""
        valid_number_types_to_test = ["asda5.99", "8.99adad", "adad5.55"]
        
        for number_type in valid_number_types_to_test:
            self.library.retail_price = number_type
            self.assertFalse(self.library.validateRetailPrice())

## python -m unittest test_cases.test_library_class


    
    
    
    
    
            
           
            
