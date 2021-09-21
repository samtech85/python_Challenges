# 2D Lists and dictionnary


######################################################################
# 096

table = [[2, 5, 8], [3, 7, 4], [4, 2, 0], [2,5,2]]

######################################################################
# 097
'''print(table)

get_row = int(input("Select a row: "))
get_col = int(input("Select a column: "))
print(table[get_row][get_col])'''

######################################################################
# 098
'''print(table)
get_row = int(input("Which row would you like: "))
print(table[get_row])
get_value = int(input("Add another value to your row: "))
table[get_row].append(get_row)

print(table[get_row])'''

######################################################################
# 099

'''print(table)
get_row = int(input("Which row do you like to display: "))
get_col = int(input("Which column do you like to display: "))
print(table[get_row][get_col])

change_value = input("would you like to change the value (y/n): ")
if change_value == 'y':
    newValue = int(input("Enter the new value: "))
    table[get_row][get_col] = newValue
    print(table[get_row])

else:
    print("Thank you!")'''
    

######################################################################
# 100

'''sales = {
    "John": {
        "N": 3056,
        "S":8463,
        "E":8441,
        "W":2694  
    },
    "Tom": {
        "N": 4832,
        "S":6786,
        "E":4737,
        "W":3612  
    },
    "Anne": {
        "N": 5239,
        "S":4802,
        "E":5820,
        "W":1859  
    },
    "Fiona": {
        "N": 3904,
        "S":3645,
        "E":8821,
        "W":1251  
    }
}'''

######################################################################
# 101
'''person = input("Enter sales person's name: ")
region = input("Select region: ")
print(sales[person][region])
newdata = int(input("Enter new data: "))
sales[person][region] = newdata

print(sales[person])'''

######################################################################
# 102

'''list = {}
for i in range(0,4):
    name = input("Enter a name: ")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {
        "Age": age,
        "Shoe size": shoe,
        }
for i in list:
    print((name), list[name]["Age"])'''

######################################################################
# 103

'''list = {}
for i in range(0,4):
    name = input("Enter name:")
    age = int(input("Enter age: "))
    shoe = int(input("Enter shoe size: "))
    list[name] = {
        "Age": age,
        "Shoe size": shoe,
    }
    getrid = input("Who do you want to remove from the list: ")
    del list[getrid]

for name in list:
    print((name), list[name]["Age", list[name]["Shoe size"]])

'''
