#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: October 16, 2024
#This program prints counts and print number of pixels that are nearly white in a user-inputted image.

import matplotlib.pyplot as plt
import numpy as np

file = input("Enter file name: ")
img = plt.imread(file)

countSnow = 0
n = 0.75

for rows in range(img.shape[0]): #Accessing the dimension at index 0: Rows
    for col in range(img.shape[1]): #Accessing the dimension at index 1: Columns
        #Check if red,green,blue are > n
        if (img[rows, col, 0] >  n) and (img[rows, col, 1] > n) and (img[rows, col, 2] > n):
            countSnow +=1


print("Snow count is ", countSnow)
