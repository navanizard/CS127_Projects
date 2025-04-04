#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 20, 2024
#This program converts the amount of seconds left until a lecture into hours, minutes, and seconds.

seconds = int(input("Enter the amount of seconds until the lecture starts: "))

hours = seconds // 3600
rem_secs = seconds % 3600

minutes = rem_secs // 60
rem_secs2 = rem_secs % 60

print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", rem_secs2)