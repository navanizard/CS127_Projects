
#Edited By: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: December 4, 2024
#This program draws nested triangles 
#Author: Professor Melissa Lynch

import turtle

def setUp(t, dist, col):
    """
    Takes three parameters, a turtle, t, the distance, dist, 
    to move the turtle and a color, col, to set the turtle's color.
    """
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)


def triangle(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 3 times:  moves forward that length, turns 120 degrees, 
    and calls triangle(t, length/2).
    """
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length/2)
    


def nestedTriangle(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 3 times:  moves forward that length, turns 120 degrees, 
    and calls triangle(t, length/2).
    """
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t, length/2)     


def main():
    n = int(input('Enter length: '))

    tom = turtle.Turtle()
    setUp(tom, -100, "darkgreen")
    triangle(tom, n)

    tess = turtle.Turtle()
    setUp(tess, 100, "steelblue")
    nestedTriangle(tess, n)

if __name__ == "__main__":
     main()
     
          