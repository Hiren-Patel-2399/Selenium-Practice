# conditional statment

# wp to check number is +v2/_ve

# data=eval(input("enter number="))
# if data>0:
#     print(f"{data} is positive")
# elif data<0:
#     print(f"{data} is negative")
# else:
#     print(f"{data} is netural number")
####################################################################################

#wp to check data is indiviual/sequence/iterable

# data=eval(input("enter value:"))
# if isinstance(data,(int,float,bool,complex)):
#     print(f"{data} is indiviual")
# elif isinstance(data,(str,tuple,list)):
#     print(f"{data} is sequence")
# else:
#     print(f"{data} is iterable")
######################################################################################

#wp to should take str as data type else invalid data type if it is str then give options upper, length, swapcase, appeand

# data=eval(input("enter value="))
#
# if isinstance(data,str):
#     op=eval(input("1.Upper, 2.length, 3.Swapcase, 4.Appand \n"))
#     if op==1:
#         print(data.upper())
#     elif op==2:
#         print(len(data))
#     elif op==3:
#         print(data.swapcase())
#     elif op==4:
#         print(data.lower())
#     else:
#         print("invaid option")
# else:
#     print(f"{data} is invalid data type")

############################################################################################

# looping statement

# wp to print sum of each tuple from a list

# l=[(3,4),(1,7),(5,8),(2,9)]
# for i ,j in l:
#     print(i+j)

# for i in l:
#     print(sum(i))
##################################################################

#wp to print element are collection data type

# l=[["hai",1],[12,2],[(11,22),3],[2.3,4]]
# for i ,j in l:
#     if isinstance(i, (str,tuple,set,dict,list)):
#         print(i)
####################################################################

# wp to print a place name only the temp is in even

# l={"bangalore":23,"mysour":16,"manglore":26}
# for i in l:
#     print(i)

# for i,j in l.items():
#     if j%2==0:
#         print(i)
#######################################################################

# unpacking iterable in for loop

# l=[(10,'a'),(20,'b'),(30,'c')]
# # for i in l:
# #     print(i)
#
# for i,j in l:
#     print(i,j)
##########################################################################

# wp to print a number which is divisible by 2 but not wiyh 5

# l=[34,67,12,98,45,18]
# for i in l:
#     if i%2==0 and not i%5==0:
#         print(i)
#############################################################################

# interview programs

# wp to find factorial no of 6(1*2*3*4*5*6)

# n=6
# res=1
# for i in range(1,n+1):
#     res=i*res
# print(res)

#############
#(6*5*4*3*2*1)
# n=6
# res=1
# for i in range(n,0,-1):
#     res=i*res
# print(res)

# find factorial by using function

# def number(n):
#     res=1
#     for i in range(1,n+1):
#         res=i*res
#     return (res)
# print(number(6))

#####################################################

#wp to print sum of n natural number

# n=5
# res=0
# for i in range(1,n+1):
#     res=i+res
# print(res)

# sum of n natural number using function

# def number(n):
#     res=0
#     for i in range(1,n+1):
#         res=i+res
#     return res
# print(number(6))

#############################################################

#wp function should accept a number if number is even return sum of n natual number else return factorial of n

# def number(n):
#     if n%2==0:
#         res=0
#         for i in range(1,n+1):
#             res=i+res
#         return res
#     else:
#         res1=1
#         for i in range(1,n+1):
#             res=i*res
#         return res
# print(number(24))
######################################################################

# wp to print sum of odd number from 1 to 20

# with if condition

# res=1
# for i in range(1,20):
#     if i%2==1:
#         res=res+i
# print(res)

# with-out if condition
# res=1
# for i in range(1,20,2):
#     res=res+i
# print(res)
############################################################################

# wp to sort given no using bubble sort
# l=[75,3,45,2,10,35]
# for i in range(len(l)):
#     for j in range(i):
#         if l[j]>=l[i]:
#             l[i],l[j]= l[j],l[i]
# print(l)

###########################################################################

#wp to sort given no using bubble sort in decending order
# l=[75,3,45,2,10,35]
# for i in range(len(l)):
#     for j in range(i):
#         if l[j]<=l[i]:
#             l[i],l[j]= l[j],l[i]
# print(l)

##################################################################################

# wp to print 1st max no. from given list

# l=[75,3,45,2,10,35]
# for i in range(len(l)):
#     for j in range(i):
#         if l[j]<=l[i+1]:
#             l[i+1],l[j]= l[j],l[i+1]
#             if len
# print(l)

