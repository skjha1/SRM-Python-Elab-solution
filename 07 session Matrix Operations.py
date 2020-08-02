#!/usr/bin/env python
# coding: utf-8

# Q. 61: Seasoners
# QUESTION DESCRIPTION
# 
# The year is divided into four seasons: spring, summer, fall and winter. While the exact dates that the seasons change vary a little bit from year to year because of the way that the calendar is constructed, we will use the following dates for this exercise:
# 
# Season First day
# Summer March 20
# Spring June 21
# Fall September 22
# Winter December 21
# 
# Create a program that reads a month and day from the user. The user will enter the name of the month as a string, followed by the day within the month as an integer.
# 
# Then your program should display the season associated with the date that was entered.
# 
# Note: Enter First three letter for month example: Jan for january, Feb for Feburary ans so on....and first letter of the month should be capital
# TEST CASE 1
# 
# INPUT
# Sep
# 22
# OUTPUT
# Fall
# TEST CASE 2
# 
# INPUT
# Mar
# 20
# OUTPUT
# Summer

# In[2]:


m=input("")
d=int(input(""))
if m == "Jan" or m == "Feb":
    s="Winter"
elif m=="Mar":
    if d<20:
        s="Winter"
    else:
      	s="Summer"
if m == "Apr" or m == "May":
    s="Summer"
elif m=="Jun":
    if d<21:
        s="Summer"
    else:
       	s="Spring"
if m == "Jul" or m == "Aug":
    s="Spring"
elif m=="Sep":
    if d<22:
        s="Spring"
    else:
       	s="Fall" 
if m == "Oct" or m == "Nov":
  	s="Fall" 
elif m=="Dec":
    if d<21:
        s="Fall" 
    else:
      	s="Winter"           
print(s) 


# Q. 62: Huffman Encoding
# QUESTION DESCRIPTION
# 
# Given An array of Alphabets and their frequency. Your task is to print all the given alphabets Huffman Encoding.
# Note: If two elements have same frequency, then the element which if at first will be taken on left of Binary Tree and other one to right.
# 
# Input:
# First line consists of test cases T. First line of every test case consists of string of alphabets and second line consists of its frequencies.
# 
# Output:
# Print the HuffmanCodes in single line, with n spaces of each alphabet's HuffmanCodes respectively. In PreOrder form of Binary Tree.
# 
# Constraints:
# 1<=T<=100
# 1<=|String length|<=26
# TEST CASE 1
# 
# INPUT
# 1
# abcdef
# 5 9 12 13 16 45
# OUTPUT
# [0, 100, 101, 1100, 1101, 111]
# TEST CASE 2
# 
# INPUT
# 1
# abcdef
# 5 9 13 21 61 45
# OUTPUT
# [0, 10, 110, 1110, 11110, 11111]

# In[ ]:


import queue
class HuffmanNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root     
    def children(self):
        return((self.left, self.right))

a=input()
b=input()
c=input()
d=c.split()
freq=[]
freq1=[]
l1=[]
l2=[eval(x) for x in d]
for x in range(len(b)):
    l1.append(b[x])
for x in range(len(l1)):
    freq1.append([])
    for y in range(0,1):
        freq1[x].append(l2[x])
for x in range(len(l1)):
    for y in range(0,1):
        freq1[x].append(l1[x])       
    freq.append(tuple(freq1[x]))

def create_tree(frequencies):
    p = queue.PriorityQueue()
    for value in frequencies:    
        p.put(value)             
    while p.qsize() > 1:         
        l, r = p.get(), p.get()  
        node = HuffmanNode(l, r) 
        p.put((l[0]+r[0], node))      
    return p.get()               

node = create_tree(freq)

def walk_tree(node, prefix="", code={}):
    if isinstance(node[1].left[1], HuffmanNode):
        walk_tree(node[1].left,prefix+"0", code)
    else:
        code[node[1].left[1]]=prefix+"0"
    if isinstance(node[1].right[1],HuffmanNode):
        walk_tree(node[1].right,prefix+"1", code)
    else:
        code[node[1].right[1]]=prefix+"1"
    return(code)

code = walk_tree(node)
l3=[]
for j in code.values():
    l3.append(eval(j))
print(l3)


# Q. 63: Diagonal Sum
# QUESTION DESCRIPTION
# 
# Write a python program to create a NESTED LIST and print the sum of the diagonal elements in the matrix
# 
# Hint:
# 
# 1. Input the number of rows First Matrix
# 
# 2. Input the number of Columns for Second Matrix
# 
# 3. Display the sum of the diagonal elements in the matrix
# TEST CASE 1
# 
# INPUT
# 2
# 2
# 10
# 20
# 30
# 40
# OUTPUT
# 50
# TEST CASE 2
# 
# INPUT
# 3
# 3
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# OUTPUT
# 150

# In[ ]:


a=int(input(""))
b=int(input(""))
sum1=0
c=[[int(input("")) for j in range(a)] for i in range(b)]
for i in range(a):
    for j in range(b):
        if i==j:
            sum1=sum1+c[i][j]
