# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:13:24 2021

@author: SonjaJutte
"""

#Chapter 3 Functions

#p57
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')


hello()

hello()
hello()   

# def statments with parameters p59

def hello(name):
    print('Hello, ' + name)
    
hello('Alice')

#define, call, pass, argument, parameter  p59

def sayHello (name):
    print('Hello,' + name)

sayHello('Al')

#pg60 return values and return statements


import random

def getAnswer(answerNumber):
    if answerNumber ==1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber ==3:
        return 'Yes'
    elif answerNumber ==4:
        return 'Reply hazy try again'
    elif answerNumber ==5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber ==7:
        return 'My reply is no'
    elif answerNumber ==8:
        return 'Outlook is not so good'
    elif answerNumber ==9:
        return 'Very doubtful'
    
r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

#alt single equivalent line
print(getAnswer(random.randint(1,9)))

#pg 61 The none value
print()


spam = print('Hello!')

None == spam
#i sort of get it

#pg65 keyword arguments and the print function
#keyword arguments are identified by the keyword before the function call. they
#are often optional parameters
#eg
print('Hello', end = '')
print(' World')

#the call stack p63

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
    
def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')
    
a()

# local variables cannot be used in global scope p 66

def spam():
    eggs = 31337

spam()

print(eggs) 
#error because eggs variable only exists in the local scope created when eggs
#is called

#local scopes cannot use variables in other local scopes
#basically local variables in one function are completely seperate in another
#function.

#global variables can be read from a local scope pg67
def spam():
    print(eggs)

eggs =42
spam ()
print(eggs)

##local and global variables with same name pg 68

def spam():
    eggs = 'spam local' #(1)
    print(eggs)

def bacon():
    eggs = 'bacon local' #(2)
    print(eggs)
    spam()
    print(eggs)
    
eggs = 'global' #(3)
bacon()
print(eggs)

#(1) variable called eggs when spam function is called. Local scope.
#(2) variable called eggs that exists when bacon function is called. Local scope.
#(3)  variable called eggs that exists in global scope.

#the global statement pg 68

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

#indentation matters!
#eggs declared as global at top of spam, so when spam is assigned to eggs it's 
#done to the global variable, no local variable is created.

#pg69
def spam():
    global eggs
    eggs = 'spam'# this is the global
    
def bacon():
    eggs = 'bacon' # this is the local
    
def ham():
    print(eggs) # this is the global
    
eggs = 42

spam()
print(eggs)
#in a function a variable is either global or local

# p70 if you try to use a local variable before you assign a value you will get 
#an error

def spam():
    print(eggs)
    eggs = 'spam local'
    
eggs = 'global'
spam()

#Exception handling p71

def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

#yields error due to divide by zero.


# need to try

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
        
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

#pg72 Short programme zigzag

import time, sys
indent = 0 # how many spaces to indent
indentIncreasing = True # whether indent is increasing or not

try:
    while True: #infinite loop
        print(' ' * indent, end = '')
        print('********')
        time.sleep(0.1) # pause 1/10 of second
        
        if indentIncreasing:
            #increase the number of ospaces
            indent = indent + 1
            if indent == 20:
                #change directions
                indentIncreasing = False
        
        else:
            #decrease number of spaces:
                indent = indent - 1
                if indent == 0:
                    #change direction
                    indentIncreasing = True

except KeyboardInterrunpt:
    sys.exit()


#q11
import areallyourpetsnamederic

#pg 76 Collatz Sequence

def collatz(number):
    if number is even:
        print number // 2
    else:
        print (3* number + 1)
        
try:
    while True:
        input()
 