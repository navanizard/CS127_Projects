#Name: Nava Karine Nizard
#Email: nava.nizard12@myhunter.cuny.edu
#Date: November 19, 2024
#This program creates a blue C image on a 30x30 grid.

import matplotlib.pyplot as plt
import numpy as np

img = np.zeros((30,30,3)) #3 dimensions: A] rows/height B] colums/width C] color channels

height = img.shape[0]
width = img.shape[1]

#top and bottom thirds fully blue
img[:height//3, : , 2] = 1
img[2*height//3:, : , 2] = 1
img[:, :width//3, 2] = 1 

#make the white part of the C:
img[height//3:2*height//3, width//3:, 0] = 1
img[height//3:2*height//3, width//3:, 1] = 1
img[height//3:2*height//3, width//3:, 2] = 1



plt.imsave("logo.png", img)

# plt.imshow(img)
# plt.show()