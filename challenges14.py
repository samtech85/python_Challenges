# Reading and writing to a .csv file
import csv

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



######################################################################
# 117