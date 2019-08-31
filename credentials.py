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
        
        #Instance Variable
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
    
        # instance variables
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password
    
    def save_credentials(self):
        '''
        Function to save a newly created user instance
        '''
        # global users_list
        Credential.credentials_list.append(self)
        