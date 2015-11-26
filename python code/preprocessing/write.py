import radius_2 as radius
import normalize as norm
import numpy as np
from PIL import Image
import time

def write_to_file(image, arr, outfile, color):
    upperLeft, bottomRight = radius.get_corners(radius.get_radius(image, arr), image.size)


    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i < upperLeft[1] and i > bottomRight[1] and j < bottomRight[0] and j > upperLeft[0]:
                outfile.write(str(arr[i][j][color]))
                outfile.write(",")
    outfile.write("\n")
