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
        