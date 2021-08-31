import math
from typing import MutableMapping

# ####################################################
# 027

'''
num = float(input("Enter a number with decimal places: "))
multiply = num * 2
print(multiply)
'''

# ####################################################
# 028
'''
num = float(input("Enter a number with lots of decimal places:"))
answer = num * 2
print(answer)
print(round(answer, 2))
'''


# ####################################################
# 029
'''
num = int(input("Enter a number over 500:"))
square = math.sqrt(num)
print(round(square, 2))
'''


# ####################################################
# 030
'''
pi = math.pi
print(round(pi, 5))
'''

# ####################################################
# 031

'''
radius = int(input("Enter the radius of a circle: "))
print((math.pi) * radius**2)
'''

# ####################################################
# 032

'''
radius = int(input("Enter the radius: "))
depth = int(input("Enter the depth: "))

volume = ((math.pi)* radius**2) * depth
print(round(volume, 3))
'''


# ####################################################
# 033
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

divider = num1 // num2
remainder = num1 % num2
print(num1, "divided by", num2, "is", divider, "with", remainder, "remaining")
'''

# ####################################################
# 034
'''
print("1) Square")
print("2) Triangle")
print()

menuselection = int(input("Enter a number: "))

if menuselection == 1:
    length = int(input("Enter the length: "))
    area = length * length
    print("Your square area is: ", area)
elif menuselection == 2:
    height = int(input("Enter the heigth: "))
    base = int(input("Enter the base: "))
    area = height * base
    print("Your triangle area is ", area)
'''