print(sum1)


# Q. 64: Maximum Rectangular Area in a Histogram
# QUESTION DESCRIPTION
# 
# Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.
# 
# 
# 
# 
# 
# Input:
# The first line contains an integer 'T' denoting the total number of test cases. In each test cases, the first line contains an integer 'N' denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array. The elements of the array represents the height of the bars.
# 
# 
# Output:
# In each seperate line the maximum rectangular area possible from the contigous bars.
# 
# 
# Constraints:
# 1<=T<=30
# 1<=N<=100
# 1<=A[i]<=1000
# TEST CASE 1
# 
# INPUT
# 1
# 7
# 6 2 5 4 5 1 6
# OUTPUT
# 12

# In[ ]:


a=eval(input())
b=eval(input())
c=input()
d=c.split()
l1=[]
l1=[eval(x) for x in d]
l1.sort()
print(max(l1)*2)
#print(l1+l1)


# Q. 65: Matrix Display -Type 1
# QUESTION DESCRIPTION
# 
# Write a python program to create a NESTED LIST and form a matrix.
# 
# Hint:
# 
# 1. Input the number of rows and columns for First Matrix
# 
# 2. Input the number of rows and columns for Second Matrix
# 
# 3. Display the first matrix elements in Matrix format
# 
# 4. Display the first matrix elements in Matrix format
# TEST CASE 1
# 
# INPUT
# 2
# 2
# 10
# 20
# 30
# 40
# 1
# 2
# 3
# 4
# OUTPUT
# Matrix 1
# [10, 20]
# [30, 40]
# Matrix 2
# [1, 2]
# [3, 4]
# TEST CASE 2
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
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# OUTPUT
# Matrix 1
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# Matrix 2
# [10, 20, 30]
# [40, 50, 60]
# [70, 80, 90]

# In[ ]:


n=int(input(""))
m=int(input(""))
a = [[0] * n for i in range(n)]
b = [[0] * n for i in range(n)]
for i in range(0,n):
	for j in range(0,n):
		a[i][j]=int(input(""))      
for i in range(0,m):
	for j in range(0,m):
		e=input("")
		b[i][j]=int(e)
print("Matrix 1")
for r in a:
	print(r)
print("Matrix 2")
for r in b:
	print(r)       


# Q. 66: Identity Matrix
# QUESTION DESCRIPTION
# 
# Write Python Program to read a number n and print an identity matrix of the desired size.
# 
# Input:
# Size of the matrix
# 
# Output:
# Print the Identity matrix
# TEST CASE 1
# 
# INPUT
# 4
# OUTPUT
# 1 0 0 0 
# 0 1 0 0 
# 0 0 1 0 
# 0 0 0 1 
# TEST CASE 2
# 
# INPUT
# 5
# OUTPUT
# 1 0 0 0 0 
# 0 1 0 0 0 
# 0 0 1 0 0 
# 0 0 0 1 0 
# 0 0 0 0 1

# In[ ]:


n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()


# Q. 67: Transpose of Matrix
# QUESTION DESCRIPTION
# 
# Write a python program to create a NESTED LIST and print the diagonal elements of the matrix
# 
# Hint:
# 
# 1. Input the number of rows First Matrix
# 
# 2. Input the number of Columns for first Matrix
# 
# 3. Display the elements of the matrix
# 
# 4. Display the transpose of the matrix
# TEST CASE 1
# 
# INPUT
# 2
# 2
# 1
# 2
# 3
# 4
# OUTPUT
# Given Matrix
# [1, 2]
# [3, 4]
# Transpose of the matrix
# [1, 3]
# [2, 4]
# TEST CASE 2
# 
# INPUT
# 3
# 3
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# OUTPUT
# Given Matrix
# [10, 20, 30]
# [40, 50, 60]
# [70, 80, 90]
# Transpose of the matrix
# [10, 40, 70]
# [20, 50, 80]
# [30, 60, 90]

# In[ ]:


n=int(input(""))
m=int(input(""))
a = [[0] * n for i in range(n)]
b = [[0] * n for i in range(m)]
matrix=[[0] * n for i in range(n)]
for i in range(0,n):
	for j in range(0,m):
		a[i][j]=int(input(""))
print("Given Matrix")
for r in a:
	print(r)
result=[[0,0],
       	[0,0]]
result1=[[0,0,0],
         [0,0,0],
         [0,0,0]]
if(n==2):
	print("Transpose of the matrix")
	for i in range(len(a)):
		for j in range(len(a[0])):
  			result[j][i] = a[i][j]
if(n==2):
	for r in result:
		print(r)   
if(n==3):
	print("Transpose of the matrix")
	for i in range(len(a)):
		for j in range(len(a[0])):
  			result1[j][i] = a[i][j]
if(n==3):
	for r in result1:
 		print(r)             


