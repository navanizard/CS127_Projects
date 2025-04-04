#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 19, 2024
#This program takes in a list of names and outputs the initial of the first name followed by the lastname.

names = input("Please enter your list of names: ")
fullNames = names.split("; ")

print("You entered: ")

for name in fullNames:
    lastName, firstName = name.split(", ")
    print(firstName[0] + ".", lastName)
    

print("Thank you for using my name organizer! ")
