#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 19, 2024
#This program asks the user for the borough, a name for the output file, 
#and then displays the fraction of the population that has lived in that borough as a plot.

import matplotlib.pyplot as plt
import pandas as pd

boro = input("Please enter a borough: ")
fileName = input("Please enter output file name: ")

#read csv file and store it in "pop"
pop = pd.read_csv("nycHistPop.csv", skiprows= 5)

pop["Fraction"] = pop[boro]/pop["Total"]

#creat a plot with the year as the x-axis and the fraction of the pop as the y-axis
pop.plot(x = "Year", y = "Fraction")

#create a new figure and save it to name fileName
fig = plt.gcf()
fig.savefig(fileName)
plt.show()