# Q. 68: Row with minimum number of 1's
# QUESTION DESCRIPTION
# 
# Determine the row index with minimum number of ones. The given 2D matrix has only zeroes and ones and also the matrix is sorted row wise . If two or more rows have same number of 1's than print the row with smallest index.
# 
# Note: If there is no '1' in any of the row than print '-1'.
# 
# Input:
# The first line of input contains an integer T denoting the number of test cases. The first line of each test case consists of two integer n and m. The next line consists of n*m spaced integers.
# 
# Output:
# Print the index of the row with minimum number of 1's.
# 
# Constraints:
# 1<=T<=200
# 1<=n,m<=100
# TEST CASE 1
# 
# INPUT
# 2
# 3 3
# 0 0 0 0 0 0 0 0 0
# 4 4
# 0 0 0 1 0 1 1 1 0 0 1 1 0 0 1 1
# OUTPUT
# minus1
# 0

# In[ ]:


t = int(input())

for i in range(t):
    n = input()
    t = n.split()
    r = int(t[0])
    c = int(t[1])
    tot = r * c
    mat = []
    inp = input()
    form = inp.split()

    inx = 0
    for i in range(r):
        tmp = []
        for j in range(c):
            e = int(form[inx])
            inx += 1
            tmp.append(e)
        mat.append(tmp)
    #Matrix ready
    #print(mat)
    
    flag = -999
    mi = 999
    #Check for row with min 1s
    res = -1
    index = 0
    for sub in mat:
        cnt = sub.count(1)
        if cnt !=0 :
            if cnt < mi:
                mi = cnt
                res = index
                flag = 0
                
        index += 1
    if flag == -999:
        print("minus1")
    else:
        print(res)


# Q. 69: Find nth element of spiral matrix
# QUESTION DESCRIPTION
# 
# Given a matrix your task is to find the kth element which is obtained while traversing the matrix spirally. You need to complete the method findK which takes four arguments the first argument is the matrix A and the next two arguments will be n and m denoting the size of the matrix A and then the forth argument is an integer k denoting the kth element . The function will return the kth element obtained while traversing the matrix spirally.
# 
# 
# Input:
# The first line of input is the no of test cases then T test cases follow . The first line of each test case has three integers n,m and k . Then in the next line are n*m space separated values of the matrix A [ ] [ ] .
# 
# Output:
# The output for each test case will be the kth obtained element .
# 
# Constraints:
# 1<=T<=100
# 1<=n,m<=20
# 1<=k<=n*m
# TEST CASE 1
# 
# INPUT
# 1
# 3 3 4
# 1 2 3 4 5 6 7 8 9 
# OUTPUT
# 6

# In[ ]:


a=eval(input())
b=input()
q=(b.split())
d=input()
me=(d.split())
m=[]
r=int(q[0])
c=int(q[1])
f=int(q[2])
i=0
for row in range(r):
    m.append([])
    for col in range(c):
        m[row].append(me[i])
        i+=1
if f<=c:
    for row in range(0,1):
        print(m[row][f], end = " ")
if f>c:
    if f==c+1:
        for row in range(1,2):
            print(m[row][col], end = " ")
    print()


# Q. 70: Overlapping rectangles
# QUESTION DESCRIPTION
# 
# Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y co-ordinates of two points: the left top corner and the right bottom corner of the rectangle.
# 
# Note that two rectangles sharing a side are considered overlapping.
# 
# rectanglesOverlap
# 
# Input:
# 
# The first integer T denotes the number of test cases. For every test case, there are 2 lines of input. The first line consists of 4 integers: denoting the co-ordinates of the 2 points of the first rectangle. The first integer denotes the x co-ordinate and the second integer denotes the y co-ordinate of the left topmost corner of the first rectangle. The next two integers are the x and y co-ordinates of right bottom corner. Similarly, the second line denotes the cordinates of the two points of the second rectangle.
# 
# Output:
# 
# For each test case, output (either 1 or 0) denoting whether the 2 rectangles are overlapping. 1 denotes the rectangles overlap whereas 0 denotes the rectangles do not overlap.
# 
# Constraints:
# 
# 1 <= T <= 10
# 
# -10000 <= x,y <= 10000
# 
# T denotes the number of test cases. x denotes the x co-ordinate and y denotes the y co-ordinate.
# TEST CASE 1
# 
# INPUT
# 2
# 0 10 10 0
# 5 5 15 0
# 0 2 1 1
# -2 -3 0 2
# OUTPUT
# 1
# 0

# In[ ]:


def ovre(x,y):
    t=0
    for z in range(x[0],x[1]):
        if z == y[0] or x == y[1]:
            t=1
            break
    if t==1:
        return 1
    else:
        return 0

a=eval(input())
b=input()
c=b.split()
d=input()
e=d.split()
f=input()
g=f.split()
h=input()
i=h.split()
l=[]
l1=[]
l2=[]
l3=[]
l=[eval(x) for x in c]
l1=[eval(x) for x in e]
l2=[eval(x) for x in g]
l3=[eval(x) for x in i]
print(ovre(l,l1))
print(ovre(l1,l2))


# In[ ]:




