#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 7, 2024
#This program uses data from a csv file to compute the min, avg, and max populations of a user-inputter borough.


import pandas as pd

boro = input("Enter a borough: ")

pop = pd.read_csv("nycHistPop.csv", skiprows=5)

min_pop = pop[boro].min()
avg_pop = pop[boro].mean()
max_pop = pop[boro].max()

print("Minimum population: ", min_pop)
print("Average population: ", avg_pop)
print("Maximum population: ", max_pop)