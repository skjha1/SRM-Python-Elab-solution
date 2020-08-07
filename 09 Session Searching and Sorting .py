#!/usr/bin/env python
# coding: utf-8

# Q. 81: Binary Search
# QUESTION DESCRIPTION
# 
# Write a program to implement binary search algorithm
# TEST CASE 1
# 
# INPUT
# 20
# 1
# 9
# 18
# 24
# 27
# 35
# 38
# 41
# 49
# 53
# 55
# 66
# 67
# 72
# 75
# 77
# 81
# 89
# 90
# 97
# 3
# 35
# 38
# 41
# OUTPUT
# Sequence found between index 5 and 8
# TEST CASE 2
# 
# INPUT
# 20
# 1
# 9
# 18
# 24
# 27
# 35
# 38
# 41
# 49
# 53
# 55
# 66
# 67
# 72
# 75
# 77
# 81
# 89
# 90
# 97
# 3
# 35
# 38
# 40
# OUTPUT
# Not found

# In[ ]:


def binarySearch (arr, l, r, x):
	if r >= l:
		mid = int(l + (r - l)/2)
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binarySearch(arr, l, mid-1, x)
		else:
			return binarySearch(arr, mid+1, r, x)
	else:
		return -1
arr=[]
n=int(input(""))
for i in range(1,n+1):
    b=int(input(""))
    arr.append(b)
a=int(input(""))
b=0
c=[]
for i in range(a):
	x=int(input(""))
	result = binarySearch(arr, 0, len(arr)-1, x)
	if result != -1:
		b+=1
		if(i==0):
			c.append(result)
		if(i==a-1):
			c.append(result+1)
if(b==a):
	print("Sequence found between index",end=" ")
	for i in range(len(c)):
		if(i==0):
			print(c[i],"and",end=" ")
		else:
			print(c[i])
else:
    print("Not found")


# Q. 82: Find the sequence of given integers
# QUESTION DESCRIPTION
# 
# Sort the given set of integers using bubble sort and find the smallest and largest among given set of integers.
# Step1: Get the number of integers
# Step 2:Receive the integers
# Step3:Sort the integers using bubble sort
# Step 4:Print the start and end of sequence
# TEST CASE 1
# 
# INPUT
# 4
# 99 
# 5 
# 6 
# 97
# OUTPUT
# Sequence of integers: 4 to 100
# TEST CASE 2
# 
# INPUT
# 5
# 22 
# 11 
# 5 
# 6 
# 7
# OUTPUT
# Sequence of integers: 4 to 23

# In[ ]:


def bsort(a):
    for i in range(len(a)):
        for k in range(0,len(a)-1):
            if(a[k]>a[k+1]):
                t=a[k]
                a[k]=a[k+1]
                a[k+1]=t
        if i==2:
            for x in a:
                x

n=int(input(""))
list=[]
for i in range(n):
    l=int(input(""))
    list.append(l)
bsort(list)
for i in list:
    i
print("Sequence of integers:",list[0]-1,"to",list[-1]+1)


# Q. 83: Find increment sequence
# QUESTION DESCRIPTION
# 
# Perform sorting on list of integers and print the sequence showing order of increment.
# TEST CASE 1
# 
# INPUT
# 5
# 11 24 77 66 55
# OUTPUT
# Sorted List
# [11, 24, 55, 66, 77]
# Sequence of increments
# [13, 31, 11, 11]
# TEST CASE 2
# 
# INPUT
# 5
# 2 2 2 2 2
# OUTPUT
# Sorted List
# [2, 2, 2, 2, 2]
# Sequence of increments
# [0, 0, 0, 0]

# In[ ]:


a=[]
c=[]
n=int(input(""))
b=input("")
a=[int(n) for n in b.split()]
a.sort()
print("Sorted List")
print(a)
for i in range(1,n):
    d=a[i]-a[i-1]
    c.append(d)
print("Sequence of increments")
aList = list(c)
print(aList)


# Q. 83: Find increment sequence
# QUESTION DESCRIPTION
# 
# Perform sorting on list of integers and print the sequence showing order of increment.
# TEST CASE 1
# 
# INPUT
# 5
# 11 24 77 66 55
# OUTPUT
# Sorted List
# [11, 24, 55, 66, 77]
# Sequence of increments
# [13, 31, 11, 11]
# TEST CASE 2
# 
# INPUT
# 5
# 2 2 2 2 2
# OUTPUT
# Sorted List
# [2, 2, 2, 2, 2]
# Sequence of increments
# [0, 0, 0, 0]

# In[ ]:


a=[]
c=[]
n=int(input(""))
b=input("")
a=[int(n) for n in b.split()]
a.sort()
print("Sorted List")
print(a)
for i in range(1,n):
    d=a[i]-a[i-1]
    c.append(d)
print("Sequence of increments")
aList = list(c)
print(aList)


# Q. 84: Find increment sequence
# QUESTION DESCRIPTION
# 
# Perform sorting on list of integers and print the sequence showing order of increment.
# TEST CASE 1
# 
# INPUT
# 5
# 11 24 77 66 55
# OUTPUT
# Sorted List:
# [11, 24, 55, 66, 77]
# Sequence of increments:
# [13, 31, 11, 11]
# TEST CASE 2
# 
# INPUT
# 5
# 2 2 2 2 2
# OUTPUT
# Sorted List:
# [2, 2, 2, 2, 2]
# Sequence of increments:
# [0, 0, 0, 0]

# In[ ]:


a=[]
c=[]
n=int(input(""))
b=input("")
a=[int(n) for n in b.split()]
a.sort()
print("Sorted List:")
print(a)
for i in range(0,n-1):
    d=a[i+1]-a[i]
    c.append(d)
print("Sequence of increments:")
print(c)


# Q. 85: Finding the occurrence of an integer
# QUESTION DESCRIPTION
# 
# Find the given integer in the given list of integers and print the number of occurrences of that integer in the list.
# TEST CASE 1
# 
# INPUT
# 7
# 64 34 7 12 22 11 7
# 7
# OUTPUT
# 2
# TEST CASE 2
# 
# INPUT
# 7
# 64 34 45 34 24 29 74
# 9
# OUTPUT
# 0

# In[ ]:


a=eval(input())
v=input()
c=v.split()
co=0
l=[] 
l=[eval(x) for x in c]
sv=eval(input())
for x in range(a):
    if l[x]==sv:
        co=co+1
print(co)


# Q. 86: Find Mid-term With ODD and Even length of list
# QUESTION DESCRIPTION
# 
# Perform sorting on list of integers and print the mid-term.
# TEST CASE 1
# 
# INPUT
# 5
# 11 
# 22 
# 33 
# 66 
# 67
# OUTPUT
# Sorted List:
# [11, 22, 33, 66, 67]
# Mid-term:
# 33
# TEST CASE 2
# 
# INPUT
# 6
# 11 
# 63 
# 4 
# 8 
# 99 
# 55
# OUTPUT
# Sorted List:
# [4, 8, 11, 55, 63, 99]
# Mid-term:
# 11
# 

# In[ ]:


mlist=[]
def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

n=int(input(""))
l=[]
for i in range(n):
    n1=int(input(""))
    l.append(n1)
#msort(l)
l.sort()
for i in l:
    mlist.append(i)
print("Sorted List:")
print (mlist)
middle = findMiddle(mlist)
print("Mid-term:")
print (middle)


# Q. 87: Finding the multiple
# QUESTION DESCRIPTION
# 
# Find the multiple of given number in the list of integers
# Input:
# First Line of the Input is the Number of Elements in the List
# Second Line of Input has the elements of the List
# Third line has has the number for which you have to find the multiples
# Output:
# Print the Multiples
# TEST CASE 1
# 
# INPUT
# 5
# 6 
# 7 
# 8 
# 13 
# 11
# 3
# OUTPUT
# 6
# TEST CASE 2
# 
# INPUT
# 4
# 5 
# 3 
# 7
# 5
# 7
# OUTPUT
# 7
# 

# In[ ]:


l=[]
n=int(input())
for i in range(n):
    ele=int(input())
    l.append(ele)
#print(l)

flag=0
finddiv=int(input())
for val in l:
    if ((val%finddiv)==0):
        print(val)
        flag=1
        if (flag!=1):
            print("No Multiples")


# Q. 88: Searching Linear
# QUESTION DESCRIPTION
# 
# Write a program to search a element linearly
# TEST CASE 1
# 
# INPUT
# 5
# 2
# 3
# 4
# 10
# 40
# 3
# OUTPUT
# Element is present at index 1
# TEST CASE 2
# 
# INPUT
# 5
# 2
# 3
# 4
# 10
# 40
# 10
# OUTPUT
# Element is present at index 3

# In[ ]:


x=int(input(""));
l=[]
for i in range(0,x):
    y=int(input(""));
    l.append(y);
f=int(input(""));
for i in range(0,x):
    if(l[i]==f):
       print("Element is present at index",i);


# Q. 89: Bubble Sort
# QUESTION DESCRIPTION
# 
# Sort the given set of numbers using Bubble Sort. The first line of the input contains the number of elements, the second line of the input contains the numbers to be sorted. In the output print the status of the array at the 3rd iteration and the final sorted array in the given format
# TEST CASE 1
# 
# INPUT
# 7
# 64
# 34
# 25
# 12
# 22
# 11
# 90
# OUTPUT
# 12 22 11 25 34 64 90
# Sorted array:
# 11 12 22 25 34 64 90
# TEST CASE 2
# 
# INPUT
# 8
# 14
# 83
# 25
# 47
# 9
# 77
# 1
# 0
# OUTPUT
# 14 9 25 1 0 47 77 83
# Sorted array:
# 0 1 9 14 25 47 77 83
# 

# In[ ]:


n=int(input())
arr=[]
t=[]
for i in range(n):
    arr.append(int(input()))
for i in range(0,n):
    for j in range(0, n-1):
        if (arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
    if (i==2):
        for p in range(0,n):
            if p < n-1:
                print(arr[p],"",end='')
            else:
                print(arr[p])
print("Sorted array:")
for p in range(n):
    if p < n-1:
        print(arr[p],"",end='')
    else:
        print(arr[p])

