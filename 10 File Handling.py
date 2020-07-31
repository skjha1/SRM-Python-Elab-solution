#!/usr/bin/env python
# coding: utf-8

# ## SESSION: File Handling

# Q. 91: Create a dynamic file and read
# QUESTION DESCRIPTION

# Write a python program to create a file and display the contents (dynamic number of lines)

# Hint:

# 1. Create a File
# 2. Take the input as number of lines to be written into the file
# 3. Based on the number of lines get the input from the user
# 4. Add a new line to the file after each input.
# 5. Display the contents of the file written in the output

# Input:
# 1. Filename
# 2,3,4,5 = File contents
# TEST CASE 1

# INPUT
# sample.txt
# 5
# This is First Line
# This is Second Line
# This is Third Line
# This is Fourth Line
# This is Fifth Line
# OUTPUT
# This is First Line

# This is Second Line

# This is Third Line

# This is Fourth Line

# This is Fifth Line

# Number of lines:
# 10
# TEST CASE 2

# INPUT
# sample.txt
# 3
# This is First Line
# This is Second Line
# This is Third Line
# OUTPUT
# This is First Line

# This is Second Line

# This is Third Line

# Number of lines:
# 6

import string
file_name = input()
file = open(file_name, 'w+')

n = int(input())

for i in range(n):
    content = input()
    file.write(content + "\n\n")

file.write(f"Number of lines:\n{n*2}")
file.close()

f = open(file_name)
print(f.read())


# Q. 92: Captilize each word
# QUESTION DESCRIPTION

# Write a python program to create a file and Capitalise each word (Starting letter) in the file

# Hint:

# 1. Create a File
# 2. Take the input as number of lines to be written into the file
# 3. File name to be searched

# Input:
# 1. Filename
# 2. The number of lines to be written into the file
# 3. File name

# Output:
# Display the file content with capitalise of each word (Starting letter)
# TEST CASE 1

# INPUT
# sample.txt
# 4
# This is First Line of the file
# This is Second Line of the file create in eLab Server
# This is Third Line sample line
# This is fourth line of the file and eLab is an auto evaluation tool launched in 2017
# sample.txt
# OUTPUT
# This Is First Line Of The File

# This Is Second Line Of The File Create In Elab Server

# This Is Third Line Sample Line

# This Is Fourth Line Of The File And Elab Is An Auto Evaluation Tool Launched In 2017
# TEST CASE 2

# INPUT
# sample.txt
# 2
# This is First Line of the file
# This is Second Line of the file create in eLab Server
# sample.txt
# OUTPUT
# This Is First Line Of The File

# This Is Second Line Of The File Create In Elab Server

file_name = input()
file = open(file_name, 'w+')

n = int(input())

for i in range(n):
    content = input()
    file.write(string.capwords(content) + "\n\n")

file.close()

f = open(file_name)
print(f.read())


# Q. 93: Create a dynamic file and read the number of lines
# QUESTION DESCRIPTION

# Write a python program to create a file and display the contents (dynamic number of lines)

# Hint:

# 1. Create a File
# 2. Take the input as number of lines to be written into the file
# 3. Based on the number of lines get the input from the user
# 4. Add a new line to the file after each input.
# 5. Display the contents of the file written in the output
# 6. Display the Number of Lines in the File in the output

# Input:
# 1. Filename
# 2,3,4,5 = File contents
# TEST CASE 1

# INPUT
# sample.txt
# 5
# This is First Line
# This is Second Line
# This is Third Line
# This is Fourth Line
# This is Fifth Line
# OUTPUT
# This is First Line
# This is Second Line
# This is Third Line
# This is Fourth Line
# This is Fifth Line
# Number of lines:
# 5
# TEST CASE 2

# INPUT
# sample.txt
# 4
# This is First Line
# This is Second Line
# This is Third Line
# This is Fourth Line
# OUTPUT
# This is First Line
# This is Second Line
# This is Third Line
# This is Fourth Line
# Number of lines:
# 4

file_name = input()
file = open(file_name, 'w+')

n = int(input())

for i in range(n):
    content = input()
    file.write(content + "\n")

file.write(f"Number of lines:\n{n}")
file.close()

f = open(file_name)
print(f.read())


# Q. 94: Count the words
# QUESTION DESCRIPTION

# Write a python program to create a file and display the contents (dynamic number of lines) and count the number of words in the file.

# Hint:

# 1. Create a File
# 2. Take the input as number of lines to be written into the file
# 3. Based on the number of lines get the input from the user
# 4. Get the file name from the user for performing operations
# 5. Count the number of words in the file and display the number of words in the fie


