# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:22:29 2016

@author: frederico
"""

import datetime

class Person(object):

    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[1]
    
    def getLastName(self):
        """returns self's last name"""
        return self.lastName
    
    def __str__(self):
        """returns self's name"""
        return self.name
    
    def setBirthday(self, month, day, year):
        """sets self's birthday"""
        self.birthday = datetime.date(year, month, day)
    
    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """returns True if self's name is lexicographically
        less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    