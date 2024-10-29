#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: October 8, 2023
#This program encripts user input using a ceasar cipher with a right shift of 13. Only accepts lowercase letters.
#The coding method involves shifting each character based on its position in the alphabet.

message = input("Enter a word: ")

coded_message = ""

for char in message:
    
    offset = ord(char) - ord('a') + 13
    wrap = offset % 26

    new_char = chr(ord('a') + wrap)

    coded_message = coded_message + new_char

print("Your word in code is: ", coded_message)
