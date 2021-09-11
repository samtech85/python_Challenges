# 14th september, Mom birthday
# Tuples, Lists, and Dictionaries

######################################################################
# 069
'''
country = ("Haiti", "Somalia", "China", "Singapour", "Russia")
print(country)
findIndex = input("Enter your favorite country: ")

found = country.index(findIndex)
print("Your country position is", found + 1)

'''

######################################################################
# 070


'''
country = ("Haiti", "Somalia", "China", "Singapour", "Russia")
print(country)
findCountry = int(input("Enter your favorite country position: "))
found =country[findCountry]
print("In position", findCountry, "There is: ", found)
'''


######################################################################
# 071
'''
sports = ["Baseball", "Football"]
print(sports)
favouriteSport = input("What is you favourite sport: ")
sports.append(favouriteSport)
print(sports)
'''

######################################################################
# 072
'''
subjects = ["Math", "Biology", "Chemestry", "Physic", "Sports"]
print(subjects)

hateSubject = input("Which of these subject you don't like: ")
subjects.remove(hateSubject)
print()
print(hateSubject, "has been removed")
print(subjects)

'''
######################################################################
# 073
''''
food_dictionary = {}
food1 = input("Enter a food you like: ")
food_dictionary[1] = food1

food2 = input("Enter another food you like: ")
food_dictionary[2] = food2

food3 = input("Enter a third food you like: ")
food_dictionary[3] = food3

food4 = input("Enter the last food you like: ")
food_dictionary[4] = food4

print(food_dictionary)

dislike = int(input("Which of these do you want to get rid of? "))

del food_dictionary[dislike]

print(sorted(food_dictionary.values()))
'''

######################################################################
# 074

'''
colour = ["red", "blue", "black", "white", "pink", "grey", "purple", "yellow", "brown",]

start = int(input("Enter a starting number (0-4): "))
end = int(input("Enter an end number (5-9): "))

print(colour[start:end])
'''

######################################################################
# 075
'''
nums = [123, 345, 234, 765]

for i in nums:
    print(i)

selection = int(input("Enter a from the list: "))
if selection in nums:
    print(selection, "is in position", nums.index(selection))
else:
    print("That is not in the list")
'''
######################################################################
# 076
'''
name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")
party = [name1,name2,name3]

another = input("Do you want to invite another (y/n): ")

while another == "y":
    newName = party.append(input("Enter another name: "))
    another = input("Do you want to invite another (y/n)")

print("You have", len(party), "people coming to your party")
'''

######################################################################
# 077
'''
name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")
party = [name1,name2,name3]

another = input("Do you want to invite another (y/n): ")

while another == "y":
    newName = party.append(input("Enter another name: "))
    another = input("Do you want to invite another (y/n)")

print("You have", len(party), "people coming to your party")

selection = input("Enter one of the names: ")
print(selection, "is in position", party.index(selection), "on the list")
stillcome = input("Do you still want them to come (y/n):")

if stillcome == "n":
    party.remove(selection)

print(party)'''


######################################################################
# 078
'''
tv = ["Task Master", "Top Gear", "The Big Bang Theory", "How I met your Mother"]

for i in tv:
    print(i)

print()

newtv = input("Enter another TV show: ")
position = int(input("Enter a number between 0 and 3: "))

tv.insert(position, newtv)
for i in tv:
    print(i)'''


######################################################################
# 079

'''nums = []
count = 0

while count <3:
    num = int(input("Enter a number: "))
    nums.append(num)
    print(nums)
    count += 1

lastnum = input("Do you the last name saved (y/n): ")
if lastnum == "n":
    nums.remove(num)

print(nums)'''