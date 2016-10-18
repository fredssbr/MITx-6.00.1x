# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:45:37 2016

@author: frederico
"""

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, " + utterance)    