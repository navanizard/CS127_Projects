#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: September 27, 2024
#This program prints out a user-inputed message in revese twice.

myString = input("Enter a message: ")

lastIdx = len(myString) - 1 #Gets the index of the last character in the string.

for i in range(lastIdx, -1, -1): #Loops through all the characters - from the last index to the first (0).
    print(myString[lastIdx], myString[lastIdx]) #Prints the character twice with a space in between.
    lastIdx -= 1 #Gets the index of the next character.

#print((myString[lastIdx] + " ")*2)
