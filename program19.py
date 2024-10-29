#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: October 21, 2024
#This program counts and prints the GC-content in a DNA string.

DNA = input("Enter a DNA string: ")

gCount = DNA.count('G')
cCount = DNA.count('C')

added = gCount + cCount

long = len(DNA)

GCcont = added / long


print(f"Lentgh is {long}")
print(f"GC-Content is {GCcont}")


#count = 0
#for char in DNA:
    #if char == 'G' or char == 'C':
        #count += 1
        
