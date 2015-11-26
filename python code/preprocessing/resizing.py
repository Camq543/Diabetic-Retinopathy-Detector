import radius_2 as radius
from normalize import normalize
import numpy as np
import PIL
from PIL import Image
import time

def resizeImages():
    loadPath = "/Volumes/Seagate Backup Plus Drive/training_set/original"
    savePath = "/Users/Carson/Desktop/cropped"

    start = time.time()
    count = 0

    newSize = 500

    for x in range(10, 40000):
        try:
            FILENAME = loadPath + "/" + str(x) + "_right.jpeg"
            new_img = cropAndResize(FILENAME, newSize)
            new_img.save(savePath + "/" + str(x) + "_right_resize.jpeg")

            FILENAME = loadPath + "/" + str(x) + "_left.jpeg"
            new_img = cropAndResize(FILENAME, newSize)
            new_img.save(savePath + "/" + str(x) + "_left_resize.jpeg")
        
            count += 1
        except: pass
       
        
        if count % 20 == 0:
            print("Count =" + str(count))
            print("Elapsed time = " + str(time.time() - start) + " seconds")
            print("Estimated time = " + str((time.time()-start)/float(count)*4000.0/60.0) + " minutes")

        if count >= 2000: break

    print(time.time() - start)

def cropAndResize(FILENAME, newSize):
    img = Image.open(FILENAME).convert('RGB')
    arr=np.array(np.asarray(img).astype('float'))
    upperLeft, bottomRight = radius.get_corners(radius.get_radius(img, arr), img.size)

    arr = arr[upperLeft[1]:bottomRight[1], upperLeft[0]:bottomRight[0]]
    new_img = Image.fromarray(arr.astype('uint8'),'RGB')
    new_img = new_img.resize((newSize,newSize))
    
    return new_img

resizeImages()

