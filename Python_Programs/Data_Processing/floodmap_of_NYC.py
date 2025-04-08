#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 19, 2024
#This program creates a floodmap of NYC using elevations data.

#import the libraries needed for numpy arrays and displaying images
import matplotlib.pyplot as plt
import numpy as np

#read the data to an array called "elevations"
elevations = np.loadtxt("elevationsNYC.txt")

#take the shape of elevations and add another dimension (the 3 color channels)
mapShape = elevations.shape + (3,)

#create another array that now has the color channels (all values set to 0):
floodMap = np.zeros(mapShape)

#loop through every pixel with an iterated for loop
for row in range(mapShape[0]):
    for col in range(mapShape[1]):

#grey area
        if (elevations[row, col] > 6) and (elevations[row, col] <= 20):
            floodMap[row, col, 0] = .5
            floodMap[row, col, 1] = .5
            floodMap[row, col, 2] = .5

#below sea level = blue
        elif (elevations[row, col] <= 0):
            floodMap[row, col, 2] = 1

#affected by the hurricane = red
        elif (elevations[row, col] <= 6):
            floodMap[row, col, 0] = 1

#everything else = green        
        else:
            floodMap[row, col, 1] = 1

# plt.imsave("floodMap.png", floodMap)
# plt.imshow(floodMap)
# plt.show()
