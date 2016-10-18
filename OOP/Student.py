# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:58:45 2016

@author: frederico
"""

class Student(MITPerson):
    #special keyword: there is no expression in the body
    pass
    
    def isStudent(obj):
        return isinstance(obj, Student)