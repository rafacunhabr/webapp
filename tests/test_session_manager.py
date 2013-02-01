'''
Created on 01/02/2013

@author: rafael.cunha
'''
#from model import 
from appController import SessionManager

def test_check_credentials_ok():
    assert(SessionManager.check_credentials('Rafael') <> None)

def test_check_credentials_nok():
    assert(SessionManager.check_credentials('rafael') is None)