###################################################################

# def bubble_sort(arr):
#     n = len(arr)
#
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     return arr
#
# def find_max(lst):
#     sorted_list = bubble_sort(lst)
#     return sorted_list[-1]
#
# numbers = [75, 3, 45, 2, 10, 35]
# result = find_max(numbers)
#
# print(f"The first maximum number is: {result}")


# def bubble_sort_min(lst):
#     n = len(lst)
#
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#
#     return lst[0]
#
# # Example usage
# my_list = [75, 3, 45, 2, 10, 35]
# result = bubble_sort_min(my_list)
#
# if result is not None:
#     print(f"The first minimum number in the list is: {result}")
# else:
#     print("The list is empty.")

# def reverse_string_with_special_chars(s):
#     string_list = list(s)
#
#     start, end = 0, len(s) - 1
#
#     while start < end:
#         if not s[start].isalnum():
#             start += 1
#         elif not s[end].isalnum():
#             end -= 1
#         else:
#
#             string_list[start], string_list[end] = string_list[end], string_list[start]
#             start += 1
#             end -= 1
#
#     result = ''.join(string_list)
#     print(result)
#
# s = "ab*cd//gd"
# reverse_string_with_special_chars(s)

# l = [3, 7, 5, 6, 1, 9]
#
# def find_pairs(lst):
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] + lst[j] == 10:
#                 print(f"Pair: ({lst[i]}, {lst[j]})")
#
# # Call the function with the provided list
# find_pairs(l)

# s='python@1991'
# s1=""
# for i in s:
#     if                                      #i.islower():
#         s1= s1 +chr(ord(i)-32)
#     else:
#         s1= s1+i
#
# print(s1)

######################################################################

# s='SaTuRDay'
# s1=''
# for i in s:
#     if i.isupper():
#         s1+=i.lower()
#     elif i.islower():
#         s1+=i.upper()
#     else:
#         s1+=i
# print(s1)

#################################################################################

# s="Tommrow IS SatUrDay"
# s1=''
# for i in s:
#     if i.isupper():
#         s1=s1+i
# print(s1)
#################################################

# s="the price of iphone 15 is rs.67865"
# s1=''
# for i in s:
#     if i.isdigit():
#         s1+=i
# print(s1)
##############################################

# s='the #supper acting %offer is 34.78,* packing $us'
# s1=''
# for i in s:
#     if not i.isalpha() and not i.isdigit():
#         s1+=i
# print(s1)


##############################################################
##s="SatuRDay"
##s1=""
##for i in s:
##    if ord(i)>=66 and ord(i)<=92:
##        s1=s1+chr(ord(i)+32)
##    elif ord(i)>=97 and ord(i)<=122:
##        s1=s1+chr(ord(i)-32)
##print(s1)

##s="SatuRDay"
##s1=""
##for i in s:
##    if ord(i)>=66 and ord(i)<=92:
##        s1=s1+chr(ord(i))
##print(s1)


##s="SatuRDay123"
##s1=""
##for i in s:
##    if ord(i)>=66 and ord(i)<=122:
##        pass
##    else:
##        s1=s1+i
##print(s1)


##s="SatuRDay123"
##s1=""
##for i in s:
##    if ord(i)>=66 and ord(i)<=122:
##        pass
##    elif i==' ':
##        pass
##    else:
##        s1=s1+i
##print(s1)

# s="Today is Monday"
# d={}
# def search(s):
#     for i in s:
#         if i.isalpha():
#             d[i]=i.index()
# print(d)

# s="helloo"
# s1=''
# for i in s:
#     if s.count(i)>1:
#         s1=s1+"-"
#     else:
#         s1=s1+i
# print(s1)

# s="tommrow python programming first mock"
# l=s.split()
# l1=[]
# for i in l:
#     print(len(i))
#     l1.append(i)
#
# print(l1)

##pattern progms

##for i in range(1,5):
##    print("*")


##for i in range(1,5):
##    print(i)


##for i in range(65,69):
##    print(chr(i))

##ch=65
##for i in range(1,5):
##    print(chr(ch))
##    ch+=1


##ch=90
##for i in range(1,5):
##    print(chr(ch))
##    ch-=1

# ch=65
# for i in range(1,5):
#     print(chr(ch))
#     ch+=2

# ch=65
# for i in range(1,3):
#     print(chr(ch))
#     print(i)
#     ch+=1

