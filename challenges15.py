from os import name, openpty
import random
import csv
# Subprograms
# #######################################################
# 118
'''def ask_value():
    num = int(input("Enter a number: "))
    return num
def count(num):
    n = 1
    while n <= num:
        print(n)
        n = n + 1

def main():
    num = ask_value()
    count(num)

main()'''


# #######################################################
# 119
'''def pick_num():
    low = int(input("Enter the bottom of the range: "))
    high = int(input("Enter the top of the range: "))
    comp_num = random.randint(low, high)
    return comp_num


def first_guess():
    print("I am thinking of a number...")

    guess = int(input("What am I thinking of: "))
    return guess

def check_answer(comp_num, guess):
    try_again = True
    while try_again == True:
        if comp_num == guess:
            print("Correct, you win.")
            try_again = False

        elif comp_num > guess:
            guess = int(input("Too low, try again: "))
        else:
            guess = int(input("Too high, try again: "))


def main():
    comp_num = pick_num()
    guess = first_guess()
    check_answer(comp_num, guess)

main()'''


# #######################################################
# 120

'''def addition():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print(num1, "+", num2, "=")
    user_answer = int(input("Your answer: "))
    actuel_answer = num1 + num2
    answer = (user_answer, actuel_answer)
    return answer


def subtraction():
    num3 = random.randint(25, 50)
    num4 = random.randint(1, 25)

    print(num3, "-", num4, "= ")
    user_answer = int(input("Your answer: "))
    actuel_answer = num3 - num4
    answer = (user_answer, actuel_answer)

    if user_answer == actuel_answer:
        print("Correct")
    else:
        print("Incorrect, the answer is", actuel_answer)


def check_answer(user_answer, actual_answer):
    if user_answer == actual_answer:
        print("Correct")
    else:
        print("Incorrect, the answer is", actual_answer)


def main():
    print("1) Addition")
    print("2) Subtraction")
    selection = int(input("Enter 1 or 2: "))
    if selection == 1:
        user_answer, actual_answer = addition()
        check_answer(user_answer, actual_answer)
    elif selection == 2:
        user_answer, actual_answer = subtraction()
        check_answer(user_answer, actual_answer)
    else:
        print("Incorrect selection")

main()

'''
# #######################################################
# 121
'''
def add_name():
    name = input("Enter a new name: ")
    names.append(name)
    return names

def change_name():
    num = 0
    for x in names:
        print(num, x)
        num += 1
    select_num = int(input("Enter the number of the name you want to change: "))
    name = int(input("Enter new name: "))
    names[select_num] = name

    return names

def delete_name():
    num = 0
    for x in names:
        print(num,x)
        num = num + 1
    select_num = int(input("Enter the number of the name you want to delete: "))
    del names[select_num]
    return names

def view_names():
    for x in names:
        print(x)
    print()

def main():
    again = "y"
    print("1) Add a name")
    print("2)change a name")
    print("3) Delete a name")
    print("4) View names")
    print("5) Quit")

    selection = int(input("What do you want to do: "))

    if selection == 1:
        names = add_name()
    elif selection == 2:
        names = change_name()
    elif selection == 3:
        names = delete_name()
    elif selection == 4:
        names = view_names()
    elif selection == 5:
        again = 'n'
    else:
        print("incorrect option: ")
    data = (names, again)

names =[]
main()
'''


# #######################################################
# 122

'''def addtofile():
    file = open("Salaries.csv", "a")
    name = input("Enter a name: ")
    salary = int(input("Enter salary: "))
    newrecord = name + ", " + str(salary) + "\n"
    file.write(str(newrecord))
    file.close()

def viewrecords():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()

tryagain = True
while tryagain == True:
    print("1) Add to file")
    print("2) View all records")
    print("3) Quit program")
    print()
    selection = input("Enter the number of your selection: ")

    if selection == "1":
        addtofile()
    elif selection == "2":
        viewrecords()
    elif selection == "3":
        tryagain = False        
    else:
        print("Incorrect option")'''

# #######################################################
# 123

def addtofile():
    file = open("Salaries.csv", "a")
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    newrecord = name + ", " + str(salary) + "\n"
    file.close()

def viewrecord():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()

def deleterecord():
    file = open("Salaries.csv", "r")
    x = 0
    tmplist = []
    for row in tmplist:
        print(x, row)
        x += 1
    rowtodelete = int(input("Enter the row to delete: "))
    del tmplist[rowtodelete]
    file = open("Salaries.csv", "w")
    for row in tmplist:
        file.write(row)
        file.close()


tryagain = True
while tryagain == True:
    print("1) Add to file")
    print("2) View all records")
    print("3) Delete a records")
    print("4) Quit program")
    print()

    selection = input("Enter the number of your selection: ")
    if selection == "1":
        addtofile()
    elif selection == "2":
        viewrecord()
    elif selection == "3":
        deleterecord()
    elif selection == "4":
        tryagain = False
    else:
        print("Incorrect option")
