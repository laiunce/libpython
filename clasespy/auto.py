# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:29:12 2018

@author: LAC40641
"""

#https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

class Auto(object):

    wheels = 4
    wheels2 = 2
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def pantalla(self):
        return 'a'
    
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'auto'
    
    def numsum(self,numsum):
        """"Return a string representing the type of vehicle this is."""
        return 9+numsum
    


