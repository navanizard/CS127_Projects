#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: September 19, 2024
#This program prompts the user to enter a phrase and prints the ASCII code of each character.

phrase = input("Enter a phrase: ")

print("In ASCII:")

for char in phrase:
    print(ord(char))
