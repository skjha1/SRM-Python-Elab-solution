#!/usr/bin/env python
# coding: utf-8

# Q. 41: LCM Check
# QUESTION DESCRIPTION
# 
# Write a python function to calculate the LCM of numbers
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output
# TEST CASE 1
# 
# INPUT
# 5
# 3
# OUTPUT
# LCM is: 15
# TEST CASE 2
# 
# INPUT
# 15
# 20
# OUTPUT
# LCM is: 60

# In[4]:


num1= int (input ())
num2= int (input ())
def gcd (num1,num2):
    
    while num2>0:
        num1,num2=num2,num1%num2
    return num1

def lcm (num1,num2):
    
    return num1*num2/gcd(num1,num2)

print("LCM is:",round(lcm(num1,num2)))


# Q. 43: Gravitational Force
# QUESTION DESCRIPTION
# 
# Python Program to Find the Gravitational Force Acting Between Two Objects
# 
# Input
# 
# First Line :Value of first mass
# Second Line:Value second mass
# Third Line: Distance between the centres of the masses
# TEST CASE 1
# 
# INPUT
# 1000000
# 500000
# 20
# OUTPUT
# 0.08 N
# TEST CASE 2
# 
# INPUT
# 90000000
# 7000000
# 20
# OUTPUT
# 105.1 N

# In[6]:


m1=float(input(""));
m2=float(input(""));
r=float(input(""));
G=6.673*(10**-11)
f=(G*m1*m2)/(r**2)
print(round(f,2),"N")


# Q. 44: Solve Equation
# QUESTION DESCRIPTION
# 
# Python Program to Find the Sum of the Series: 1 + 1/2 + 1/3 + .. + 1/N
# 
# Input:
# 
# The number of terms
# 
# Output
# 
# Print the Sum of Series
# TEST CASE 1
# 
# INPUT
# 7
# OUTPUT
#  2.59
# TEST CASE 2
# 
# INPUT
# 15
# OUTPUT
# 3.32

# In[7]:


n=int(input(""))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print(round(sum1,2))


# Q. 45: Perfect Number
# QUESTION DESCRIPTION
# 
# Write a Python Program to Check if a Number is a Perfect Number
# TEST CASE 1
# 
# INPUT
# 6
# OUTPUT
# The number is a Perfect number!
# TEST CASE 2
# 
# INPUT
# 25
# OUTPUT
# The number is not a Perfect number!

# In[8]:


n = int(input(""))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")


# Q. 46: Taxi Fare
# QUESTION DESCRIPTION
# 
# In a particular jurisdiction in India after implementing GST the taxi fares are altered. Taxi fares consist of a base fare of 200 and GST tax as 4% of base fare for every 140 meters traveled. Write a function that takes the distance traveled (in kilometers) as its only parameter and returns the total fare as its only result. Write a main program that demonstrates the function.
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output
# TEST CASE 1
# 
# INPUT
# 25
# OUTPUT
# 1628.57
# TEST CASE 2
# 
# INPUT
# 225
# OUTPUT
# 13057.14

# In[9]:


base_fare=200
GST_rate=8
def fare(kms):
    meters=kms*1000
    cost_calculate=meters/140
    tax=cost_calculate*GST_rate
    total=base_fare+tax
    print(round(total,2))
def main():
    kms=int(input(""))
    fare(kms)
main()


# Q. 47: Check My Password
# QUESTION DESCRIPTION
# 
# In this exercise you will write a function that determines whether or not a password is good. We will define a good password to be a one that is at least 8 characters long and contains at least one uppercase letter, at least one lowercase letter, and at least one number,one Special character.
# 
# Your function should return true if the password passed to it as its only parameter is good.
# 
# Otherwise it should return false. Include a main program that reads a password from the user and reports whether or not it is good.
# 
# Ensure that your main program only runs when your solution has not been imported into another file.
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output
# TEST CASE 1
# 
# INPUT
# eLabTool2017#
# OUTPUT
# Good Password
# TEST CASE 2
# 
# INPUT
# elabtool2017
# OUTPUT
# Try Again

# In[10]:


import re

def passwordv(strw):
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    result = re.findall(pattern, strw)
    if (result):
        print( "Good Password")
    else:
        print ("Try Again")

strw= input()
passwordv(strw)


# Q. 48: Prime Numbers
# QUESTION DESCRIPTION
# 
# Python Program to Print all the Prime Numbers within a Given Range
# 
# Input :
# 
# Upper Limit
# 
# Output :
# 
# Print the prime numbers within the specified limit
# TEST CASE 1
# 
# INPUT
# 15
# OUTPUT
# 2
# 3
# 5
# 7
# 11
# 13
# TEST CASE 2
# 
# INPUT
# 40
# OUTPUT
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37

# In[11]:


upper = int(input(""));
for num in range(2,upper):
    for i in range(2,num):
       if (num % i) == 0:
               break
    else:
       print(num)


# Q. 49: Grade System
# QUESTION DESCRIPTION
# 
# Write a python function to calculate the GRADE systems of marks
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output
# 
# Input :
# Input 5 numbers
# 
# Output:
# 
# 1. If the average is above 90 then print Grade as "A" (Hint : 90 and above)
# 2. If the average is above 70 and less than 90 then print Grade as "B" (Hint: 71-89)
# 3. If the average is above 50 and less than 70 then print Grade as "C"(Hint: 51-70)
# 4. If the average is 50 or less then then print as "D"
# TEST CASE 1
# 
# INPUT
# 99
# 98
# 87
# 99
# 90
# OUTPUT
# Grade:A
# TEST CASE 2
# 
# INPUT
# 71
# 77
# 67
# 89
# 89
# OUTPUT
# Grade:B

# In[12]:


a=int(input(''))
b=int(input(''))
c=int(input(''))
d=int(input(''))
e=int(input(''))
avg=(a+b+c+d+e)/5
print("Grade:",end="")
if (avg>90):
	grade='A'
elif (avg>70):
	grade='B'
elif avg>50:
	grade='C'
elif avg<=50 :
	grade='D'
print(grade)


# Q. 50: GCD Check
# QUESTION DESCRIPTION
# 
# Write a python function to calculate the GCD of numbers
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output
# TEST CASE 1
# 
# INPUT
# 15
# 5
# OUTPUT
# The GCD of the two numbers is 5
# TEST CASE 2
# 
# INPUT
# 81
# 9
# OUTPUT
# The GCD of the two numbers is 9

# In[13]:


import fractions
a=int(input(""))
b=int(input(""))
print("The GCD of the two numbers is",fractions.gcd(a,b))