# ch=65
# num=1
# for i in range(1,5):
#     if i%2==0:
#         print(num)
#         num+=1
#     else:
#         print(chr(ch))
#         ch+=1
#############################################

# for i in range(1,5):
#     print("*",end=" ")
###############################################

# num=1
# for i in range(1,5):
#     print(num,end=" ")
#     num+=1
#
# 1 2 3 4
########################################

# ch=65
# for i in range(1,5):
#     print(chr(ch),end=" ")
#     ch+=1
#     A B C D
#######################################

# ch=87
# for i in range(1,5):
#     print(chr(ch),end=" ")
#     ch+=1
#     W X Y Z
###############################################

# cha=65
# ch2=97
# for i in range(1,5):
#     if i%2==1:
#         print(chr(cha),end=" ")
#         cha+=1
#     else:
#         print(chr(ch2),end=" ")
#         ch2+=1
# A a B b


# num=1
# for i in range(1,5):
#     if i%2==1:
#         print(num,end=" ")
#         num+=1
#     else:
#         print("*",end=" ")
# 1 * 2 *


# num=1
# cha=90
#
# for i in range(1,5):
#     if i%2==1:
#         print(num,end=" ")
#         num+=1
#     else:
#         print(chr(cha),end=" ")
#         cha-=1
# 1 Z 2 Y


# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end=" ")
#     print()
#
# * * * *
# * * * *
# * * * *
# * * * *



# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()
#
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
################################################33

# num=1
# for i in range(1,5):
#     for j in range(1,5):
#         print(num,end=" ")
#     num+=1
#     print()
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
############################################################

# for i in range(1,5):
#     n=4
#     for j in range(1,5):
#         if i%2==1:
#             print(j,end=" ")
#         else:
#             print(n,end=" ")
#             n-=1
#     print()
#
# 1 2 3 4
# 4 3 2 1
# 1 2 3 4
# 4 3 2 1
###########################################################################

#assignment
###################################################################################
# ch=65
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()
#
# A B C D
# E F G H
# I J K L
# M N O P

###########################################

#
# for i in range(1,5):
#     ch = 65
#     for j in range(1,5):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()
#
# A B C D
# A B C D
# A B C D
# A B C D
#############################################

# ch=65
# for i in range(1,5):
#     for i in range(1,5):
#         print(chr(ch),end=" ")
#     ch+=1
#     print()
#
# A A A A
# B B B B
# C C C C
# D D D D
###########################################

#
# for i in range(1,5):
#     ch = 65
#     ch2 = 68
#     for j in range(1,5):
#         if i%2==1:
#             print(chr(ch), end=" ")
#             ch+=1
#         else:
#             print(chr(ch2),end=" ")
#             ch2-=1
#     print()
#
# A B C D
# D C B A
# A B C D
# D C B A
##############################################3

# ch=65
# num=1
# for i in range(1,5):
#     for j in range(1,5):
#         if i%2==1:
#             print(num,end=" ")
#             num+=1
#         else:
#             print(chr(ch),end=" ")
#             ch+=1
#     print()
#
# 1 2 3 4
# A B C D
# 5 6 7 8
# E F G H
############################################
# not working

# ch=65
# ch2=97
# for i in range(1,5):
#     for j in range(1,5):
#         if i%2==1:
#             print(chr(ch),end=" ")
#             ch+=1
#         else:
#             print(chr(ch2),end=" ")
#             ch2+=1
#     print()
#
# A B C D
# a b c d
# E F G H
# e f g h
############################################


# car=65
# cha=90
# for i in range(1,5):
#     for j in range(1,5):
#         if i%2==1:
#             print(chr(car),end=" ")
#             car+=1
#         else:
#             print(chr(cha),end=" ")
#             cha-=1
#     print()
#
# A B C D
# Z Y X W
# E F G H
# V U T S

#####################################################
# num=1
# for i in range(1,5):
#     for j in range(1,5):
#         print(num,end=" ")
#         num+=1
#     print()
#
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

###############################################

# num=2
# for i in range(1,5):
#     for j in range(1,5):
#         print(num, end=" ")
#         num+=2
#     print()
#
# 2 4 6 8
# 10 12 14 16
# 18 20 22 24
# 26 28 30 32

###############################################


# num=1
# cha=65
# for i in range(1,5):
#     for j in range(1, 5):
#         if j % 2 == 1:
#             print(chr(cha), end=" ")
#             cha += 1
#         else:
#             print(num,end=" ")
#             num += 1
#     print()

