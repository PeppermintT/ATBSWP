# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:39:18 2021

@author: SonjaJutte
"""

##ATBSWP Ch6 Pig Latin Project

#Writing a short programme that turns english to pig latin.

#English to pig latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')# this is a tuple of strings

pigLatin = [] # A list fo the words in PL
for word in message.split():
    #seperate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
            
    #seperate the non letters at the end of this word:
    suffixNonLetters = ''    
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
                
    #remember is the word was in uppercase or title case
    
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() #make the word lower case for translation
            
    #seperate the consonants at the start of this word
    prefixConsonants = ''
    while len(word)>0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

#add PL ending to the word
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

#set the word back to uppercase or titlecase

    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    #add the non letter back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

#Join all the words back together to a single string:

print(' '.join(pigLatin))    