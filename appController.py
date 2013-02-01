'''
Created on 01/02/2013

@author: rafael.cunha
'''
from model import * 

class SessionManager():

    @classmethod
    def check_credentials(self,username):
        if not Core.is_initialized():
            Core.initialize()
        for user in User.objects(first_name = username):
            return user
        return None
        
