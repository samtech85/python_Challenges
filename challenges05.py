
'''For loop lesson'''

# #################################################################
# 035

'''
name = input("Enter your name:")
for i in range(0, 3):
    print(name)
'''

# #################################################################
# 036

'''
name = input("Enter your name: ")
number = int(input("Enter a number: "))
for i in range(0, number):
    print(name)

'''

# #################################################################
# 037

'''
name = input("Enter your name:")
for i in name:
    print(i)
'''


# #################################################################
# 038

'''
num = int(input("Enter a number:"))
name = input("Enter your name:")

for x in range(0, num):
    for i in name:
        print(i)
'''



# #################################################################
# 039

'''
num = int(input("Enter a number between 1 and 13: "))
for i in range(1, 13):
    answer = i * num
    print(i, "x", num, "=", answer)

'''

# #################################################################
# 040

'''
num = int(input("Enter a number below 50: "))
for i in range(50, num-1, -1):
    print(i)
    
'''
# #################################################################
# 041

'''
name = input("Enter your name:")
num = int(input("Enter a number: "))

if num < 10:
    for i in range(0, num):
        print(name)
else:
    for i in range(0,3):
        print("Too high")
'''

# #################################################################
# 042

'''
total = 0
for i in range(0,5):
    num = int(input("Enter a number: "))
    ans = input("Do you want this number included? (Y/n ")
    if ans == "y":
        total = total + num
print(total)

'''
# #################################################################
# 043

'''
direction = input("Do you want to count up or down: (u/d) ")
if direction == "u":
    num = int(input("What is the top number?"))
    for i in range(1, num+1):
        print(i)
elif direction == "d":
    num = int(input("Enter a number below 20:"))
    for i in range(20, num-1, -1):
        print(i)
else:
    print("I don't understand")
'''

# #################################################################
# 044
'''
num = int(input("How many friends do you want to invite to the party?"))
if num < 10:
    for i in range(0,num):
        name = input("Enter a name:")
        print(name, "has been invited")
else:
    print("Too many people")
    '''