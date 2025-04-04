#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 27, 2024
#This program makes a turtle move 100 times, rotating at randomly chose angles.

import turtle
import random

t = turtle.Turtle()

for i in range(100):
    t.forward(30)
    t.left(random.randrange(0, 360, 10))
    