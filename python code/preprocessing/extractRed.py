import numpy as np
from PIL import Image
import time

def normalize(arr):
    """
    Linear normalization
    http://en.wikipedia.org/wiki/Normalization_%28image_processing%29
    """
    arr = arr.astype('float')
    # Do not touch the alpha channel
    for i in range(3):
        minval = arr[...,i].min()
        maxval = arr[...,i].max()
        if minval != maxval:
            arr[...,i] -= minval
            arr[...,i] *= (255.0/(maxval-minval))
    return arr

def extract_red(arr):
    start = time.time()
    newList = []
    for row in arr:
        for col in row:
            newList.append(col[0])
    print(time.time() - start)
    return newList

def is_Black(pixel):
    for color in pixel:
        if color != 0:
            return False
    return True

def demo_normalize():
        FILENAME = "/Users/Carson/Desktop/training_set/original/" + str(10) + "_right.jpeg"
        img = Image.open(FILENAME, 'r')
        arr=np.array(np.asarray(img).astype('float'))
        redList = extract_red(arr)
        normalize(arr)
        extract_red(arr)
        
            
demo_normalize()