'''
Created on 15/01/2013

@author: kalunga
'''
from mongoengine import *
from mongodb import Core

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    
