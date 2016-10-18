# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:23:11 2016

@author: frederico
"""

class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """Create empty grade book"""
        self.students = [] # list of Student objects
        self.grades = {} # maps idNum -> list of Grades
        self.isSorted = True # true if self.students is sorted
    
    def addStudent(self, student):
        """Assumes: student is of type Student
        Add student to grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def getGrades(self, student):
        """Returns a list of grades for student"""
        try: # returns a copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def allStudents(self):
        """Returns a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] # returns a copy list of students
    
    def gradeReport(course):
        """Assumes: course is of type Grades"""
        report = []
        for s in course.allStudents():# use method to get data (preserves information hiding)
            tot = 0.0
            numGrades = 0
            for g in course.getGrades(s):
                tot += g
                numGrades += 1
            try:
                average = tot/numGrades
                report.append(str(s) + '\'s mean grade is ' + str(average))
            except ZeroDivisionError:
                report.append(str(s) + ' has no grades')
        return '\n'.join(report) #returns a string with carriage return between student's grades
    
    