#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 26, 2024
#This program prints out 10 worst violators of a user-inputted csv file.

import pandas as pd
import numpy as np

file = input("Enter file name: ")
attr = input("Enter attribute: ")

tickets = pd.read_csv(file)

print(tickets[attr].value_counts()[:10]) #Print 10 worst and number of tickets based on attr

print("The top 10 worst offenders are: ")