###################################################


# for i in range(1,5):
#     num = 1
#     cha = 65
#     for j in range(1, 5):
#         if i % 2 == 1:
#             print(chr(cha), end=" ")
#             cha += 1
#         else:
#             print(num,end=" ")
#             num += 1
#     print()
#
# A B C D
# 1 2 3 4
# A B C D
# 1 2 3 4
################################################3


# num=1
# cha=65
# for i in range(1,5):
#     for j in range(1,5):
#         if i%2==1:
#             print(chr(cha),end=" ")
#             cha+=1
#         else:
#             print(num%2,end=" ")
#     num+=1
#     print()
# A B C D
# 1 1 1 1
# E F G H
# 2 2 2 2
##########################################################33
 # first logic
# num=2
# cha=65
# for i in range(1,5):
#     for j in range(1,5):
#         if i%2==1:
#             print(chr(cha),end=" ")
#             cha+=1
#         else:
#             print(num//2,end=" ")
#             num+=1
#     print()

# A B C D
# 1 1 2 2
# E F G H
# 3 3 4 4
########################################################

# second logic
# num=0
# cha=65
# for i in range(1,5):
#     for j in range(1,5):
#         if i%2==1:
#             print(chr(cha),end=" ")
#             cha+=1
#         else:
#             print((num//2)+1,end=" ")
#             num+=1
#     print()
# A B C D
# 1 1 2 2
# E F G H
# 3 3 4 4
########################################################
# cha=65
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(cha),end=" ")
#         cha+=2
#     print()

# A C E G
# I K M O
# Q S U W
# Y [ ] _

###################################################3

# num = 1
# cha = 65
# for i in range(1,5):
#     for j in range(1,5):
#         if j%2==0:
#             print(chr(cha), end=" ")
#         else:
#             print(num,end=" ")
#     num+=1
#     cha+=1
#     print()
# 1 A 1 A
# 2 B 2 B
# 3 C 3 C
# 4 D 4 D
#############################################

# num=0
# cha=65
# for i in range(1,5):
#     for j in range(1,5):
#         if i%2==1:
#             print(chr(cha),end=" ")
#             cha+=1
#         else:
#             print((num%2)+i-1,end=" ")
#             num+=1
#     print()
#
# A B C D
# 1 2 1 2
# E F G H
# 3 4 3 4
#####################################################################

# Triangle pattern

# *
# *
# *
# * * * *
#####################################
#second logic

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or i==n:
#             print("*",end=" ")
#     print()

######################################################3
# * * * *
# *
# *
# *
# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==n:
#             print("*",end=" ")
#     print()
###################################################
# * * * *
#       *
#       *
#       *
# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
###################################################
#     *
#   * *
# * * *
# n=5
# for i in range(1,n-1):
#     for j in range(1,n-1):
#         if i+j>=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#############################################################
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==4 or i==1 or i==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
###########################################################3

# Triangle pattern

# one ways

# # frist logic
# *
# * *
# * * *
# * * * *
# * * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#############################################################################
# second logic
# *
# * *
# * * *
# * * * *
# * * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#####################################3
# second way
#
# *
# * *
# * * *
# * * * *
# n=4
# star=1
# space=3
# for _ in range(1,n+1):
#     for i in range(1,star+1):
#         print("*",end=" ")
#     star+=1
#     for j in range(1,space+1):
#         print(" ",end=" ")
#     space-=1
#     print()
##############################################################
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# # first ways
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j>=i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# second ways
# n=5
# star=5
# space=0
# for _ in range(1,n+1):
#     for j in range(1, space+1):
#         print(" ",end=" ")
#     space+=1
#     for i in range(1, star+1):
#         print("*",end=" ")
#     star-=1
#     print()

############################################33
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# n=4
# for i in range(0,n+1):
#     for j in range(0,n+1):
#         if i+j>=n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#      *
#     * *
#   * * *
# * * * *
# n=4
# star=1
# space=3
# for _ in range(1,n+1):
#     for j in range(1,space+1):
#         print(" ",end=" ")
#     space-=1
#     for i in range(1,star+1):
#         print("*",end=" ")
#     star+=1
#     print()
#######################################################33
# * * * * *
# * * * *
# * * *
# * *
# *

# #first way
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j<=n+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# second ways
# n=5
# star=5
# space=0
#
# for _ in range(0,n+1):
#     for i in range(0,star):
#         print("*",end=" ")
#     star-=1
#     for j in range(0, space+1):
#         print(" ",end=" ")
#     space+=1
#     print()

