import unittest
import pyperclip
from credentials import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviors.
    
    Args:
        unittest.TestCase: helps in creating test case
    '''
    def setUp(self):
        '''
        Function to create a user account before each test
        '''
        self.new_user = User('Christian','Jire','21','Pwd123456')
        
    def test__init__(self):
        '''
        Test to if check the creation of user instances works
        '''
        self.assertEqual(self.new_user.first_name,'Christian')
        self.assertEqual(self.new_user.last_name,'Jire')
        self.assertEqual(self.new_user.age,'21')
        self.assertEqual(self.new_user.password,'Pwd123456')
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()