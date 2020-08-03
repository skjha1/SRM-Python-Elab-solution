#!/usr/bin/env python
# coding: utf-8

# Q. 71: Display Values
# QUESTION DESCRIPTION
# 
# Write a program to display only the values of the keys in the output
# 
# Input:
# 
# 1.Get two dictionaries key-value elements
# 
# Output:
# 1. Display the first dictionary
# 2. Display the second dictionary
# 3. Display the concatenated dictionary
# 4. Display the values of the concatenated dictionary
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output
# TEST CASE 1
# 
# INPUT
# 1
# 111
# 2
# 222
# OUTPUT
# First Dictionary
# {1: 111}
# Second Dictionary
# {2: 222}
# Concatenated dictionary is
# {1: 111, 2: 222}
# The Values of Dictionary
# [111, 222]
# TEST CASE 2
# 
# INPUT
# 3
# 333
# 4
# 444
# OUTPUT
# First Dictionary
# {3: 333}
# Second Dictionary
# {4: 444}
# Concatenated dictionary is
# {3: 333, 4: 444}
# The Values of Dictionary
# [333, 444]

# In[ ]:


d1={};
d2={};
d3={};
x=int(input());
d1[x]=int(input());
y=int(input());
d2[y]=int(input());
d3.update(d1);
d3.update(d2);
print("First Dictionary");
print(d1);
print("Second Dictionary");
print(d2);
print("Concatenated dictionary is");
print(d3);
print("The Values of Dictionary");
x=[];
for i in d3.values():
    x.append(i);
print(x);


# Q. 72: Has Keys
# QUESTION DESCRIPTION
# 
# Write a program to check whether the given key is present in the dictionary.
# 
# If the key is present then display the value of the entered key and if the key is not present then display the appropriate message
# 
# Input:
# 
# 1.Get size of the dictionary
# 2. Get the key-value elements
# 3. Get the key to be searched
# 
# Output:
# 1. Display the dictionary
# 2. Print either True or False
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output
# TEST CASE 1
# 
# INPUT
# 2
# 25
# 20
# 1252
# 1120
# 20
# OUTPUT
# The dictionary is
# {25: 1252, 20: 1120}
# True
# TEST CASE 2
# 
# INPUT
# 3
# 25
# 20
# 9
# 1252
# 1120
# 9009
# 11
# OUTPUT
# The dictionary is
# {25: 1252, 20: 1120, 9: 9009}
# False

# In[ ]:


n=int(input());
m=n;
k=n;
x=[];
d={};
while(n>0):
    a=int(input());
    x.append(a);
    n-=1;
i=0;
while(m>0):
    d[x[i]]=int(input());
    i+=1;
    m=m-1;
g=int(input());
print("The dictionary is");
print(d);
if(g in d.keys()):
    print("True");
else:
    print("False");


# Q. 73: Display Values
# QUESTION DESCRIPTION
# 
# Write a program to display only the values of the keys in the output
# 
# Input:
# 
# 1.Get two dictionaries key-value elements
# 
# Output:
# 1. Display the first dictionary
# 2. Display the second dictionary
# 3. Display the concatenated dictionary
# 4. Display the values of the concatenated dictionary
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output
# TEST CASE 1
# 
# INPUT
# 1
# 111
# 2
# 222
# OUTPUT
# First Dictionary
# {1: 111}
# Second Dictionary
# {2: 222}
# Concatenated dictionary is
# {1: 111, 2: 222}
# The Values of Dictionary
# [111, 222]
# TEST CASE 2
# 
# INPUT
# 3
# 333
# 4
# 444
# OUTPUT
# First Dictionary
# {3: 333}
# Second Dictionary
# {4: 444}
# Concatenated dictionary is
# {3: 333, 4: 444}
# The Values of Dictionary
# [333, 444]

# In[ ]:


d1={};
d2={};
d3={};
x=int(input());
d1[x]=int(input());
y=int(input());
d2[y]=int(input());
d3.update(d1);
d3.update(d2);
print("First Dictionary");
print(d1);
print("Second Dictionary");
print(d2);
print("Concatenated dictionary is");
print(d3);
print("The Values of Dictionary");
x=[];
for i in d3.values():
    x.append(i);
