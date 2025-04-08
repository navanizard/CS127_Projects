#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 19, 2024
#This program creates a topographic map 
#highlighting the points that have elevations that are multiples of 10.

import matplotlib.pyplot as plt
import numpy as np

elevations = np.loadtxt("elevationsNYC.txt")

mapShape = elevations.shape + (3,)
topoGraph = np.zeros(mapShape)

blue = float(input("How blue is the ocean?: ")) #float between 0.0 and 1.0
fileName = input("What is the output file name?: ")

for row in range(mapShape[0]):
    for col in range(mapShape[1]):

        if (elevations[row, col] <= 0):
            topoGraph[row, col, 2] = blue

        if (elevations[row, col] % 10 == 0):
            topoGraph[row, col, 0] = 0
            topoGraph[row, col, 1] = 0
            topoGraph[row, col, 2] = 0
        
        else:
            topoGraph[row, col, 0] = 1
            topoGraph[row, col, 1] = 1
            topoGraph[row, col, 2] = 1

plt.imshow(topoGraph)
plt.show()
# plt.imsave(fileName, topoGraph)

print("Thank you for using my program!")
print("Your map is stored as", fileName)