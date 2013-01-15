'''
Created on 15/01/2013

@author: rafael.cunha
'''
from mongoengine import *
from mongodb import Core

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    
if __name__ == '__main__':
    rafael = User(email='rafael.cunha@corp.terra.com.br', first_name='Rafael', last_name='da Cunha')
    rafael.save()
