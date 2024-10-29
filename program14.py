#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: September 30, 2024
#This program asks users for 5 values and rotates the turtle x degrees left.

import turtle

nums = []
for i in range(5):
    nums.append(int(input("Enter a number: ")))


t = turtle.Turtle()

for num in nums:
    t.left(num)
    t.forward(100)