###################################################33
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# First way
# n=4
# num=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=i:
#             print(num,end=" ")
#             num+=1
#         else:
#             print(" ",end=" ")
#     print()

# second ways
# n=4
# num=1
# space=3
# no=1
# for _ in range(1,n+1):
#     for i in range(1,num+1):
#         print(no,end=" ")
#         no+=1
#     num+=1
#     for j in range(1, space+1):
#         print(" ",end=" ")
#     space-=1
#     print()

#######################################################
# first way
# a
# b c
# d e f
# g h i j

# n=4
# cha=97
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=i:
#             print(chr(cha),end=" ")
#             cha+=1
#         else:
#             print(" ",end=" ")
#     print()

# second ways

# n=4
# cha=97
# space=3
# num=1
# for _ in range(1,n+1):
#     for i in range(1, num+1):
#         print(chr(cha),end=" ")
#         cha+=1
#     num+=1
#     for j in range(1, space+1):
#         print(" ",end=" ")
#     space-=1
#     print()

##############################################################
# 1 2 3 4
#   5 6 7
#     8 9
#       10

# first ways
# n=4
# num=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j>=i:
#             print(num,end=" ")
#             num+=1
#         else:
#             print(" ",end=" ")
#     print()

# seond ways

# n=4
# num=4
# space=0
# no=1
# for _ in range(1, n+1):
#     for j in range(1, space+1):
#         print(" ", end=" ")
#     space+=1
#     for i in range(1, num+1):
#         print(no, end=" ")
#         no += 1
#     num -= 1
#
#     print()

###############################################################
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# n=4
# for i in range(1,n+1):
#     num = 1
#     for j in range(1,n+1):
#         if i+j<=n+1:
#             print(num,end=" ")
#             num+=1
#         else:
#             print(" ",end=" ")
#     print()

# second ways

# n=4
# num=4
# space=0
#
# for _ in range(1,n+1):
#     no = 1
#     for i in range(1, num+1):
#         print(no,end=" ")
#         no+=1
#     num-=1
#     for j in range(1, space+1):
#         print(" ",end=" ")
#     space-=1
#     print()

###########################################################################
# 2
# 4 6
# 8 10 12
# 14 16 18 20

# n=4
# num=2
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j<=i:
#             print(num,end=" ")
#             num+=2
#         else:
#             print(" ",end=" ")
#     print()


# second ways
# n=4
# num=2
# space=3
# no=1
# for _ in range(1,n+1):
#     for i in range(1,no+1):
#         print(num,end=" ")
#         num+=2
#     no+=1
#     for j in range(1, space+1):
#         print(" ",end=" ")
#     space-=1
#     print()
########################################################
# 1 2 3 4
# A B C
# 5 6
# D
# n=4
# cha=65
# num=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j<=n+1:
#             if i%2==1:
#                 print(num,end=" ")
#                 num+=1
#             else:
#                 print(chr(cha),end=" ")
#                 cha+=1
#         else:
#             print(" ",end=" ")
#     print()

# second ways
# n=4
# cha=65
# num=4
# space=0
# no=1
# for l in range(1,n+1):
#     for i in range(1,num+1):
#         if l%2==0:
#             print(chr(cha),end=" ")
#             cha+=1
#         else:
#             print(no,end=" ")
#             no+=1
#     num-=1
#     for j in range(1,space+1):
#         print(" ",end=" ")
#         space+=1
#     print()
###########################################################
# A
# a b
# B C D
# c d e f

# first way
# n=4
# cha=65
# chi=97
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             if i%2==1:
#                 print(chr(cha),end=" ")
#                 cha+=1
#             else:
#                 print(chr(chi),end=" ")
#                 chi+=1
#         else:
#             print(" ",end=" ")
#     print()

# second way
# n=4
# cha=65
# chi=97
# num=1
# space=3
# for p in range(1,n+1):
#     for i in range(1,num+1):
#         if p%2==0:
#             print(chr(chi),end=" ")
#             chi+=1
#         else:
#             print(chr(cha),end=" ")
#             cha+=1
#     num+=1
#     for j in range(1, space+1):
#         print(" ",end=" ")
#     print()

##########################################################
# A A A A
#   B B B
#     C C
#       D
# n=4
# cha=65
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j>=i:
#             print(chr(cha),end=" ")
#         else:
#             print(" ",end=" ")
#     cha+=1
#     print()

