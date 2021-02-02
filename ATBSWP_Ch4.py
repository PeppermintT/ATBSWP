# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 08:47:20 2021

@author: SonjaJutte
"""

###Ch4 Lists and Tuples

#lists of lists p79

spam = [['cat','bat'], [10,20,30,40,50]]

spam[0]

#here I am basically using am multiple index to access the list in a list
#the fist index dictates whic list value to use and the second indicates
#the value within the list value
spam[0][1]

spam[1][4]

#what happens if we just use one index here?
#we get the whole list at that index
spam[1]

 #del statement will delete values at an index in list

spam = ['cat','bat','rat', 'elephant']

del spam [2]

spam

#all my cats p83

catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatenation

print('The cat names are: ')
for name in catNames:
    print ('  ' + name)
    
    #using for loops with lists
    
for i in range (4):
    print(i)
    
    #output is identical to:

for i in [0,1,2,3]:
    print(i)
    
    
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in suppliers is: ' + supplies [i])
    
    ### in or not in operators
    #pg 85
    
'howdy' in ['hello', 'hi', 'howdy', 'heyas']

spam = ['hello', 'hi', 'howdy', 'heyas'] 
'cat' in spam

'howdy' not in spam

'cat' not in spam  

#
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:') 
name = input()

if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')


#Multiple Assignment Trick (technical terms if tuple unpacking)
#assign multiple variables with one line of code

cat = ['fat', 'gray', 'loud']
size = cat[0]
cat
size

colour = cat[1]
disposition = cat[2]

cat

#
cat = ['fat', 'gray', 'loud']

size, colour, disposition = cat

#not sure why this isn't working

#enumerate function p86

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

#random choice

import random
pets = ['Dog', 'Cat', 'Moose']
random.choice (pets)

random.choice(pets)

#random shuffle
import random

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
people

#augmented assignement operators
spam = 42
spam +=2
spam

#methods pg 88
people = ['Alice', 'Bob', 'Carol', 'David']

people.index('Carol')

##p89

spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam

#remove

spam = ['cat','bat', 'rat','elephant']
spam.remove('bat')
spam

#sorting pg 90

spam = [2,5,3.14,1,-7]
spam.sort()
spam

#default alphabetical
spam = ['ants', 'cats', 'dogs','badgers', 'elephants']
spam.sort()
spam

#or
spam.sort (reverse = True)
spam

#upper case come first
spam = ['Alice', 'ants', 'Badger', 'bats']
spam.sort()
spam

spam.sort(key = str.lower)
spam

#reverse
spam.reverse()
spam

#making code readable

print('Four score and seven' + \
      ' years ago......')
    
    # \ is like " the instruction continues on next line'
    
#pg 92 Magic 8 Ball with a list

import random

messages = ['It is certain,'
            'It is decidedly so',
            'Yes definately',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not do good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

#many things you can do with lists you can do with strings

name  = 'Zophie'
name [0]

name[-2]

'Zo' in name

'p' in name


#p94 Mutable and Immutable data types
#strings are not mutable

name = 'Zophie a cat'
newName = name [0:7] + 'the' + name[8:12]
newName

#pg 96 tuples

eggs = ('hello', 42, 0.5)
eggs[0]

eggs[1:3]

#tuples are a bit like lists, but they can't have their values changed. They
#are immutable

eggs[1] = 99 # will give an error

#converting types pg 97

tuple ( ['cat', 'dog', 5 ])

list ( ('cat', 'dog', 5 ))

list ('hello')

#p97 References
spam = 42
cheese = spam
spam = 100
spam

cheese

###
spam = [0,1,2,3,4,5]
cheese = spam # reference is copied not list
cheese[1] = 'hello' #changes the list value
spam

cheese# cheese variabl refers to same list

#p99 

id(cheese)

id ('Howdy')

#p100
eggs = ['cat', 'dog']
id(eggs)

eggs.append('moose')
id(eggs)
#same id

eggs = ['bat', 'rat', 'cow']
id(eggs)

#passing references
def eggs (someParameter):
    someParameter.append('Hello')
    
spam = [1,2,3]
eggs(spam)
print(spam)

#pg101 distinguish between copy and reference
import copy

spam = ['A', 'B', 'C', 'D']

id(spam)

cheese = copy.copy(spam)
id(cheese)# cheese is a different list with different identify

cheese[1] = 42
spam

cheese
#cheese and spam refer to seperate lists which is why cheese is modified while
#spam is not

#pg 102 Conways game of life

import random, time, copy
WIDTH = 60
HEIGHT = 40

#create a list of list for the cells:
    
nextCells = []
for x in range (WIDTH):
    column = []#create a new column.
    for y in range(HEIGHT):
        if random.randint (0,1) == 0:
            column.append('#') #add a living cell
        else:
            column.append(' ')
    nextCells.append(column) # nextCells is a list of column lists

while True: #main programme loop
    print('\n\n\n\n\n')#seperate each step with new lines
    currentCells = copy.deepcopy(nextCells)
    
#print currentCells on screen:
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(currentCells [x][y], end = '') #print the # or space
    print() # print the new line at the end of the row
    
#Calculate the next steps cells based on current step's cells:

for x in range(WIDTH):
    for y in range(HEIGHT):
        #get neibouring coordinates
        # % WIDTH ensures leftCoord is always between 0 and WIDTH
        
        leftCoord = ( x-1) % WIDTH
        rightCoord = ( x+ 1) % WIDTH
        aboveCoord = ( y-1) % HEIGHT
        belowCoord = ( y+1) % HEIGHT
        
        #count number of living neighbours:
        numNeighbours = 0
        if currentCells [leftCoord][aboveCoord] == '#':
            numNeighbours += 1# top left neighbour is alive
        if currentCells [x][aboveCoord] == '#':
            numNeighbours += 1# top neighbour is alive 
        if currentCells [rightCoord][aboveCoord] == '#':
            numNeighbours += 1# top right neighbour is alive
        if currentCells [leftCoord][y] == '#':
            numNeighbours += 1# left neighbour is alive
        if currentCells [rightCoord][y] == '#':
            numNeighbours += 1# right neighbour is alive
        if currentCells [leftCoord][belowCoord] == '#':
            numNeighbours += 1# bottom left neighbour is alive
        if currentCells [x][belowCoord] == '#':
            numNeighbours += 1# bottom neighbour is alive
        if currentCells [rightCoord][belowCoord] == '#':
            numNeighbours += 1# bottom right neighbour is alive
            
 #set cell based on Conways Game of Life rules:
        if currentCells [x][y] == '#' and (numNeighbours == 2 or numNeighbours ==3):
    #living cells  with 2 or 3 neighbours stay alive
            nextCells [x][y] = '#'
        elif currentCells [x][y] == ' ' and numNeighbours == 3:
            #dead cells with 3 neighbours come alive
            nextCells [x][y] = '#'
        else:
            #everything else dies or stays dead
            nextCells [x][y] = ' '
    time.sleep(1) # add 1 second pause to reduce flickering
    
    
    #practice project pg 107
    
    
list = ['apples', 'bananas', 'tofu', 'cats']
    
def add_to_list (list):
    print(list.insert(-1, 'and'))
 
add_to_list (list)       
####hmmm here is what SO suggests

def pr_list(listothings):    #define a function

    for i in range(len(listothings)-1):  # use range(len(somelist)) to iterate over
    #index of lists
        print(listothings[i] + ', ', end='')

spam = ['apples', 'bananas', 'tofu', 'cats']

pr_list(spam)

print('and ' + spam[-1])

test = ['parrot', 'budgie', 'magpie']
pr_list(test)
print('and ' + test [-1])


# pg 107 Coin flip streaks

import random
numberofStreaks = 0
for experimentNumber in range(10000):
    #code that creates a list of 100 heads or tails values
    HEADS = []
    TAILS = []
    if random.randint(0,1) == 0:
        HEADS.append()
    else:
        TAILS.append()
        
        
    