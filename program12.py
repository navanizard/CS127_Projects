#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: September 25, 2024
#This program prints draws a cornflower-blue pentagon using the turtle library.

import turtle

#Set up the turtle
turtle.colormode(255)
thomasH = turtle.Turtle()
thomasH.shape("turtle")
thomasH.color(100,149,237)

#Draw the shape
for i in range(5):
    thomasH.forward(100)
    thomasH.left(360/5)
    thomasH.stamp() #Stamps the turtle shape
    