print(x);


# Q. 74: Print the dictionary
# QUESTION DESCRIPTION
# 
# Write a program to get the input of key and value of the element in dictionary.
# 
# Display the key-value pair in the python dictionary format.
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output.
# TEST CASE 1
# 
# INPUT
# 25
# 75
# OUTPUT
# Updated dictionary is:
# {25: 75}
# TEST CASE 2
# 
# INPUT
# 2017
# 2019
# OUTPUT
# Updated dictionary is:
# {2017: 2019}

# In[ ]:


d=dict()
for x in range(0,2):
    d[x]=int(input(""))
print("Updated dictionary is:")
print("{%d: %d}" %(d[0],d[1]))


# Q. 75: Display Items
# QUESTION DESCRIPTION
# 
# Write a program to get four dictionary items and display all the key-values format using update function and items() function
# TEST CASE 1
# 
# INPUT
# 10
# -10
# 20
# -20
# 30
# -30
# 40
# -40
# OUTPUT
# [(10, -10)]
# [(20, -20)]
# [(30, -30)]
# [(40, -40)]
# TEST CASE 2
# 
# INPUT
# 20
# 200
# 10
# 100
# 30
# 300
# 40
# 400
# OUTPUT
# [(20, 200)]
# [(10, 100)]
# [(30, 300)]
# [(40, 400)]

# In[ ]:


for i in range(4):
    l =[]
    t =()
    for j in range(2):
        t = t + (int(input()),)
    l.append(t)
    print(l)


# Q. 76: Update the Dictionary
# QUESTION DESCRIPTION
# 
# Write a program to update the Dictionary. Define the dictionary in the program and update the values as given in the program
# 
# The Dictionary is as follows
# dict = {'Toolname': 'eLab', 'Launch': 2017, 'State: 'Tamilnadu', 'Country':'Ind'}
# 
# Input:
# 
# 1. Get the key that needs to be updated
# 
# 2. The value that needs to be updated
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output
# TEST CASE 1
# 
# INPUT
# Toolname
# ELAB
# OUTPUT
# eLab
# 2017
# Tamilnadu
# Ind
# ELAB
# TEST CASE 2
# 
# INPUT
# Country
# India
# OUTPUT
# eLab
# 2017
# Tamilnadu
# Ind
# India

# In[ ]:


dict = {'Toolname': 'eLab','Launch': 2017, 'State': 'Tamilnadu', 'Country':'Ind'}
k = input()
v = input()
for e in dict.values():
    print(e)
dict[k]=v
print(v)


# Q. 77: Dictionary Using List
# QUESTION DESCRIPTION
# 
# Write a program to get the input of key and value of the element in dictionary.
# 
# Display the key-value pair in the python dictionary format.
# 
# Kindle get the input using List Concept.
# 
# Input:
# 1. Size of first list
# 2. Elements of first list
# 3. Size of second list
# 4. Elements of second list
# 
# Output:
# 1. The first list elements are keys of the dictionaries
# 2. The second list elements are corresponding elements of the dictionaries
# TEST CASE 1
# 
# INPUT
# 2
# 12
# 14
# 2
# 1212
# 1414
# OUTPUT
# {12: 1212, 14: 1414}
# TEST CASE 2
# 
# INPUT
# 2
# 4
# 5
# 2
# 16
# 25
# OUTPUT
# {4: 16, 5: 25}

# In[ ]:


d1=[]
d2=[]
d3={}
x=int (input (''))
for i in range (x):
  a=int (input ())
  d1.append(a)
y =int (input ())
for i in range (y):
  a=int (input ())
  d2.append(a)
for i in range (x):
  d3[d1[i]]=d2[i]
print (d3)


