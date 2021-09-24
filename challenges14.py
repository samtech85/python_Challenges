# Reading and writing to a .csv file
import csv
import random
######################################################################
# 111

'''file = open("Books.csv", "w")
newRecord = "To kill a Mockingbird, Harper Lee, 1960\n"
file.write(str(newRecord))

newRecord = "A Brief of Time, Stephen Hawking, 1988\n"
file.write(str(newRecord))

newRecord = "The Great Gatsby,Scott Fitzgerald, 1922\n"
file.write(str(newRecord))

newRecord = "The Man who Mistook His wife for a Hat, Oliver Sacks, 1813\n"
file.write(str(newRecord))

file.close()
'''
######################################################################
# 112

'''
file = open("Books.csv", "w")
title =input("Enter a title: ")
author = input("Enter author: ")
year = input("Enter the year it was released: ")

newRecord = title + ", " + author + ", " + year + "\n"

file.write(str(newRecord))
file.close()

file = open("Books.csv", "r")
for row in file:
    print(row)
file.close()'''

######################################################################
# 113
'''num = int(input("How many books do you want to add to the list? "))
file = open("Books.csv", "a")
for x in range(0, num):
    title = input("Enter a title: ")
    author = input("Enter author: ")
    year = input("Enter the year it was released: ")
    newRecord = title + ", " + author + ", " + year + "\n"
    file.write(str(newRecord))
file.close() 
searchauthor = input("Enter an authors name to search for: ")
file = open("Books.csv", "r")
count = 0

for row in file:
    if searchauthor in str(row):
        print(row)
        count += 1

    if count == 0:
        print("There are no books by that author in this list.")
file.close()'''


######################################################################
# 114
'''start = int(input("Enter a starting year:"))
end = int(input("Enter an end year: "))
file = list(csv.reader(open("Books.csv")))
tmp = []

for row in file:
    tmp.append(row)

x = 0
for row in file:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
        print(tmp[x])
    x += 1'''


######################################################################
# 115
'''file = open("Books.csv", "r")
x = 0
for row in file:
    display = "Row: " + str(x) + " - " + row
    print(display)

x += 1'''

######################################################################
# 116
'''
file = list(csv.reader(open("Books.csv")))
booklist = []
for row in file:
    booklist.append(row)

x = 0
for row in booklist:
    display = x, booklist[x]
    print(display)
    x+=1

getrid = int(input("Enter a row number to delete: "))
del booklist[getrid]

x = 0
for row in booklist:
    display = x, booklist[x]
    print(display)
    x += 1
    alter = int(input("Enter a row number to alter: "))

x = 0
for row in  booklist:
    display = x, booklist[alter][x]
    print(display)
    x += 1

part = int(input("Which part do you wat to change? "))
newdata = input("Enter new data: ")
booklist[alter][part] = newdata
print(booklist[alter])

file = open("Books.csv", 'w')
x = 0
for row in booklist:
    newrecord = booklist[x][0] + ", " + booklist[x][1] +", " + booklist[x][2] + "\n"

    file.write(newrecord)
    x = x + 1
    file.close()'''


######################################################################
# 117

score = 0
name = input("What is your name: ")
q1_num1 = random.randint(10,50)
q1_num2 = random.randint(10,50)

question1 = str(q1_num1) + " + " + str(q1_num2) + " = "
ans1 = int(input(question1))
realans1 = q1_num1 + q1_num2
if ans1 == realans1:
    score = score + 1
q2_num1 = random.randint(10, 50)
q2_num2 = random.randint(10, 50)

question2 = str(q2_num1) + " + " + str(q2_num2) + " = "
ans2 = int(input(question2))
realans2 = q2_num1 + q2_num2
if ans2 == realans2:
    score += 1


file = open("QuizScore.csv", "a")
newrecord = name + ", " + question1 + "," + str(ans1) + ", " + question2 + ", " + str(score) + "\n"

file.write(str(newrecord))
file.close()