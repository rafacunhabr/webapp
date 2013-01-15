'''
Created on 15/01/2013

@author: kalunga
'''
from mongoengine import connect
from mongodb import *

CORE_INITIALIZED = False

class Core(object):
    '''
    classdocs
    '''

    @classmethod
    def initialize(cls):
        global CORE_INITIALIZED
        if CORE_INITIALIZED is False:  
            print '----- not initialized'
            connect('terratv')
            CORE_INITIALIZED = True
        else:
            print '----- already initialized'
            
    @classmethod
    def is_initialized(cls):
        global CORE_INITIALIZED
        return CORE_INITIALIZED
          
        