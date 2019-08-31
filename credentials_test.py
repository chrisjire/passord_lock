import unittest
import pyperclip
from credentials import User, Credential


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
        
    def test_save_user(self):
        '''
		Test to check if the new users info is saved into the users list
		'''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
        
class TestCredentials(unittest.TestCase):
    '''
	Test class that defines test cases for the credentials class behaviors.
	Args:

        unittest.TestCase: helps in creating test cases
	'''
    def test_check_user(self):
        '''
		Function to test whether the login in function check_user works as expected
		'''
        self.new_user = User('Christian','Jire','21','pwd123456')
        self.new_user.save_user()
        user2 = User('Chase','Lorde',22,'pw123456')
        user2.save_user()
        for user in User.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
        return current_user

        self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credential('Christian','Facebook','chris','pwd123456')
        
    def test__init__(self):
        '''
        Test to if check the initialization/creation of credential instances is properly done
        '''
        
        self.assertEqual(self.new_credential.user_name,'Christian')
        self.assertEqual(self.new_credential.site_name,'Facebook')
        self.assertEqual(self.new_credential.account_name,'chris')
        self.assertEqual(self.new_credential.password,'pwd123456')

    def test_save_credentials(self):
        '''
        Test to check if the new credential info is saved into the credentials list
        '''
        self.new_credential.save_credentials()
        twitter = Credential('louis','Twitter','lou','14789')
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)
        
    def tearDown(self):
        '''
        Function to clear the credentials list after every test
        '''
        Credential.credentials_list = []
        User.users_list = []
        
    def test_display_credentials(self):
        '''
        Test to check if the display_credentials method, displays the correct credentials.
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Chris','Twitter','will','pwd123456')
        twitter.save_credentials()
        LinkedIn = Credential('chris','LinkedIn','will','pwd123456')
        LinkedIn.save_credentials()
        self.assertEqual(len(Credential.display_credentials(twitter.user_name)),1)
        
    #def test_delete_credentials(self):
        #'''
        #test_delete_contact to test if we can remove a contact from our contact list
        #'''
        #self.new_credential.save_credentials()
        #test_credential = Credential('Christian','Jire','21','pwd123456')
        #test_credential.save_credentials()

        #self.new_credential.delete_credentials()
        #self.assertEqual(len(Credential.delete_credentials),1)

    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_site_name method returns the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Chris','Twitter','will','pwd123456')
        twitter.save_credentials()
        credential_exists = Credential.find_by_site_name('Twitter')
        self.assertEqual(credential_exists,twitter)

    def test_copy_credential(self):
        '''
        Test to check if the copy a credential method copies the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Chris','Twitter','will','pwd123456')
        twitter.save_credentials()
        find_credential = None
        for credential in Credential.user_credentials_list:
                find_credential =Credential.find_by_site_name(credential.site_name)
                return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.site_name)
        self.assertEqual('pwd123456',pyperclip.paste())
        print(pyperclip.paste())

        
if __name__ == '__main__':
    unittest.main()