# second ways
# n=4
# num=4
# cha=65
# space=0
# for k in range(1,n+1):
#     for i in range(1,space+1):
#         print(" ",end=" ")
#     space+=1
#     for j in range(1,num+1):
#         print(chr(cha),end=" ")
#     num-=1
#     cha+=1
#     print()

###########################################################################
# A
# 1 2
# B C D
# 3 4 5 6
# n=4
# num=1
# cha=65
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             if i%2==0:
#                 print(num,end=" ")
#                 num+=1
#             else:
#                 print(chr(cha),end=" ")
#                 cha+=1
#         else:
#             print(" ",end=" ")
#     print()

# n=4
# no=1
# cha=65
# num=1
# space=3
# for w in range(1,n+1):
#     for i in range(1,num+1):
#         if w%2==0:
#             print(no,end=" ")
#             no+=1
#         else:
#             print(chr(cha),end=" ")
#             cha+=1
#     num+=1
#     for j in range(1,space+1):
#         print(" ",end=" ")
#     space-=1
#     print()
##################################################################################
# A A A A
# 1 1 1
# B B
# 2
# n=4
# star=4
# space=0
# no=1
# ch=65
# for row in range(1,n+1):
#     for i in range(1, star+1):
#         if row%2==0:
#             print(no,end=" ")
#         else:
#             print(chr(ch),end=" ")
#     star-=1
#     if row%2==0:
#         no+=1
#     else:
#         ch+=1
#     for j in range(1,space+1):
#         print(" ",end=" ")
#     space+=1
#     print()
#################################################################################################


# wirte alphabate using *
# * * * * *
# *       * 
# * * * * *
# *       *
# *       *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or i==1 or i==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#########################################################

#   * * *
# *       *
# * * * * *
# *       *
# *       *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i>1 and j==1) or (i>1 and j==n) or (i==1 and (j>1 and j<n)) or (i==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
######################################################################################
# * * * * *
# *       *
# * * * * *
# *       *
# * * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or j == n or i == 1 or i == 3 or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#######################################################################################
# * * * *
# *       *
# * * * *
# *       *
# * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (j==1) or (i%2==0 and j==n) or (i==1 and j<n) or (i==3 and j<n) or (i==n and j<n):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
##########################################################################################
# * * * * *
# *
# *
# *
# * * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or i==1 or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
################################################3
#   * * * *
# *
# *
# *
#   * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if ((i>1 and i<n)and j==1) or (i==1 and j>1) or (i==n and j>1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#################################################################################
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or i==1 or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
##########################################################################3
# * * * *
# *       *
# *       *
# *       *
# * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or (i==1 and j<n) or (i>1 and j==n and i<n) or (i==n and j<n):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
####################################################################
# * * * * *
# *
# * * * * *
# *
# * * * * *
#
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or i==1 or i==3 or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
###################################################################
#   * * * *
# *
# * * * * *
# *
#   * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if ((i>1 and i<n)and j==1) or (i==1 and j>1) or (i==n and j>1) or i==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
###############################################################################3
# * * * * *
# *
# * * * * *
# *
# *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or i == 1 or i == 3 or i==3 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
############################################################################
#   * * *
# *
# * * * *
# *
# *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i>1 and j==1)or (i==1 and j>1 and j<n) or (i==3 and j<n) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#######################################3###################################
# *       *
# * *   * *
# *   *   *
# *       *
# *       *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or ((i==j) and (j<4)) or ((i+j)==6 and (i<3)) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#############################################################################3
# * * * *
# *     *
# *   * *
# * * * *
#         *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (j==1 and i<n)or (i==1 and j<n)or (j==4 and i<n) or (i==4 and j<n)or (i==j and j>=3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#################################################################################
#
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or i==3 or j==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==3 or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or i == 1 or i == 3 or i==3 or ((i>=1 and i<4) and j==n) or (i==j and j>2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or i==1 or i==3 or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print()
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or ((i==j) and (j==n)) or ((i+j)==6 and (i==n))or (i==j) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# *       *
# *       *
# * * * * *
# *       *
# *       *
#
# * * * * *
#     *
#     *
#     *
# * * * * *
#
# * * * * *
# *       *
# * * * * *
# *     *
# *       *
#
# * * * * *
# *
# * * * * *
# *
# * * * * *
#
# *       *
# * *     *
# *   *   *
# *     * *
# *       *