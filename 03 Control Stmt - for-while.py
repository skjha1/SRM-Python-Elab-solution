#!/usr/bin/env python
# coding: utf-8

# ## SESSION: Control Stmt - for-while
# Q. 21: Star Pattern 1
# QUESTION DESCRIPTION
# 
# Write a program to print the star pattern
# 
# Input:Number of rows
# 
# Output:Star pattern
# 
# Refer sample input and output for formatting specification.
# TEST CASE 1
# 
# INPUT
# 5
# OUTPUT
# *****
# ****
# ***
# **
# *
# TEST CASE 2
# 
# INPUT
# 7
# OUTPUT
# *******
# ******
# *****
# ****
# ***
# **
# *
# Q. 21: Star Pattern 1
# QUESTION DESCRIPTION
# 
# Write a program to print the star pattern
# 
# Input:Number of rows
# 
# Output:Star pattern
# 
# Refer sample input and output for formatting specification.
# TEST CASE 1
# 
# INPUT
# 5
# OUTPUT
# *****
# ****
# ***
# **
# *
# TEST CASE 2
# 
# INPUT
# 7
# OUTPUT
# *******
# ******
# *****
# ****
# ***
# **
# *

# In[7]:


a= int (input (''))
for i in range (1,a+1):
    for j in range (i,a+1):
        print ('*',end='')
    print ('')


# Q. 22: Exponentation- Part B
# QUESTION DESCRIPTION
# 
# Write a program to find the exponentation of given number
# 
# Input 1: Base
# Input 2: Number of inputs
# 
# Output:
# List of exponentation terms for the given input
# TEST CASE 1
# 
# INPUT
# 2
# 5
# OUTPUT
# The total terms is: 5
# 1
# 2
# 4
# 8
# 16
# 32
# TEST CASE 2
# 
# INPUT
# 5
# 5
# OUTPUT
# The total terms is: 5
# 1
# 5
# 25
# 125
# 625
# 3125

# In[8]:


a= int (input (''))
b=int (input (''))
print ('The total terms is:',b)
for i in range (b+1):
    print (a**i)


# Q. 23: palindrome
# QUESTION DESCRIPTION
# 
# The program takes a number and checks whether it is a palindrome or not .DESCRIPTION:
# 1. Take the value of the integer and store in a variable.
# 2. Transfer the value of the integer into another temporary variable.
# 3. Using a while loop, get each digit of the number and store the reversed number in another variable.
# 4. Check if the reverse of the number is equal to the one in the temporary variable.
# 5. Print the final result.
# 6. Exit.
# TEST CASE 1
# 
# INPUT
# 33
# OUTPUT
# palindrome
# TEST CASE 2
# 
# INPUT
# 345
# OUTPUT
# not a palindrome

# In[11]:


n = int(input(''))
temp = n
rev = 0

while n:
    rev*=10
    rev+=n%10
    n/=10
    n=int(n)

if rev==temp:
    print("palindrome")
else:
    print("not a palindrome")


# Q. 24: Check Armstrong
# QUESTION DESCRIPTION
# 
# Write a program to check whether the given number is a armstrong number or not
# 
# Input :Positive Number
# 
# Output: Yes or No
# 
# Refer sample input and output for formatting specification.
# TEST CASE 1
# 
# INPUT
# 153
# OUTPUT
# Yes
# TEST CASE 2
# 
# INPUT
# 123
# OUTPUT
# No

# In[12]:


n=int(input(""))
n1=n
sum=0
while(n1>0):
	ne=n1 % 10
	sum+=(ne ** 3)
	n1=int(n1 / 10)
if(sum==n):
	print('Yes')
else:
    print('No')


# Q. 25: Sum on n number
# QUESTION DESCRIPTION
# 
# Write a program to find the sum of numbers
# Input 1:Negative number
# 
# Output:
# Display the appropriate error message
# 
# Input 2: Positive number
# 
# Output:
# Display the sum
# 
# Refer sample input and output for formatting specification.
# TEST CASE 1
# 
# INPUT
# -1
# OUTPUT
# Enter a positive number
# TEST CASE 2
# 
# INPUT
# 10
# OUTPUT
# The sum is 55

# In[13]:


n=int(input(''))
s=0
status = True
if n < 0:
    print("Enter a positive number")
else:
    for i in range(1,n+1):
        s=s+i
    print("The sum is",s)


# Q. 26: Strong Number
# QUESTION DESCRIPTION
# 
# Write a program to check whether the given number is Strong number or not
# 
# Input:Positive number
# 
# Output:Display the appropriate message
# 
# Refer sample input and output for formatting specification.
# TEST CASE 1
# 
# INPUT
# 145
# OUTPUT
# The number is a strong number
# TEST CASE 2
# 
# INPUT
# 2509
# OUTPUT
# The number is not a strong number

# In[14]:


sum1=0
num=int(input(''))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")


# Q. 27: Sum of Even and Odd
# QUESTION DESCRIPTION
# 
# Write a program to calculate the sum of even and odd numbers including its count.
# 
# Input:
# 1.Total number of Inputs
# 2. Input elements
# 
# Output:
# 1. Odd numbers count
# 2. Even numbers count
# 3. Sum of even numbers
# 4. Sum of odd numbers
# TEST CASE 1
# 
# INPUT
# 10
# 2
# 4
# 6
# 8
# 10
# 1
# 3
# 5
# 7
# 9
# OUTPUT
# 5
# 5
# 30
# 25
# TEST CASE 2
# 
# INPUT
# 9
# 2
# 4
# 6
# 8
# 10
# 1
# 3
# 5
# 7
# OUTPUT
# 4
# 5
# 30
# 16

# In[17]:


evenno=[]
oddno=[]
sum=[0,0]
num=int(input())
while num>0:
    ip=int(input())
    if ip%2==0:
        evenno.append(ip)
        sum[0]+=ip
    else:
        oddno.append(ip)
        sum[1]+=ip
    num-=1
print(len(oddno))
print(len(evenno))
print(str(sum[0])+'\n'+str(sum[1]))


# Q. 28: Perfect Number
# QUESTION DESCRIPTION
# 
# Write a program to check whether the given number is perfect number or not
# 
# Input:A positive number
# 
# Output:Display the appropriate message
# 
# Refer sample input and output for formatting specification.
# TEST CASE 1
# 
# INPUT
# 144
# OUTPUT
# The number is not a Perfect number
# TEST CASE 2
# 
# INPUT
# 6
# OUTPUT
# The number is a Perfect number

# In[18]:


n = int(input())
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")


# Q. 29: Positive Odd
# QUESTION DESCRIPTION
# 
# Write a program to find the sum of positive odd numbers
# 
# Input:Positive and negative numbers
# 
# Output:Display Sum of positive odd numbers.
# 
# Refer sample input and output for formatting specification.
# TEST CASE 1
# 
# INPUT
# 5
# 10
# -10
# 43
# 45
# 46
# OUTPUT
# Sum of positive odd numbers: 88
# TEST CASE 2
# 
# INPUT
# 7
# 10
# -10
# 43
# 45
# 46
# 30
# 31
# OUTPUT
# Sum of positive odd numbers: 119

# In[20]:


s=0
n=int(input(''))
i=1
num=0
while i <= n:
    num=int(input(''))
    i=i+1
 
    if num>0 and (num%2==1):
        s=s+num
print("Sum of positive odd numbers:",s)


# In[21]:

#Q. 23: Sets
#QUESTION DESCRIPTION

#Write a program to do basic set operations

#Input:Two Sets

#Output:
#Result of Union,intersection,difference and symmetric difference operations on the given input

#Refer sample input and output for formatting specification.
#TEST CASE 1

#INPUT
#8
#5
#0
#1
#2
#3
#4
#5
#6
#8
#1
#2
#3
#4
#5
#OUTPUT
#[0, 1, 2, 3, 4, 5, 6, 8]
#[1, 2, 3, 4, 5]
#Union is: {0, 1, 2, 3, 4, 5, 6, 8}
#Intersection is {1, 2, 3, 4, 5}
#Difference is {0, 6, 8}

l={8,5,0,1,2,3,4,5,6,8}
r={1,2,3,4,5}
print(list(l))
print(list(r))
print("Union is:",l|r)
print("Intersection is",l&r)
print("Difference is",l^r)

#In []:


