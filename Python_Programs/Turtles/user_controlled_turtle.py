#Author: Katherine St. John
#Date: August 2014
#A program that uses command strings to control turtle drawing
#Modified by:  Nava Karine Nizard
#Date: October 28, 2024.

import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     #The graphics window
commands = input("Please enter a command string: ")

for ch in commands:
    #perform action indicated by the character
    if ch == 'F':            #move forward
        tess.forward(50)
    elif ch == 'L':          #turn left
        tess.left(90)
    elif ch == 'R':          #turn right
        tess.right(90)
    elif ch == '^':          #lift pen
        tess.penup()
    elif ch == 'v':          #lower pen
        tess.pendown()
    elif ch == 'B':            #move backward
        tess.backward(50)
    elif ch == 'S':          #stamps a turtle
        tess.stamp()
    elif ch == 'l':          #turn left
        tess.left(45)
    elif ch == 'r':          #turn right
        tess.right(45)
    elif ch == 'p':          #pen color purple
        tess.pencolor('purple')
    else:                   #for any other character, print an error message 
        print("Error: do not know the command:", ch)

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked




