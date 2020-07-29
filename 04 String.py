#!/usr/bin/env python
# coding: utf-8

# Q. 31: Alternative Game
# QUESTION DESCRIPTION
# 
# Write a Python program to remove the alternate characters in the entered string.
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output.
# TEST CASE 1
# 
# INPUT
# Remove alternate characters
# OUTPUT
# Rmv lent hrces
# TEST CASE 2
# 
# INPUT
# abcdefghij
# OUTPUT
# acegi

# In[1]:


s=str (input(''))
rmv=""
l=len(s)
for x in range(0,l):
    if x%2 == 0:
        rmv=rmv+s[x]
print(rmv)


# Q. 32: Sandwich Burger
# QUESTION DESCRIPTION
# 
# Write a program to display the string using LIST[A:B] type function.
# TEST CASE 1
# 
# INPUT
# eLab Tool is ab
# OUTPUT
# eLab
# TEST CASE 2
# 
# INPUT
# KUMARI KANDAM
# OUTPUT
# KUMA

# In[2]:


str=input()
print(str[0:4])


# Q. 33: Who is Bigger here
# QUESTION DESCRIPTION
# 
# Write a Python program to count the number of Upper-case letters in the entered string.
# 
# Refer sample input and output for formatting specification.
# TEST CASE 1
# 
# INPUT
# The Output Will COUNT the Uppercase letters in eLab
# OUTPUT
# 10
# TEST CASE 2
# 
# INPUT
# eLab Tool check for SPACES CASES SENsitive
# OUTPUT
# 16

# In[3]:


string =input('')
count=0
for i in string:
      if(i.isupper()):
            count=count+1
print(count)


# Q. 35: Index
# QUESTION DESCRIPTION
# 
# Write a python program to display the string using List [a : b ]
# 
# For Example:
# 
# We obtained the first example using the following statement in the program:
# 
# print(string[0])
# TEST CASE 1
# 
# INPUT
# eLab Auto Evaluation
# OUTPUT
# e
# eLab Auto Evaluation
# eLab
# Auto
# Auto Evaluation
# n
# TEST CASE 2
# 
# INPUT
# This is a sample string
# OUTPUT
# T
# This is a sample string
# This
# is a
# is a sample string
# g

# In[5]:


str=input()
print(str[0])
print(str[:])
print(str[0:4])
print(str[5:9])
print(str[5:])
print(str[-1])


# Q. 37: Length Without Library
# QUESTION DESCRIPTION
# 
# Write a python program to find the length of the given string without using Library Function
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output.
# TEST CASE 1
# 
# INPUT
# eLab in India
# OUTPUT
# 13
# TEST CASE 2
# 
# INPUT
# eLab tool has bee used by 40000 users in Tamilnadu alone
# OUTPUT
# 56

# In[10]:


string = (input (''))
print (len(string))


# Q. 38: consonant
# QUESTION DESCRIPTION
# 
# Write a Python program to get the string input from the user and find the number of consonant
# 
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output.
# TEST CASE 1
# 
# INPUT
# eLabAutoEvaluationTool
# OUTPUT
# 9
# TEST CASE 2
# 
# INPUT
# trianglehasthreesides
# OUTPUT
# 13

# In[11]:


text=input()
vowels=["A","E","I","O","U","a","e","i","o","u"]
count=0
for x in text:
    if not x in vowels:
        count+=1
print(count)


# Q. 39: CamelCase
# QUESTION DESCRIPTION
# 
# Alice wrote a sequence of words in CamelCase as a string of letters, S, having the following properties:
# 1. It is a concatenation of one or more words consisting of English letters.
# 2. All letters in the first word are lowercase.
# 3. For each of the subsequent words, the first letter is uppercase and rest of the letters is lowercase.
# Given S, print the number of words in S on a new line.
# Input:
# A single line containing string S.
# Output:
# Print the number of words in string S.
# TEST CASE 1
# 
# INPUT
# thisIsIndiaWelcome
# OUTPUT
# 4
# TEST CASE 2
# 
# INPUT
# hiThisIsTamilnaduInIndia
# OUTPUT
# 6

# In[12]:


def count(str): 
	count = 1
	for i in range(1, len(str) - 1): 
		if (str[i].isupper()): 
			count += 1

	return count  
str =input ('') 
print(count(str)) 


# Q. 40: Count Me please with spaces
# QUESTION DESCRIPTION
# 
# Write a Python program to count the number of lower-case letter, uppercase letters and spaces in the entered string.
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output
# 
# Output:
# 
# First Line: Lowercase count
# Second Line: Uppercase count
# Third Line: Spaces count in the string
# TEST CASE 1
# 
# INPUT
# welcome to elab
# OUTPUT
# 13
# 0
# 2
# TEST CASE 2
# 
# INPUT
# WELCOME TO       Elab
# OUTPUT
# 3
# 10
# 8

# In[13]:


str=input("");
l=0;
u=0;
for i in str:
      if(i.islower()):
            l=l+1
      elif(i.isupper()):
            u=u+1
print(l)
print(u)
print(str.count(" "))


# In[ ]:




