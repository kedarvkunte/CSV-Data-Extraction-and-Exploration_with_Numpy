import unittest
import numpy as np

####################################################
# Problem 1: Classes
####################################################
        
class Course:

    def __init__(self, course_number):
        ## Add code here ##
        self.course_number = course_number
        self.roster = []
        
    def get_course_number(self):
        ## Add code here ##
        return self.course_number
        
    def add_student(self, student):
        ## Add code here ##

        self.roster.append(student)
        
    def drop_student(self,student_id):
        ## Add code here ##
        if (student_id in self.roster):
            print(student_id, " has dropped the course ",self.course_number)
            self.roster.remove(student_id)

        else:
            print(student_id," is not in the course ", self.course_number)
        
    def get_roster(self):
        ## Add code here ##
        return sorted(self.roster,key = str.lower)


course1 = Course(590)
course2 = Course(589)

course1.add_student("Roy")
course2.add_student("Emma")
course1.add_student("Douglass")
course2.add_student("Martin")
course1.add_student("Henry")
course2.add_student("Erik")

print("There are two courses: 1) ",course1.get_course_number()," and 2)", course2.get_course_number())

course1_studentlist = course1.get_roster()
print(" Course ",course1.get_course_number(), "has following students : ",course1_studentlist)

course2_studentlist = course2.get_roster()
print(" Course ",course2.get_course_number(), "has following students : ",course2_studentlist)


#str_input = input("Enter student to drop from course ")
course1.drop_student('Roy')
course2.drop_student('Emma')
course2.drop_student('Chris')


course1_studentlist = course1.get_roster()
print(" Course ",course1.get_course_number(), "has following students : ",course1_studentlist)


course2_studentlist = course2.get_roster()
print(" Course ",course2.get_course_number(), "has following students : ",course2_studentlist)




        
####################################################
# Problem 2: Root Finding
####################################################
from math import sqrt
from sys import float_info


def root_finder(a, b, c, max_iter=1000, x0=0):
    xn = x0
    for i in range(max_iter):
        xn = xn - (a*(xn**2) + b*xn + c) / (2*a*xn + b)
    return xn

def find_roots(a,b,c):
    ## Add code here ##


    if a ==0 and b == 0 and c == 0:
        return []
    elif (a == 0):
        return [float(-1*c/b)]
    elif (c ==0):
        tmp_list = [float(-1*b/a),0]
        return sorted(tmp_list)
    elif (b ==0) and ((-1*c/a)>=0):
        return [-1*sqrt(-1*c/a),sqrt(-1*c/a)]
    elif (b ==0) and ((-1*c/a)<0):
        return []
    elif (b**2 - 4*a*c == 0):
        return [float(-1*b/(2*a))]
    elif (b**2 - 4*a*c < 0):
        return []
    elif (b**2 - 4*a*c > 0):
        if (abs(b**2-(b**2-4*a*c))>1e-08):
            tmp = sqrt(b**2-4*a*c)
            tmp_list = [float((-b-tmp)/(2*a)),float((-b+tmp)/(2*a))]
            return sorted(tmp_list)
        elif (abs(b**2-(b**2-4*a*c))<1e-08):
            one_root = root_finder(a,b,c)
            other_root = c/(a*one_root)
            return sorted([one_root, other_root])


list_of_roots = find_roots(1e-8,10,1e-8)
print("Roots : ",list_of_roots)

list_of_roots = find_roots(1,7,12)
print("Roots : ",list_of_roots)

list_of_roots = find_roots(-3,5,2)
print("Roots : ",list_of_roots)

list_of_roots = find_roots(0,5,4)
print("Roots : ",list_of_roots)

list_of_roots = find_roots(1.5,7.2,0)
print("Roots : ",list_of_roots)

list_of_roots = find_roots(4,5,4)
print("Roots : ",list_of_roots)