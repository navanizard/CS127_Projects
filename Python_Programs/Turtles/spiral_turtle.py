#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 19, 2024
#This program creates a spiral-shaped turtle.

import turtle

t = turtle.Turtle()

for i in range(90, -1, -2):
    t.forward(25)
    t.left(i)