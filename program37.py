#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 26, 2024
#This program asks the user for a binary number and converts it to decimal.

binString = str(input("Enter a binary number: "))

decNum = 0

for c in binString:
    decNum = decNum * 2
    if c == "1":
        decNum = decNum + 1

print("Your number in decimal is: ", decNum)
























# dec = "" 
# for char in binString:
#     x = binString[char]
#     new_char = (char)*(2^x)
#     str(new_char)
#     dec += new_char

# print(dec)

