'''
Created on Aug 15, 2017

@author: zhaxind
'''

class item():
    def __init__(self, name, price, detailed_URL):
        '''
        Constructor
        '''
        self.name = name
        self.price = price
        self.detailed_URL = detailed_URL
        
    def printName(self):    
        print(self.name)
        return