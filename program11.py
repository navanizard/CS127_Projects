#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: September 24, 2024
#This program draws a shape gradually getting bigger and brighter in blue.

import turtle

turtle.colormode(255) #Changes the color mode to be given in values from 0 to 255

thomasH = turtle.Turtle()
thomasH.shape("turtle") #Makes the turtle turtle-shaped

thomasH.backward(100) #Moves the turtle backwards to give more space 

for i in range(0,255,10):
    thomasH.forward(10)
    thomasH.pensize(i) #Sets the drawing size to be i (getting larger)
    thomasH.color(0,0,i) #Sets the blue channel to be i (getting brighter)
