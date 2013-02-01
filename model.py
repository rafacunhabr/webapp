'''
Created on 15/01/2013

@author: kalunga
'''
from mongoengine import *

CORE_INITIALIZED = False

class Core(object):
    '''
    classdocs
    '''

    @classmethod
    def initialize(cls):
        global CORE_INITIALIZED
        if CORE_INITIALIZED is False:  
            connect('terratv')
            CORE_INITIALIZED = True
           
    @classmethod
    def is_initialized(cls):
        global CORE_INITIALIZED
        return CORE_INITIALIZED
    
class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    
