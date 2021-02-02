# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 08:38:46 2021

@author: SonjaJutte
"""

#ATBSWP ch5 dictionaries

#p111

myCat = { 'size': 'fat', 'colour': 'grey', 'disposition': 'loud'}

#access values via keys
myCat['size']

'My cat has ' + myCat['colour'] + ' fur.'

#can use ints for keys, but don't need to start with nil and can be any number

#dicts vs list

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']

spam == bacon

#for lists the order matters

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham 

#for dicts the order does not matter

eggs['name']# i can access the key
#and if a key doesn't exist I get an error

eggs ['address'] 

#p113

birthdays = {'Alice': 'Apr 1', 'Bob' : 'Dec 12', 'Carol' : 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays [name] +  ' is the birthday of ' + name)
    else:
        print('I do not have the birthday information for  ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays [name] = bday
        print ('Birthday database updated.')        
        
        #sequence of KV pairs
list(eggs) # this gives us the order in which they were entered
#older versions of python don't remember this

#pg 114

spam = {'colour': 'red', 'age': 42}
for v in spam.values():
    print(v)
    
    #i am a bit confused by this
    #ok got it - values in quotations marks are values
    #if no quotation maround round 42, not a value

for k in spam.keys():
    print(k)
    
for i in spam.items():
    print(i)
    #note that output from items for loop is a tuple
    
#to get a list from these methods

spam = {'colour': 'red', 'age': 42}
spam.keys()

list(spam.keys())

#multiple assignment trick


spam = {'colour': 'red', 'age': 42}
for k,v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))

#pg115 check whether key or value exists

biscuit = {'name': 'Zophie', 'age': 7}
'name' in biscuit.keys()

'Zophie' in biscuit.values()

'colour' in biscuit.keys()

'colour' not in biscuit.keys()
'colour' in biscuit

#if you want to check whether a value is or is not a key, you can do in/not 
#with the dictionary value itself


#get() method

picnicItems = {'apples' : 5, 'cups' : 2}
'I am bringing ' + str( picnicItems.get('cups', 0)) + ' cups.'
'I am bringing ' + str( picnicItems.get('eggs', 0)) + ' eggs.'


#setdefault()
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('colour', 'black')
spam
#setdefault() is a nice shortcut to ensure that a key exists

#character count

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
print(count)

#Pretty printing p 118

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count)

pprint(pprint.pformat(count)) #not sure about this.

##p120 tic tac toe

theBoard = {'top-L': '', 'top-M' : '', 'top-R' : '',
            'mid-L': '', 'mid-M' : '', 'mid-R' : '',
            'low-L': '', 'low-M' : '', 'low-R' : ''}

def printBoard(board):
    print(board['top-L'] + '|' + board ['top-M'] + '|' + board ['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board ['mid-M'] + '|' + board ['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board ['low-M'] + '|' + board ['low-R'])

printBoard(theBoard)

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
printBoard(theBoard)

###
#not a complete programme, but helps see how data structures can be used in programmes
####
##pg125 nested dicts and lists

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches' : 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies' :1}}

def totalBrought (guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples     ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups     ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes     ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches     ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))


###






