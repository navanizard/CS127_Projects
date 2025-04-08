#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: December 4, 2024
#This program validates the user's input such that they are required to enter a non-negative integer.

#num can be 0-infinity


num = int(input("Enter a non-negative integer: "))

while num < 0:
    print("You entered a negative number. Try again.")
    num = int(input("Enter a non-negative integer: "))

print(num)

# while True:
#     num = int(input("Enter a number: "))

#     if num < 0:
#         print("Negative integer. Try again.")
    
#     else: 
#         print(num)
#         break
    