# Input:
# 1. Filename
# 2. The number of lines to be written into the file
# 3. File name to perform operations
# TEST CASE 1

# INPUT
# sample.txt
# 2
# eLab an auto evaluation tool in Tamilnadu
# eLab will be launched in SWAYM platform soon
# sample.txt
# OUTPUT
# Number of words:
# 15
# TEST CASE 2

# INPUT
# sample.txt
# 4
# This is First Line of the file
# This is Second Line of the file create in eLab Server
# This is Third Line sample line
# This is fourth line of the file and eLab is an auto evaluation tool launched in 2017
# sample.txt
# OUTPUT
# Number of words:
# 41

file_name = input()
file = open(file_name, 'w+')

n = int(input())
word_count = 0

for i in range(n):
    content = input()
    file.write(content + "\n\n")
    word_count += len(content.split())

file.close()
print(f"Number of words:\n{word_count}")


# Q. 95: Create a File and read
# QUESTION DESCRIPTION

# Write a python program to create a file and display the contents

# Hint:

# 1. Create a File
# 2. Take four inputs from the user and add the four lines to the file
# 3. Display the contents of the file written in the output

# Input:
# 1. Filename
# 2,3,4,5 = File contents
# TEST CASE 1

# INPUT
# sample.txt
# This is First Line
# This is Second Line
# This is Third Line
# This is Fourth Line
# OUTPUT
# This is First LineThis is Second LineThis is Third LineThis is Fourth Line
# TEST CASE 2

# INPUT
# sample.txt
# eLab
# Tool
# is an
# auto evaluation tool
# OUTPUT
# eLab Tool is an auto evaluation tool

file_name = input()
file = open(file_name, 'w+')

n = 4

for i in range(n):
    content = input()
    file.write(content)

file.close()

f = open(file_name)
print(f.read())


# Q. 96: Reverse File
# QUESTION DESCRIPTION

# Write a Python Program to create a file and display the content(dynamic number of lines) and print the files contents in reverse order.
# Hint 1:
# 1. Create a file
# 2. Take the Input as number of lines to be written into the file
# 3. Based on the number of lines get the input from the user
# 4. Get the file name from the user for performing operations
# 5. Count the number of words in the file and display the number of words in the file input
# Input1:
# 1: Filename
# 2: The number of lines to be written into the file.
# 3. File name to perform operations
# TEST CASE 1

# INPUT
# sample.txt
# 4
# eLab an auto evaluation tool in Tamilnadu - eLab
# eLab will be launched in SWAYM platform soon - eLab
# eLab is used by 45000+users every year- eLab
# eLab is a copyleft tool - eLab
# sample.txt
# OUTPUT
# eLab is a copyleft tool - eLab
# eLab is used by 45000+users every year- eLab
# eLab will be launched in SWAYM platform soon - eLab
# eLab an auto evaluation tool in Tamilnadu - eLab
# TEST CASE 2

# INPUT
# sample.txt
# 2
# eLab an auto evaluation tool in Tamilnadu
# eLab will be launched in SWAYM platform soon
# sample.txt
# OUTPUT
# eLab will be launched in SWAYM platform soon
# eLab an auto evaluation tool in Tamilnadu

file_name = input()
file = open(file_name, 'w+')

n = int(input())

for i in range(n):
    content = input()
    file.write(content + "\n")

file.close()

f = open(file_name)
lines = f.read().strip().split("\n")
rev = lines[::-1]
for line in rev:
    print(line)


# Q. 97: Find the letter
# QUESTION DESCRIPTION

# Write a python program to create a file and display the contents (dynamic number of lines) and count the occurrence of the letter in the file and display the count.

# Hint:

# 1. Create a File
# 2. Take the input as number of lines to be written into the file
# 3. Based on the number of lines get the input from the user
# 4. Input the file name to perform the operations
# 5. Input the letter to be searched in the file

# Input:
# 1. Filename
# 2. The number of lines to be written into the file
# 3. File name
# 4. Letter to be searched

# Output:
# The occurrence(count) of the letter
# TEST CASE 1

# INPUT
# sample.txt
# 4
# eLab
# eLab eLab
# eLab eLab tool
# eLab eLab eLab eLab tool
# sample.txt
# e
# OUTPUT
# Occurrences of the letter
# 9
# TEST CASE 2

