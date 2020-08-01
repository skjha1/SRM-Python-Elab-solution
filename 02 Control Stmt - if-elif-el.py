#!/usr/bin/env python
# coding: utf-8

# ## Control Stmt - if-elif-el

# Q. 11: BMI
# QUESTION DESCRIPTION
# 
# Write a python program to find someone will have a risk of heart Disease using BMI and age .
# 
# AGE BMI RISK
# <45 <22 Low
# >45 <22 Medium
# <45 >22 Medium
# >=45 >=22 High
# TEST CASE 1
# 
# INPUT
# 44
# 21
# OUTPUT
# Low
# TEST CASE 2
# 
# INPUT
# 46
# 21
# OUTPUT
# Medium

# In[1]:


age = int(input(''))
bmi = int(input(''))
if(age <45 and bmi <22):
      print ("Low")
elif (age >45 and bmi <22):
      print ("Medium")
elif (age <45 and bmi >22):
      print ("Medium")
elif (age >=45 and bmi >=22):
      print("High")


# Q. 12: India Vs England 50-50 Match
# QUESTION DESCRIPTION
# 
# Virat Kohli has won the toss against England in a 50 Over World Cup Final 2019. During the Toss time the commentator have him a funny task to test his mathematical skills.
# 
# Shastri was the umpire to judge his mathematical skills. When the number is 28 he needs tell "INDIA" and when the number is 25 he needs to tell "ENGLAND".
# 
# Refer sample Input and Output:
# Input 1: 20 Output: INDIA
# Input 2: 21 Output: ENGLAND
# Input 3: 22 Output: INDIA
# 
# TEST CASE 1
# 
# INPUT
# 20
# OUTPUT
# INDIA
# TEST CASE 2
# 
# INPUT
# 21
# OUTPUT
# ENGLAND

# In[2]:


# Code By Shivendra
no=int ( input (''))
if no%2==0:
  print ('INDIA')
else :
  print ('ENGLAND')


# Q. 13: Grade
# QUESTION DESCRIPTION
# 
# Write a program asks the user to enter a exam score, and then prints the grade (A/B/C/D) that corresponds to the score.
# 
# If the score that the user entered is less than 0 or greater than 100, the program prints an error message.
# Use the following grades
# A grade >=85
# B grade 70-85
# C grade 50-70
# D grade <50
# TEST CASE 1
# 
# INPUT
# 85
# OUTPUT
# A
# TEST CASE 2
# 
# INPUT
# 78
# OUTPUT
# B

# In[3]:


score=int(input(""))
if(score>=85):
    print('A')
elif (score>=70 and score<85):
	print('B')
elif (score>=50 and score<70):
	print('C')
elif(score<50):
	print('D')


# Q. 14: Name of the Shape
# QUESTION DESCRIPTION
# 
# Write a program that determines the name of a shape from its number of sides.
# 
# Read the number of sides from the user and then report the appropriate name as part of a meaningful message.
# 
# Your program should support shapes with anywhere from 3 up to (and including) 6sides.
# 
# If a number of sides outside of this range is entered then your program should display an appropriate error message.
# 
# 1. If the input is 5 then display as Pentagon
# 
# 2. if the input is 6 display as Hexagon
# 
# 3.if the input is any another number then display the message "Input should be from 3 to 6"
# TEST CASE 1
# 
# INPUT
# 3
# OUTPUT
# Triangle
# TEST CASE 2
# 
# INPUT
# 4
# OUTPUT
# Quadrilateral

# In[4]:


n = int(input())
if n == 3:
    print("Triangle")
elif n == 4:
    print("Quadrilateral")
elif n == 5:
    print("Pentagon")
elif n == 6:
    print("Hexagon")


# Q. 15: Find Year
# QUESTION DESCRIPTION
# 
# Most years have 365 days. However, the time required for the Earth to orbit the Sun is actually slightly more than that. As a result, an extra day, February 29, is included in some years to correct for this difference. Such years are referred to as leap years.
# 
# The rules for determining whether or not a year is a leap year follow:
# 
# Any year that is divisible by 400 is a leap year.
# Of the remaining years, any year that is divisible by 100 is not a leap year.
# Of the remaining years, any year that is divisible by 4 is a leap year.
# All other years are not leap years.
# 
# Write a program that reads a year from the user and displays a message indicating
# whether or not it is a leap year.
# TEST CASE 1
# 
# INPUT
# 2016
# OUTPUT
# 2016 is a leap year
# TEST CASE 2
# 
# INPUT
# 2001
# OUTPUT
# 2001 is not a leap year

# In[5]:


# Code by shivendra
year= int (input(''))
if (((year % 4 == 0) and (year % 100!= 0)) or (year%400 == 0)):
  print (year,'is a leap year')
else :
  print (year,'is not a leap year')


