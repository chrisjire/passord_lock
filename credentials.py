import pyperclip
import random
import string

#Global Variables
global users_list
class User:
    '''
    Class to create user accounts and save their information
    '''
    users_list = []
    def __init__(self,first_name,last_name,age,password):
        '''
        Methord to define the properties for each user object
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.password = password
        
    def save_user(self):
        '''
        Function to save a newly created user
        '''
        self.users_list.append(self)
        
class Credential:
    '''
	Class to create  account credentials and generate passwords and save their information
	'''
	# Class Variables
    credentials_list =[]
    user_credentials_list = []
    @classmethod
    def check_user(cls,first_name,password):
        '''
        Method that checks if the name and password entered match entries in the users_list
        '''
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user
    
    def __init__(self,user_name,site_name,account_name,password):
    
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password
    
    def save_credentials(self):
        '''
        Function to save a newly created user instance
        '''
        Credential.credentials_list.append(self)
        
    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate an 8 character password for a credential
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass
        
    @classmethod
    def display_credentials(cls,user_name):
        '''
        Class method to display the list of credentials saved
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list
    
    def delete_credentials(self):
    
        '''
        delete_credentials method deletes saved credentials
        '''

        Credential.credentials_list.remove(self)