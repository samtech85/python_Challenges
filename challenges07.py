# Random
import random
# ##################################################################
# 52
'''
print(random.randrange(1,100))
'''

# ##################################################################
# 53
'''
fruit = ["Mango", "pineaple", "apple", "banana"]
print(random.choice(fruit))
'''

# ##################################################################
# 54
'''
print("Choose Head or Tail (h /t)")
game = ['t','h']
user_Choice = input("Your choice: ")
computer_choice = random.choice(game)

print(user_Choice)
if user_Choice == computer_choice:
    print("You win")
else:
    print("Bad luck")
'''
# ##################################################################
# 55
'''
print("Choose a number between 1 and 5")
num = int(input("Choose a number: "))
computer_choice = random.randint(1,5)
if num == computer_choice:
    print("Well done")
elif num > computer_choice:
    print("Too high")
    num = int(input("A number again? :"))
    if num == computer_choice:
        print("Correct")
    else:
        print("You lose")
elif num < computer_choice:
    print("Too low")
    num = int(input("Do you wanna try another: "))
    if num == computer_choice:
        print("Correc")
    else:
        print("You loose")
'''

# ##################################################################
# 56
'''
num = random.randint(1,10)

correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True
        print("You win")
'''

# ##################################################################
# 57

'''
num = random.randint(1,10)

correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True
    elif guess > num:
        print("Too high")
    else:
        print("Too low")
'''

# ##################################################################
# 58

'''
score = 0
for i in range(1,6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct = num1 + num2
    print(num1, "+", num2,"= ")
    answer = int(input("Your answer: "))
    print()
    if answer == correct:
        score = score + 1
print("You scored", score, "/ 5")
'''

# ##################################################################
# 59
'''
colour = random.choice(["red", "blue","green", "white", "Pink"])
print("Select from red, blue, green, white or pink")

tryagain = True
theirchoice = input("Enter a colour: ")
theirchoice = theirchoice.lower()
if colour == theirchoice:
    print("Well done")
    tryagain = False
else:
    if colour == "red":
        print("I bet you are seeing RED right now.")
    elif colour == "blue":
        print("Don't feel BLUE.")
    elif colour == "green":
        print("I bet you are GREEN  with envy right now.")
    elif colour == "white":
        print("Are you WHITE as a sheet, as you didn't guess correctly?")
    elif colour == "pink":
        print("Shame you are not feeling in the PINK, as you got it wrong!")
'''

