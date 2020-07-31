#!/usr/bin/env python
# coding: utf-8

# Q. 51: Number and Square
# QUESTION DESCRIPTION
# 
# Python Program to create a list of tuples with the first element as the number and the second element as the square of the number
# 
# Input:
# First Line: Lower Range
# Second Line:Upper Range
# 
# Output:
# Print the List of Values With the number and the square of that number.
# TEST CASE 1
# 
# INPUT
# 1
# 4
# OUTPUT
# (1 1) (2 4) (3 9) (4 16)
# TEST CASE 2
# 
# INPUT
# 45
# 49
# OUTPUT
# (45 2025) (46 2116) (47 2209) (48 2304)  (49 2401)

# In[ ]:


l_range=int(input(""))
u_range=int(input(""))
a=[(x) for x in range(l_range,u_range+1)]
b=[(x*x) for x in range(l_range,u_range+1)]
c=len(a)
for x in range(c):
	if(x<c and x!=3):
		print("(%d %d)" %(a[x],b[x]),end=" ")
	if(x==3):
		print("(%d %d)" %(a[x],b[x]),end="  ")    


# Q. 52: Remove Duplicate Elements from the List
# QUESTION DESCRIPTION
# 
# Write a program to eliminate the duplicate elements in the list
# 
# Input:
# 
# 1. The Size of List
# 2. The List elements
# 
# Output:
# Non-duplicate elements
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output.
# TEST CASE 1
# 
# INPUT
# 8
# 25
# 20
# 23
# 9
# 25
# 23
# 19
# 21
# OUTPUT
# Non-duplicate items
# [25, 20, 23, 9, 19, 21]
# TEST CASE 2
# 
# INPUT
# 5
# 25
# 20
# 23
# 9
# 25
# OUTPUT
# Non-duplicate items
# [25, 20, 23, 9]

# In[ ]:


a=[]
n=int(input())
for x in range(0,n):
    element=int(input())
    a.append(element)
b=set()
unique=[]
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non-duplicate items")
print(unique)


# Q. 53: Reverse
# QUESTION DESCRIPTION
# 
# Write a program to add the list and display the list in the reverse order
# 
# Input:
# 
# 1. The size of the first list
# 2. The size of the second list
# 3. The List elements of first and second list
# 
# Output:
# 
# 1. The appended or extended list
# 2. The reverse list
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
# 3
# 81
# 71
# 61
# 10
# 20
# 30
# OUTPUT
# The Extended List
# [81, 71, 61, 10, 20, 30]
# The Reverse List
# [30, 20, 10, 61, 71, 81]
# TEST CASE 2
# 
# INPUT
# 2
# 2
# 100
# 200
# 10
# 20
# OUTPUT
# The Extended List
# [100, 200, 10, 20]
# The Reverse List
# [20, 10, 200, 100]

# In[ ]:


a=int(input(""))
b=int(input(""));
l=[]
for i in range(0,a):
   x=int(input(""));
   l.append(x);
for i in range(0,b):
   y=int(input(""));
   l.append(y);
print("The Extended List")
print(l)
print("The Reverse List")
l.reverse()
print(l)


# Q. 54: Second largest
# QUESTION DESCRIPTION
# 
# Write a Python Program to Find the Second Largest Number in a List
# Input :
# Number of Elements in the List
# Output
# Print the Second Largest Element in the List
# TEST CASE 1
# 
# INPUT
# 4
# 23 56 39 11
# OUTPUT
# 39
# TEST CASE 2
# 
# INPUT
# 3
# 23 4 67
# OUTPUT
# 23

# In[ ]:


no = int(input())
l = [int(i) for i in input().split()]
l.sort()
print(l[-2])


# Q. 55: Reverse and Remove
# QUESTION DESCRIPTION
# 
# Write a Program to create a list and get the input from the user.
# 
# Hint:
# 1. Get the size of the first list from the user
# 
# 2. Get the size of the second list from the user
# 
# 3. Get the elements of the first list
# 
# 4. Get the elements of the second list
# 
# 5. Get the element to be deleted in the list from the user
# 
# Operations:
# 
# 1. Concat both the lists and display the combined or extended list
# 
# 2. Display the list in the reverse order
# 
# 3. Delete the element entered by the user (Hint step 5)
# 
# 4. Display the final list after deletion of the element
# 
# TEST CASE 1
# 
# INPUT
# 2
# 2
# 100
# 200
# 10
# 20
# 100
# OUTPUT
# The Extended List
# [100, 200, 10, 20]
# The Reverse List
# [20, 10, 200, 100]
# [20, 10, 200]
# TEST CASE 2
# 
# INPUT
# 3
# 3
# 100
# 200
# 300
# 10
# 20
# 30
# 20
# OUTPUT
# The Extended List
# [100, 200, 300, 10, 20, 30]
# The Reverse List
# [30, 20, 10, 300, 200, 100]
# [30, 10, 300, 200, 100]

# In[ ]:


a=[]
c=[]
n=int(input(""))
m=int(input(""))
for i in range(1,n+1):
    b=int(input(""))
    a.append(b)
for i in range(1,m+1):
    b=int(input(""))
    a.append(b)
d=int(input(""))
new=a+c
print("The Extended List")
print(new)
new.reverse()
print("The Reverse List")
print(new)
new.remove(d)
print(new)


# Q. 56: Diagonal elements
# QUESTION DESCRIPTION
# 
# Write a program to display the diagonal elements
# TEST CASE 1
# 
# INPUT
# 3
# 3
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# OUTPUT
# The List
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# The Array elements
# 1 2 3 
# 4 5 6 
# 7 8 9 
# The Diagonal elements
# 1
# 5
# 9
# TEST CASE 2
# 
# INPUT
# 2
# 2
# 10
# 20
# 30
# 40
# OUTPUT
# The List
# [[10, 20], [30, 40]]
# The Array elements
# 10 20 
# 30 40 
# The Diagonal elements
# 10
# 40

# In[ ]:


m=[]
r=eval(input())
c=eval(input())
for row in range(r):
    m.append([])
    for col in range(c):
        e=eval(input())
        m[row].append(e)
print('The List')
print(m)
print('The Array elements')
for row in range(len(m)):
    for col in range(len(m[row])):
        print(m[row][col], end = " ")
    print()
print('The Diagonal elements')
p=len(m[0])
for i in range(p):
    print(m[i][i])
    


# Q. 57: Intersection
# QUESTION DESCRIPTION
# 
# Write a program to find the intersection of two lists
# TEST CASE 1
# 
# INPUT
# 5
# 5
# 12
# 13
# 14
# 15
# 16
# 11
# 12
# 10
# 14
# 16
# OUTPUT
# The intersection is
# [16, 12, 14]
# TEST CASE 2
# 
# INPUT
# 5
# 5
# 12
# 13
# 11
# 15
# 20
# 11
# 10
# 10
# 15
# 16
# OUTPUT
# The intersection is
# [11, 15]

# In[ ]:


def intersection(a, b):
    return list(set(a) & set(b))
 
def main():
    alist=[]
    blist=[]
    n1=int(input(""))
    n2=int(input(""))
    
    for x in range(0,n1):
        element=int(input())
        alist.append(element)
    
    for x in range(0,n2):
        element=int(input())
        blist.append(element)
    print("The intersection is")
    print(intersection(alist, blist))
main()


# Q. 57: Intersection
# QUESTION DESCRIPTION
# 
# Write a program to find the intersection of two lists
# TEST CASE 1
# 
# INPUT
# 5
# 5
# 12
# 13
# 14
# 15
# 16
# 11
# 12
# 10
# 14
# 16
# OUTPUT
# The intersection is
# [16, 12, 14]
# TEST CASE 2
# 
# INPUT
# 5
# 5
# 12
# 13
# 11
# 15
# 20
# 11
# 10
# 10
# 15
# 16
# OUTPUT
# The intersection is
# [11, 15]

# In[ ]:


def intersection(a, b):
    return list(set(a) & set(b))
 
def main():
    alist=[]
    blist=[]
    n1=int(input(""))
    n2=int(input(""))
    
    for x in range(0,n1):
        element=int(input())
        alist.append(element)
    
    for x in range(0,n2):
        element=int(input())
        blist.append(element)
    print("The intersection is")
    print(intersection(alist, blist))
main()


# Q. 58: Sorted Order
# QUESTION DESCRIPTION
# 
# Write a program that reads integers from the user and stores them in a list. Your program should continue reading values until the user enters 0. Then it should display all of the values entered by the user (except for the 0) in order from smallest to largest, with one value appearing on each line. Use either the sort method or the sorted function to sort the list.
# TEST CASE 1
# 
# INPUT
# 5
# 44
# 33
# 25
# 78
# 23
# 345
# 76
# 0
# OUTPUT
# 5
# 23
# 25
# 33
# 44
# 76
# 78
# 345
# TEST CASE 2
# 
# INPUT
# 15
# 144
# 133
# 125
# 178
# 123
# 1345
# 376
# 0
# OUTPUT
# 15
# 123
# 125
# 133
# 144
# 178
# 376
# 1345
# 

# In[ ]:


l = []
while(True):
    t = int(input())
    if t == 0 :
        break
    else:
        l.append(t)
l.sort()
for e in l:
    print(e)


# Q. 59: Odd and Even in a list
# QUESTION DESCRIPTION
# 
# Python Program to Put Even and Odd elements in a List into Two Different Lists
# 
# Input
# First Line is the Number of Inputs
# Second line is the elements of the list
# 
# Output
# Print the Even List and Odd List
# TEST CASE 1
# 
# INPUT
# 5
# 67 
# 43 
# 44 
# 22 
# 455
# OUTPUT
# The even list [44, 22]
# The odd list [67, 43, 455]
# TEST CASE 2
# 
# INPUT
# 3
# 23 
# 44 
# 99
# OUTPUT
# The even list [44]
# The odd list [23, 99]

# In[ ]:


a=[]
n=int(input())
for i in range(1,n+1):
    b=int(input())
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)


# Q. 60: Perfect Square
# QUESTION DESCRIPTION
# 
# Write a program to display the perfect square using list
# 
# Input:
# 
# 1. The lower range number
# 2. The upper range number
# 
# Output:
# 
# The perfect square number using List
# 
# Refer sample input and output for formatting specification.
# 
# All float values are displayed correct to 2 decimal places.
# 
# All text in bold corresponds to input and the rest corresponds to output.
# TEST CASE 1
# 
# INPUT
# 50
# 100
# OUTPUT
# [64, 81, 100]
# TEST CASE 2
# 
# INPUT
# 1
# 300
# OUTPUT
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]

# In[ ]:


def squares(a, b):
	lists=[]

	# Traverse through all numbers
	for i in range (a,b+1):
		j = 1;
		while j*j <= i:
			if j*j == i:
				lists.append(i)  
			j = j+1
		i = i+1
	return lists

lo = int(input())
up = int(input())

print(squares(lo, up))

