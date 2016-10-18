# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:50:01 2016

@author: frederico
"""

class MITPerson(Person):
    
    """this is a class attribute. all instances (objects in memory)
    have access to it (like a shared attribute)"""
    nextIdNum = 0 #next id number to assign
    
    def __init__(self,name):
        Person.__init__(self, name) #initializes Person attributes
        self.idNum = MITPerson.nextIdNum #MITPerson attribute: unique ID
        MITPerson.nextIdNum += 1
    
    def getIdNum(self):
        return self.idNum
    
    # sorting MIT people uses their ID number, not name!    
    def __lt__(self, other):
        """If you try to compare MITPerson < Person, it will raise an AttributeError
        because it is equivalent to MITPerson.__lt__(Person) - only MITPerson has idNum.
        However, if you try Person < MITPerson, it will compare correctly because
        it is equivalent to Person.__lt__(MITPerson) - both classes have name due to 
        MITPerson inheriting from Person"""
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.name + " says: " + utterance)
    
    
        