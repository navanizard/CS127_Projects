#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: December 4, 202


#Sample program that loops from 2 to 22
ADDI $s0, $zero, 0 #set s0 to 0
ADDI $s1, $zero, 2  #use to increment counter, $s0
ADDI $s2, $zero, 20  #set breakoff
AGAIN: ADD $s0, $s0, $s1
BEQ $s0, $s2, DONE
J AGAIN
DONE:  #To break out of the loop