# Q. 78: List to Directory
# QUESTION DESCRIPTION
# 
# Write the python program which takes two lists and maps two lists into a dictionary
# TEST CASE 1
# 
# INPUT
# 3
# 1 2 3
# 1 4 9
# OUTPUT
# The dictionary is:
# {1: 1, 2: 4, 3: 9}
# TEST CASE 2
# 
# INPUT
# 2
# 23 46
# 69 138
# OUTPUT
# The dictionary is:
# {23: 69, 46: 138}

# In[ ]:


no= int (input ())
a= input().split()
b=input ().split()
l=list(map(int,a))
m=list(map(int,b))
color_dic=dict(zip(l,m))
print ('The dictionary is:')
print (color_dic)


# Q. 79: Length of Dictionary
# QUESTION DESCRIPTION
# 
# Write a program to get the input of key and value of the element in dictionary.
# 
# Display the key-value pair in the python dictionary format and find the length of the dictionary
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output.
# TEST CASE 1
# 
# INPUT
# 3
# 23
# 33
# 43
# 32
# 33
# 34
# OUTPUT
# The dictionary is
# {23: 32, 33: 33, 43: 34}
# Length of dictionary is
# 3
# TEST CASE 2
# 
# INPUT
# 4
# 23
# 33
# 43
# 53
# 32
# 33
# 34
# 35
# OUTPUT
# The dictionary is
# {23: 32, 33: 33, 43: 34, 53: 35}
# Length of dictionary is
# 4

# In[ ]:


dic1=[]
dic2=[]
dic3={}
x=int (input ())
for i in range (x):
  m=int (input ())
  dic1.append(m)
for i in range (x):
  m= int (input())
  dic2.append(m)

for i in range (x):
  dic3[dic1[i]]=dic2[i];
print("The dictionary is")
print(dic3)
print("Length of dictionary is"),
print(len(dic3))


# Q. 80: Compare Dictionary
# QUESTION DESCRIPTION
# 
# Write a program to get the input of key and value of the element in dictionary.
# 
# Display the key-value pair of the dictionary in the python dictionary format.
# 
# Compare the dictionary in the following sequence:
# 
# 1. First and Second Dictionary
# 2. Second and Third Dictionary
# 3.Third and Fourth Dictionary
# 4.Fourth and First Dictionary
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output.
# TEST CASE 1
# 
# INPUT
# 23
# 33
# 43
# 53
# 32
# 33
# 34
# 35
# OUTPUT
# First Dictionary
# {23: 33}
# Second Dictionary
# {43: 53}
# Third Dictionary
# {32: 33}
# Fourth Dictionary
# {34: 35}
# -1
# 1
# -1
# 1
# TEST CASE 2
# 
# INPUT
# 53
# 93
# 33
# 43
# 2
# 10
# 3
# 35
# OUTPUT
# First Dictionary
# {53: 93}
# Second Dictionary
# {33: 43}
# Third Dictionary
# {2: 10}
# Fourth Dictionary
# {3: 35}
# 1
# 1
# -1
# -1

# In[ ]:


dict={}
dict1={}
dict2={}
dict3={}
a=[]
b=[]
print('First Dictionary')
for i in range(1):
 key=int(input())
 value=int(input())
 a.append(value)   
 dict[key]=value   
print(dict)
print('Second Dictionary')
for i in range(1):
 key=int(input())
 value=int(input())
 b.append(value) 
dict1[key]=value   
print(dict1)
print('Third Dictionary')
for i in range(1):
 key=int(input())
 value=int(input())
 b.append(value) 
dict2[key]=value   
print(dict2)
print('Fourth Dictionary')
for i in range(1):
 key=int(input())
 value=int(input())
 b.append(value) 
dict3[key]=value   
print(dict3)
if(list(dict.keys())[0]>list(dict1.keys())[0]):
   print(1)
else:
    print(-1)
if(list(dict1.keys())[0]>list(dict2.keys())[0]):
    print(1)
else:
    print(-1)
if(list(dict2.keys())[0]>list(dict3.keys())[0]):
    print(1)
else:
    print(-1)
if(list(dict3.keys())[0]>list(dict.keys())[0]):
    print(1)
else:
    print(-1)


# In[ ]:




