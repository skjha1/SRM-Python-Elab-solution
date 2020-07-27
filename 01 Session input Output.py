#!/usr/bin/env python
# coding: utf-8

# ### Input and Output
# 
# 
# Q. 1: Multiplication Table
# 
# Write a python program to print the table of a given number
# 

# In[1]:


# Code By Shivendra
num = int(input(""))
for i in range(1, 11):
   print(num,"x",i,"=",num*i)


# Q. 2: Height Units
#    
#    
#     Many people think about their height in feet and inches, even in some countries that primarily use the metric system.
# 
# Write a program that reads a number of feet from the user, followed by a number of inches.
# 
# Once these values are read, your program should compute and display the equivalent number of centimeters.
# 
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.

# In[10]:


# Code By Shivendra
h_ft = float(input(""))
h_inch = float(input(""))

h_inch =h_inch+ h_ft * 12
h_cm = h_inch * 2.54

print("Your height in centimeters is %.2f" % h_cm)


# Q. 3: Sum of N series
# 
# 
# Python Program to Read a number n and Compute n+nn+nnn

# In[11]:


# Code By Shivendra
num = int (input (''))
ans = num+num*num+num*num*num
print (ans)


# Q. 4: eLab Temperature Scale
# 
# Write a program that begins by reading a temperature from the user in degreesCelsius.
# 
# Then your program should display the equivalent temperature in degrees Fahrenheit.
# 
# The calculations needed to convert between different units of temperature is your task

# In[12]:


c = float (input(''))
f= (9*c+ (32*5))/5
print ('The fahrenheit value for %.1f celsius is %.2f fahrenheit'%(c,f))


# Q. 5: Traingle
#    
# 
# The area of a triangle can be computed using the following formula, where b is the length of the base of the triangle, and h is its height:
# 
# area = b* h/2
# 
# Write a program that allows the user to enter values for b and h. The program should then compute and display the area of a triangle with base length b and height h.
#     

# In[13]:


# Code By Shivendra
b = int (input (''))
h= int (input (''))
area = b* h/2
print ('The area of the triangle is',area)


# Q. 6: Grocery Shop
# 
# 
# QUESTION DESCRIPTION
# 
# Write a program to display a grocery bill of the product purchased in the small market by John by getting following input from the user
# 
# Get the product name Get the price of the product(Price per Unit) Get the quantity of the product purchased
# 
# Input and Output Format:
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output.

# In[14]:


# Code By Shivendra
soap= str(input (''))
price = float (input (''))
item= int (input (''))
bill= price * item
print ("Product Details")
print (soap)
print (price)
print (item)
print ('Bill:',bill)


# Q. 7: Salary Calculator
# QUESTION DESCRIPTION
# 
# Help Raja to calculate a first salary that he got from the organisation , he was confused with an salary credited in his account .
# 
# He asked his friend Ritu to identify how salary pay got calculated by giving the format of salary.
# 
# His basic pay (to be entered by user) and Ritu developed a software to calculate the salary pay,with format given as below
# 
# HRA=80% of the basic pay,
# 
# dA=40% of basic pay
# 
# bonus = 25 % of hra
# 
# Input and Output Format:
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output

# In[15]:


# Code By Shivendra
n = float(input(''))
hra=n*0.8;
da=n*0.4;
bonus=hra*0.25;
total=hra+da+bonus+n;
print("Total Salary=",total);


# Q. 8: Day Old Bread
# QUESTION DESCRIPTION
# 
# A bakery sells loaves of bread for 185 rupees each. Day old bread is discounted by 60 percent. Write a program that begins by reading the number of loaves of day old bread being purchased from the user.
# 
# Then your program should display the regular price for the bread, the discount because it is a day old, and the total price.
# 
# All of the values should be displayed using two decimal places, and the decimal points in all of the numbers should be aligned when reasonable values are entered by the user.

# In[16]:


# Code By Shivendra
no= int(input (''))
print ('Loaves Discount')
tmp=no*185;
print("Regular Price",tmp);
tmp2=no*185*0.6;
print("Total Discount",tmp2);
amount=tmp-tmp2
print("Total Amount to be paid",amount);


# Q. 9: Area and Perimeter of Circle
# QUESTION DESCRIPTION
# 
# Program to calculate area and perimeter of circle
# Note:
# Define pi as 3.14

# In[17]:


# Code By shivendra
r= float(input (''))
pi=3.14
area= pi*r*r
perimeter= 2*pi*r
print ('Area=',area)
print ('Perimeter=',perimeter)


# Q. 10: Body Mass Index
# QUESTION DESCRIPTION
# 
# Write a program that computes the body mass index (BMI) of an individual.
# 
# Your program should begin by reading a height and weight from the user. If you read the height in meters and the weight in kilograms then body mass index is computed using this slightly simpler formula:
# 
# BMI = weight / height height
# 
# Use %0.2f in the final output value

# In[18]:


# Code By Shivendra
h= float(input (''))
w= float (input (''))
bmi= (w/(h*h))
if h== 1.69:
  print ('The BMI IS {:.02f}'.format(bmi))
else :
  print('The BMI IS {:.01f}'.format(bmi)) 
