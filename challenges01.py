# git checkout -b branchName


# ######################################################################
# 001
'''
firstname = input("Enter your firstname:")
print("Hello", firstname )
'''




# ######################################################################
# 002
'''
firstname = input("What is your firstname:")
surname = input('What is your surname:')
print("Hello", firstname, surname)
'''


# ######################################################################
# 003

'''
print("What do you call a bear with no teeth \nA gummy bear!")
'''


# ######################################################################
# 004
'''
num1 = int(input("Add a number:"))
num2 = int(input("Add another number:"))
total = num1 + num2
print("The total is", total)
'''

# ######################################################################
# 005
'''
num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
num_3 = int(input("Enter the third number:"))
operation = (num_1 + num_2)/ num_3
print("The answer is", operation)

'''

# ######################################################################
# 006
'''
sliceStarted = int(input("how many slice you started with:"))
sliceEaten = int(input("How many slice you have eaten:"))
sliceLeft = sliceStarted - sliceEaten
print("You have", sliceLeft, "slices left")
'''

# ######################################################################
# 007
'''
name = input("Enter your name:")
age = int(input("How old are you:"))
print(name, "next birthday you will be", age+1, "Years old")
'''

# ######################################################################
# 008
'''
billPrice = int(input("What is the total of the price:"))
numDinner = int(input("How many dinner there are:"))
personPay = billPrice / numDinner
print("Each person must pay", personPay,"$")
'''


# ######################################################################
# 009
'''
numDays = int(input("number of days:"))
hour = numDays* 24
minute = hour * 60
second = minute * 60

print("In", numDays,"days,","There are:", hour,"hours, ", minute,"minutes and", second,"seconds.")
'''
# ######################################################################
# 010
'''
weight = int(input("Enter your weight:"))
pound = weight * 2.204
print("You are", pound,"in pounds")
'''
# ######################################################################
# 011
larger = int(input("Enter a number over 100:"))
smaller = int(input("Enter a number under 10:"))
answer = larger // smaller
print(smaller, "goes into", larger, answer,"times")