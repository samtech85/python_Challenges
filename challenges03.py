
# #############################################################
# 020
'''
name = input("Enter your name:")
name = len(name)
print(name)

'''


# #############################################################
# 021

'''
firstname = input("Enter your firstname:")
surname = input("Enter your surname:")
name = firstname + " " + surname
length = len(name)
print(name)
print(length)

'''

# #############################################################
# 022

'''
firstname = input("Enter your first name in lowercase: ")
surname = input("Enter your surname in lowercase: ")
firstname = firstname.title()
surname = surname.title()

name = firstname + " " + surname
print(name)

'''

# #############################################################
# 023

'''
phrase = input("Enter the first line of a nursery rhyme:")
length = len(phrase)
print("This has", length, "letters in it")
start = int(input("Enter a starting number: "))
end = int(input("Enter an end number: "))

part = (phrase[start:end])
print(part)

'''


# #############################################################
# 024

'''
word = input("Enter a word: ")
word = word.upper()
print(word)

'''

# #############################################################
# 025

'''name = input("Enter your first name: ")
if len(name) < 5:
    surname = input("Enter your surname: ")
    name = name + surname
    print(name.upper())
else:
    print(name.lower())
    
'''


# #############################################################
# 026

'''
word = input("Please enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"
    print(newword.lower())

'''