# Q. 16: Mirror Image
# QUESTION DESCRIPTION
# 
# Puck, the trickster, has again started troubling people in your city.
# 
# The people have turned on to you for getting rid of Puck. Puck presents to you a number consisting of numbers from 0 to 9 characters.
# 
# He wants you to reverse it from the final answer such that the number becomes Palindrome number.
# 
# A Palindrome is a number which equals its reverse. The hope of people are on you so you have to solve the riddle.
# 
# You have to tell if some number exists which you would reverse to convert the number into palindrome.
# TEST CASE 1
# 
# INPUT
# 2112
# OUTPUT
# Palindrome
# TEST CASE 2
# 
# INPUT
# 2001
# OUTPUT
# Not a Palindrome

# In[6]:


n = int(input(''))
temp = n
rev = 0

while n:
    rev*=10
    rev+=n%10
    n/=10
    n=int(n)

if rev==temp:
    print("Palindrome")
else:
    print("Not a Palindrome")


# Q. 17: Indian Zodiac
# QUESTION DESCRIPTION
# 
# The indian zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is shown in the table below. The pattern repeats from there, with 2012 being another year of the dragon, and 1999 being another year of the hare. 2000 Dragon
# 2001 Snake
# 2002 Horse
# 2003 Sheep
# 2004 Monkey
# 2005 Rooster
# 2006 Dog
# 2007 Pig
# 2008 Rat
# 2009 Ox
# 2010 Tiger
# 2011 Hare
# Write a program that reads a year from the user and displays the animal associated with that year. Your program should work correctly for any year greater than or equal to zero, not just the ones listed in the table.
# TEST CASE 1
# 
# INPUT
# 1998
# OUTPUT
# Tiger
# TEST CASE 2
# 
# INPUT
# 2017
# OUTPUT
# Rooster

# In[7]:


year=int(input(""))
if (year % 12 == 8):
    animal="Dragon"
elif (year % 12 ==9):
    animal="Snake"
elif (year % 12==10):
    animal="Horse"
elif (year % 12== 11):
    animal="Sheep"
elif (year % 12== 0):
    animal="Monkey"
elif (year % 12==1):
    animal="Rooster"
elif (year % 12==2):
    animal="Dog"
elif (year % 12==3):
	animal="Pig"
elif (year % 12==4):
	animal="Rat"
elif (year%12==5):
    animal="Ox"
elif (year%12==6):
    animal="Tiger"
else:
    animal="Hare"
print(animal)


# Q. 18: Check Number
# QUESTION DESCRIPTION
# 
# Write a python program to check whether a given number is positive /Negative or Zero
# TEST CASE 1
# 
# INPUT
# -5
# OUTPUT
# Negative

# In[8]:


n = int(input())
if n < 0:
    print("Negative")
elif n > 0:
    print("Positive")
elif n ==0:
    print("Zero")


# Q. 19: Game of Digits
# QUESTION DESCRIPTION
# 
# Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number. For example, if the user enters 3141 then your program should display 3+1+4+1=9.
# TEST CASE 1
# 
# INPUT
# 9091972
# OUTPUT
# The total sum of digits is: 37
# TEST CASE 2
# 
# INPUT
# 25121988
# OUTPUT
# The total sum of digits is: 36

# In[9]:


n=int(input())
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)


# Q. 20: India National Holidays
# QUESTION DESCRIPTION
# 
# Date to Holiday Name
# 
# India has three national holidays which fall on the same dates each year.
# 
# Holiday Date
# New Year January 1
# Independence Day August 15
# Republic DayJanuary 26
# 
# Write a program that reads a month and day from the user. If the month and day match one of the holidays listed previously then your program should display the holidays name.
# 
# Otherwise your program should indicate that the entered month and day do not correspond to a fixed-date holiday.
# 
# India has two additional national holidays, Good Friday and Labour Day, whose dates vary from year to year. There are also numerous provincial and territorial holidays, some of which have fixed dates, and some of which have variable dates.
# 
# We will not consider any of these additional holidays in this exercise.
# TEST CASE 1
# 
# INPUT
# January
# 1
# OUTPUT
# New Year
# TEST CASE 2
# 
# INPUT
# April
# 14
# OUTPUT
# Sorry No National Holidays

# In[10]:


mth=input('');
dt=int(input(''));
if (mth=='January') and (dt==1):
    print('New Year')
elif (mth=='August') and (dt==15):
    print('Independence Day')
elif (mth=='January') and (dt==26):
    print('Republic Day')
else:
    print('Sorry No National Holidays')	

---------------------------------------------------------------------------------------------
# "Q. 30: Game of Digits
#QUESTION DESCRIPTION

#Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number. For example, if the user enters 3141 then your program should display 3+1+4+1=9.
#TEST CASE 1

#INPUT
#9091972
#OUTPUT
#The total sum of digits is: 37
#TEST CASE 2

#INPUT
#25121988
#OUTPUT
#The total sum of digits is: 36 -m "

n=int(input(""))
num=0
while n>0:
      dig=n%10
      num=num+dig
      n=int(n/10)
print('The total sum of digits is:',num)
