# Numeric Arrays
from array import *
import random
import math
# ####################################################################
# 088

'''nums = array('i', [])

for i in range(0,5):
    num = int(input("Enter a number: "))
    nums.append(num)

nums = sorted(nums)
nums.reverse()
print(nums)'''

# ####################################################################
# 089

'''nums = array('i', [])
for i in range(0, 5):
    num = random.randint(1,100)
    nums.append(num)
for i in nums:
    print(i)
'''

# ####################################################################
# 090
'''nums = array("i", [])
while len(nums) < 5:
    num = int(input("Enter a number between 10 and 20: "))
    if num >= 10 and num <= 20:
        nums.append(num)
    else:
        print("Outside the range")

for i in nums:
    print(i)'''


# ####################################################################
# 091
'''nums = array('i', [5, 7, 9, 2, 9])

for i in nums:
    print(i)
num = int(input("Enter a number: "))
if nums.count(num) == 1:
    print(num, "is in the list once")
else:
    print(num, "is in the list", nums.count(num), "times")'''
# ####################################################################
# 092
'''num1 = array('i', [])
num2 = array('i', [])

for i in range(0,3):
    num = int(input("Enter a number: "))
    num1.append(num)

for i in range(0,5):
    num = random.randint(1,100)
    num2.append(num)

num1.extend(num2)

num1 = sorted(num1)

for i in num1:
    print(i)'''


# ####################################################################
# 093
'''nums = array("i", [])
for i in range(0,5):
    num = int(input("Enter a number: "))
    nums.append(num)

nums = sorted(nums)

for i in nums:
    print(i)

num = int(input("Select a number from the array: "))
if num in nums:
    nums.remove(num)
    num2 = array("i", [])
    num2.append(num)
    print(nums)
    print(num2)
else:
    print("That is not a value in the array: ")'''


# ####################################################################
# 094
'''nums = array('i', [4,6,8,2,5])

for i in nums:
    print(i)
    num = int(input("Select one of the numbers: "))

tryagain = True
while tryagain == True:
    if num in nums:
        print("This is in position", nums.index(num))
        tryagain = False
    else:
        print("Not in array")
        num = int(input("Select one of the numbers: "))'''


# ####################################################################
# 095

'''nums = array('f', [34.75, 27.23, 99.58, 45.26, 28.65])
tryagain = True
while tryagain == True:
    num = int(input("Enter a number between 2 and 5: "))
    if num < 2 or num > 5:
        print("Incorrect value, try again.")
    else:
        tryagain = False
    for i in range(0,5):
        ans = nums[i]/num

        print(round(ans,2))'''