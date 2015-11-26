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
    for i in range(1):
        minval = arr[...,i].min()
        maxval = arr[...,i].max()
        if minval != maxval:
            arr[...,i] -= minval
            arr[...,i] *= (255.0/(maxval-minval))
    return arr

def demo_normalize():
    start = time.time()
    count = 0

    loadPath = "/Users/Carson/Desktop/training_set/original"
    savePath = "/Users/Carson/Desktop/training_set/norm"
    
    for x in range(10, 100):
        try:
            FILENAME = loadPath + "/" + str(x) + "_right.jpeg"
            img = Image.open(FILENAME).convert('RGB')
            arr=np.array(np.asarray(img).astype('float'))
            new_img = Image.fromarray(normalize(arr).astype('uint8'),'RGB')
            new_img.save(savePath + "/" + str(x) + "_right_norm.jpeg")

            FILENAME = loadPath + "/" + str(x) + "_left.jpeg"
            img = Image.open(FILENAME).convert('RGB')
            arr=np.array(np.asarray(img).astype('float'))
            new_img = Image.fromarray(normalize(arr).astype('uint8'),'RGB')
            new_img.save(savePath + "/" + str(x) + "_left_norm.jpeg")
        except: pass
        count += 1
        
        if count % 20 == 0:
            print("Count =" + str(count))
            print("Elapsed time = " + str(time.time() - start) + " seconds")
            print("Estimated time = " + str((time.time()-start)/float(count)*44340.0/60.0) + " minutes")

