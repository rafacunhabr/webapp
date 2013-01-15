'''
Created on 15/01/2013

@author: rafael.cunha
'''
from mongoengine import connect

class Core(object):
    '''
    classdocs
    '''

    @classmethod
    def initialize(cls):
        connect('terratv')

