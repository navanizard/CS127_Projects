#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 7, 2024
#This program accepts a user-inputted png file and ourputs a copy of it will only the blue channel turned on.

import matplotlib.pyplot as plt
import numpy as np

input_file = input("Enter name of the input file: ")
output_file = input("Enter name of the output file: ")


img = plt.imread(input_file)
#plt.imshow(img)
#plt.show()

img2 = img.copy()

img2[:, :, 0] = 0 #red channel set to zero
img2[:, :, 1] = 0 #green channel set to zero

plt.imsave(output_file, img2)

#plt.imshow(img2)
#plt.show()