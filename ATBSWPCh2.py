# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:13:07 2020

@author: SonjaJutte
"""
##Ch2 Flow Control


#mixing boolean values and comparison operators pg 26
(4<5) and (5<6)

(4<5) and (9<6)

#blocks of code pg28
name = 'Mary'
password = 'swordfish'

if name == 'Mary':
    print("Hello, Mary")
    if password == 'swordfish':    
        print("Access granted")
    else: print("Wrong password")

# elif statements pg 31

name = 'Carol'
age = 3000
if name == 'Alice':
    print("Hi, Alice.")
elif age < 12:
    print("You are not Alice, kiddo.")
elif age >2000:
    print("Unlike you, Alice is not an undead, immortal vampire")
elif age >100:
    print("You are not Alice, grannie") 
    #Remember the rest of the elif clauses are automatically skipped once a 
    #true condition has been found
    
#alternative and better
name = 'Carol'
age = 3000
if name == 'Alice':
    print("Hi, Alice.")
elif age < 12:
    print("You are not Alice, kiddo.")
else:
    print("You are neither Alice nor a little kid.")
    
    #there is one if;
    #followed by elif
    #use else to close to ensure at least one clause is executed
    
#While Loops pg 35

#compare if and while. Code behaves differently.

#if
spam = 0
if spam < 5:
    print("hello world")
    spam = spam + 1
    
#while
spam = 0
while spam < 5:
    print("hello world")
    spam = spam + 1
else:
    print("End")

##annoying while loops pg 39



#if you never enter your name the while loop will never be false and keeps
#going forever

#break clauses 

while True: #this creates an infinate loop
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

#continue statements pg 40

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password?')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')
#note break leaves the loop and indentation matters here.

#for loops and range function pg44

print('My name is')
for i in range(7):
    print('Joe Five Times (' +str(i) + ')')
    
##pg 45
total = 0
for num in range(101):
    total = total + num
print(total)

#lets try another example
#this won't work because range start at nil
total_product = 0
for num in range(10):
    total_product = total_product * num
print(total_product)

#bingo

#equivalent while loop
# i can use a while loop to do the same thing as a for loop

print ('My name is')
i = 0

while i <5:
    print('Jimmy Five Times (' + str(i) + ') ')
    i = i +1
    
    #this gives the same output as for i in range (5) above. Interesting that
    #output varied whether you give it ' or '' marks. Keep with ' made output 
    #equivalent
    
#pg 46 starting, stopping and stepping args to range()

for i in range (12, 16):
    print(i)
    
    #let 's go back to  my little experiment above
    
total_product = 1
for num in range (1,4):
    total_product = total_product * num
print(total_product)

#add a step argument

for i in range (0, 10, 2):
    print(i)
    
#let's try with negative numbers

for i in range (5, -1, -1):
    print(i) 

#importing modules

import random
for i in range(5):
    print(random.randint(1,10))
    
#terminating a programme early

import sys

while True: #infinite loop
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You types ' + response + '.')


# Practice questions - for 1-8 see notebook
#q9

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')


#q13
for i in range(11):
    print(i)
    
#while i < 11:
    print(i)
    #note: bad idea. never ending loop
    
i = 1
while i <= 10:
    print(i)
    i = i +1
    
    #ok this works, but the the for loop seems more logical.
    
    #round() function
    #Python provides an inbuilt function round() which rounds off to the 
    #given number of digits and returns the floating point number, if no 
    #number of digits is provided for round off , it rounds off the number 
    #to the nearest integer.
    print(round(51.4)) 
    print(round(51.46586, 3))
    
    
    
    #abs() function
    
    #The abs() function is used to return the absolute value of a number.
float = -100/3

abs(float)

float1 = -54.6
abs(float1)
    