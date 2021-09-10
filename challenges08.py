from turtle import *
import turtle
import random

# turtle

# ####################################################################
# 060
'''
turtle.shape("turtle")
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()'''

# ####################################################################
# 061
'''
turtle.shape("turtle")
for i in range(0,3):
    turtle.forward(120)
    turtle.right(120)
turtle.exitonclick()
'''
# ####################################################################
# 062
'''
turtle.hideturtle()
for i in range(0, 360):
    turtle.forward(2)
    turtle.right(1)
turtle.exitonclick()
'''


# ####################################################################
# 063

'''turtle.color("black", "green")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "blue")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick()
'''

# #####################################################################
# 064

'''for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()'''

# #####################################################################
# 065

'''
# One
turtle.left(90)
turtle.forward(100)
turtle.right(90)

#  Two
turtle.penup()
turtle.forward(50)
turtle.pendown()

turtle.forward(75)
turtle.right(90)
turtle.forward(50)

turtle.right(90)
turtle.forward(75)
turtle.left(90)

turtle.forward(50)
turtle.left(90)
turtle.forward(75)

# three
turtle.penup()
turtle.forward(50)
turtle.pendown()

turtle.forward(75)
turtle.left(90)
turtle.forward(50)

turtle.left(90)
turtle.forward(75)
turtle.left(180)

turtle.forward(75)
turtle.left(90)
turtle.forward(50)

turtle.left(90)
turtle.forward(75)
turtle.hideturtle()

turtle.exitonclick()
'''
######################################################################
# 066

'''
turtle.pensize(3)

for i in range(0,8):
    turtle.color(random.choice(["red", "blue", "yellow", "green", "pink", "orange"]))
    turtle.forward(50)
    turtle.right(45)
turtle.exitonclick()
'''
######################################################################
# 067

'''for x in range(0,10):
    # turtle.color(random.choice(["red", "blue", "yellow", "green", "pink", "orange","black"]))
    for i in range(0,8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)
'''

######################################################################
# 068

'''
lines = random.randint(5,20)

for x in range(0,lines):
    length = random.randint(25,100)
    rotate = random.randint(1, 365)
    turtle.forward(length)
    turtle.right(rotate)

turtle.exitonclick()
'''