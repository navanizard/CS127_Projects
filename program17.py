#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: October 15, 2024
#This program prints the days and hours left to the weekend when inputting hours.

hours = int(input("Enter number of hours: "))

days = hours // 24
hours_2 = hours % 24

print(f"Days: {days} ") 
print(f"Hours: {hours_2}")
