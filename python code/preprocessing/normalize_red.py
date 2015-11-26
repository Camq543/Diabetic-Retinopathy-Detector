import numpy as np
from PIL import Image
import time

def normalize(arr):
    """
    Linear normalization
    http://en.wikipedia.org/wiki/Normalization_%28image_processing%29
    """
    arr = arr.astype('float')
    #print(arr)

    # Do not touch the alpha channel
    minval = arr[...,0].min()
    maxval = arr[...,0].max()
    if minval != maxval:
        for row in range(len(arr)):
            for col in range(len(arr[row])):
                arr[row][col][0] -= minval
                arr[row][col][0] *= (255.0/(maxval-minval))


    return arr

def demo_normalize():
    FILENAME = "/Users/Carson/Desktop/final_project/image_org/" + str(10) + "_right.jpeg"
    img = Image.open(FILENAME).convert('RGB')
    arr=np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(normalize(arr).astype('uint8'),'RGB')
    new_img.save("/Users/Carson/Desktop/final_project/image_norm/" + str(10) + "_right_norm.jpeg")

    FILENAME = "/Users/Carson/Desktop/final_project/image_org/" + str(10) + "_left.jpeg"
    img = Image.open(FILENAME).convert('RGB')
    arr=np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(normalize(arr).astype('uint8'),'RGB')
    new_img.save("/Users/Carson/Desktop/final_project/image_norm/" + str(10) + "_left_norm.jpeg")