# INPUT
# sample.txt
# 2
# eLab eLab tool
# eLab eLab eLab eLab tool
# sample.txt
# L
# OUTPUT
# Occurrences of the letter
# 6

file_name = input()
file = open(file_name, 'w+')

n = int(input())

for i in range(n):
    content = input()
    file.write(content)
file.close()

f_name = input()
key = input()

f = open(f_name)
ref = f.read()

print(f"Occurrences of the letter\n{ref.count(key)}")


# Q. 98: Count Words
# QUESTION DESCRIPTION

# Write a python program to create a file and display the count of all the characters in the file

# Hint:

# 1. Create a File
# 2. Take the input as number of lines to be written into the file
# 3. Based on the number of lines get the input from the user
# 4. File name to be searched

# Input:
# 1. Filename
# 2. The number of lines to be written into the file
# 3. File name

# Output:
# Display the count of all characters in the file
# TEST CASE 1

# INPUT
# sample.txt
# 2
# eLab is an auto evaluation tool
# This file program in eLab will show you the count of words in the file except numbers like 1234567890
# sample.txt
# OUTPUT
# 99
# TEST CASE 2

# INPUT
# sample.txt
# 3
# eLab is an auto evaluation tool
# This file program in eLab will show you the count of words in the file except numbers like 1234567890
# 2017 2016 2015 2018 eLab
# sample.txt
# OUTPUT
# 103

file_name = input()
file = open(file_name, 'w+')

n = int(input())
char_count = 0

for i in range(n):
    content = input()
    file.write(content + "\n\n")
    words = content.split()
    for word in words:
        if not word.isdigit():
            char_count += len(word)

file.close()
print(char_count)


# Q. 99: Reverse File
# QUESTION DESCRIPTION

# Write a python program to create a file and display the contents (dynamic number of lines) and print the files contents in reverse order.

# Hint:

# 1. Create a File
# 2. Take the input as number of lines to be written into the file
# 3. Based on the number of lines get the input from the user
# 4. Get the file name from the user for performing operations
# 5. Count the number of words in the file and display the number of words in the fie


# Input:
# 1. Filename
# 2. The number of lines to be written into the file
# 3. File name to perform operations
# TEST CASE 1

# INPUT
# sample.txt
# 4
# eLab an auto evaluation tool in Tamilnadu - eLab
# eLab will be launched in SWAYM platform soon - eLab
# eLab is used by 45000+users every year- eLab
# eLab is a copyleft tool - eLab
# sample.txt
# OUTPUT
# eLab is a copyleft tool - eLab
# eLab is used by 45000+users every year- eLab
# eLab will be launched in SWAYM platform soon - eLab
# eLab an auto evaluation tool in Tamilnadu - eLab
# TEST CASE 2

# INPUT
# sample.txt
# 2
# eLab an auto evaluation tool in Tamilnadu
# eLab will be launched in SWAYM platform soon
# sample.txt
# OUTPUT
# eLab will be launched in SWAYM platform soon
# eLab an auto evaluation tool in Tamilnadu

file_name = input()
file = open(file_name, 'w+')

n = int(input())

for i in range(n):
    content = input()
    file.write(content + "\n")

file.close()

f = open(file_name)
lines = f.read().strip().split("\n")
rev = lines[::-1]
for line in rev:
    print(line)


# Q. 100: Count Number
# QUESTION DESCRIPTION

# Write a python program to create a file and display the contents (dynamic number of lines) and count the numbers in the file and display the count.

# Hint:

# 1. Create a File
# 2. Take the input as number of lines to be written into the file
# 3. Based on the number of lines get the input from the user
# 4. Input the file name to perform the operations

# Input:
# 1. Filename
# 2. The number of lines to be written into the file
# 3. File name

# Output:
# The total count of the numbers in the file
# TEST CASE 1

# INPUT
# sample.txt
# 2
# eLab 1.0 launched in 2017
# eLab 2.0 next version will be launched in 2019
# sample.txt
# OUTPUT
# 12
# TEST CASE 2

# INPUT
# sample.txt
# 3
# eLab 1.0 launched in 2017
# eLab 2.0 next version will be launched in 2019
# 2016 2017 2018 2019 2020 2021
# sample.txt
# OUTPUT
# 36

file_name = input()
file = open(file_name, 'w+')

n = int(input())
char_count = 0

for i in range(n):
    content = input()
    file.write(content + "\n\n")
    words = content.split()
    for word in words:
        if word.replace('.', '').isdigit():
            char_count += len(word)
            if "." in word:
                char_count -= 1

file.close()
print(char_count)
