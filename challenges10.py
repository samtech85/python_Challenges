# More String Manipulation

# ####################################################################
# 080
'''name = input("Enter your firstname: ")
print("That has",len(name), "characters in it")

surname = input("Enter your surname: ")
print("That has",len(surname), "characters in it")

fullname = surname + " " + name
print("Your full name is")
print("That has", len(fullname), "characters in it")
'''


# ####################################################################
# 081

'''subject = input("Enter your favourite school subject: ")
for letter in subject:
    print(letter, end="-")'''


# ####################################################################
# 082

'''poem = "Oh I wish something like this!!!!!!"
print(poem)

start = int(input("Enter a starting number: "))
end = int(input("Enter an end number: "))

print(poem[start:end])'''


# ####################################################################
# 083
'''
msg = "Enter a message in uppercase: "
tryagain = False
while tryagain == False:
    if msg.isupper():
        print("Thank you")
        break
        tryagain == True
    else:
        print("Try again")
        msg = input("Enter a message in uppercase: ")

    '''


# ####################################################################
# 084

'''postcode = input("Enter your postcode: ")
start = postcode[0:2]
print(start.upper())'''

# ####################################################################
# 085
'''name = input("Enter your name: ")
count = 0

name = name.lower()
for x in name:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        count += 1
        print("Vowels =", count)

 '''    


# ####################################################################
# 086

'''pswd1 = input("Enter a password: ")
pswd2 = input("Enter it again: ")
if pswd1 == pswd2:
    print("Thank you")
elif pswd1.lower() == pswd2.lower():
    print("They must be the same case")
else:
    print("Incorrect")
'''


# ####################################################################
# 087



'''word = input("Enter a word:")
length = len(word)
num = 1
for x in word:
    position = length - num
    letter = word[position]
    print(letter)
    num = num + 1
'''
