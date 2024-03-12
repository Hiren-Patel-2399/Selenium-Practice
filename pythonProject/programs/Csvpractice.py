# import os
import os
from csv import *

#wp to create a folder name python in language folder
# data=os.mkdir("Python")
# print(data)
############################################################

#wp to create for loop,while loop, comperhension, function.txt file

# os.chdir(r"C:\Language\Python")
# with open("for loop.txt","x")as file:
#     pass

# os.chdir(r"C:\Language\Python")
# with open("while loop.txt","x")as file:
#     pass

# os.chdir(r"C:\Language\Python")
# with open("comperhension.txt","x")as file:
#     pass

# os.chdir(r"C:\Language\Python")
# with open("function.txt","x")as file:
#     pass
#############################################################################
#wp to create a file called result in python folder only the student who pass in java exam

# l=[]
# with open(r"C:\Language\Java\student.csv", "r") as file:
#     data=DictReader(file)
#     for i in data:
#         if i['status'] == "Pass":
#             l.append(i)
#
# os.chdir(r"C:\Language\Python")
#
# with open("result.csv", "w", newline="") as file:
#     d=DictWriter(file,["sname","branch","status"])
#     d.writeheader()
#     d.writerows(l)

#############################################################################################################
#class ceration

#1
# class Student:
#     sid=234
#     sname="Hiren"
#     standard="12th"
#     school_name="BMS school"
#     steram="Science"

#accessing by class name
# print(Student.sid)        234
# print(Student.sname)      Hiren
# print(Student.standard)   12th
# print(Student.school_name)BMS school
# print(Student.steram)     Science

#accessing by object
# s=Student()
# print(s.sid)               234
# print(s.sname)             Hiren
# print(s.standard)          12th
# print(s.school_name)       BMS school
# print(s.steram)            Science

#################################################################################
#2
# class Pen:
#     color="black"
#     nipple="pointed"
#     ink="full"
#     brand_name="Doms"
#     cap_height="2cm"

#accessing by class name
# print(Pen.color)       black
# print(Pen.nipple)    pointed
# print(Pen.brand_name)  Doms
# print(Pen.ink)         full
# print(Pen.cap_height)  2cm

#accessing by object
# p=Pen()
# print(p.color)       black
# print(p.nipple)      pointed
# print(p.ink)         full
# print(p.brand_name)  Doms
# print(p.cap_height)  2cm
#########################################################################
#3
# class Bank:
#     name="SBI"
#     accno=234
#     branch="Basvanagudi"
#     ifsc="SBI00342"
#     phone_no="8273923021"

#accessing by class name
# print(Bank.name)     #SBI
# print(Bank.accno)    234
# print(Bank.branch)   Basvanagudi
# print(Bank.ifsc)      SBI00342
# print(Bank.phone_no)   8273923021

#accessing by object
# b=Bank()
# print(b.name)       SBI
# print(b.accno)      234
# print(b.branch)     Basvanagudi
# print(b.ifsc)       SBI00342
# print(b.phone_no)   8273923021
######################################################################################
#4
# class Collage:
#     name="BMS_Collage"
#     loc="Basvanagudi"
#     principle="Roshan Singh"
#     staff=23
#     sector="Government"

#accessing by class name
# print(Collage.name)        BMS_Collage
# print(Collage.loc)         Basvanagudi
# print(Collage.principle)   Roshan Singh
# print(Collage.staff)       23
# print(Collage.sector)      Government

#accessing by object

# c=Collage()
# print(c.name)          BMS_Collage
# print(c.loc)           Basvanagudi
# print(c.principle)     Roshan Singh
# print(c.staff)         23
# print(c.sector)        Government
#############################################################################3
#5

# class Paper:
#     paper_size="A4"
#     type="unrulled"
#     color="white"
#     corner="pointed"
#     price="Rs 12"

#accessing by class name
# print(Paper.paper_size)     A4
# print(Paper.type)           unrulled
# print(Paper.color)          white
# print(Paper.corner)         pointed
# print(Paper.price)          Rs 12

#accessing by object
# p=Paper()
# print(=p.paper_size)     A4
# print(p.type)           unrulled
# print(p.color)          white
# print(p.corner)         pointed
# print(p.price)          Rs 12


