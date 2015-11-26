import radius_2 as radius
from normalize import normalize
import numpy as np
import PIL
from PIL import Image
import time

def resizeImages():
    loadPath = "/Volumes/EXTRA/training_set/original"
    savePath = "/Volumes/EXTRA/training_set/resized"
    savePathNorm = "/Volumes/EXTRA/training_set/resized_norm"

    start = time.time()
    count = 1

    newSize = 500

    for x in range(15757, 46000):
        try:
            FILENAME = loadPath + "/" + str(x) + "_right.jpeg"
            new_img, new_img_norm = cropAndResize(FILENAME, newSize)
            #save both images
            new_img.save(savePath + "/" + str(x) + "_right_resize.jpeg")
            new_img_norm.save(savePathNorm + "/" + str(x) + "_right_resize_norm.jpeg")

            FILENAME = loadPath + "/" + str(x) + "_left.jpeg"
            new_img, new_img_norm = cropAndResize(FILENAME, newSize)
            #save both images
            new_img.save(savePath + "/" + str(x) + "_left_resize.jpeg")
            new_img_norm.save(savePathNorm + "/" + str(x) + "_left_resize.jpeg")
        
            count += 1
        except: pass
       
        
        if count % 20 == 0:
            print("Count =" + str(count))
            print("Elapsed time = " + str(time.time() - start) + " seconds")
            print("Estimated time = " + str((time.time()-start)/float(count)*40000.0/60.0) + " minutes")

def cropAndResize(FILENAME, newSize):
    img = Image.open(FILENAME).convert('RGB')
    arr=np.array(np.asarray(img).astype('float'))
    upperLeft, bottomRight = radius.get_corners(radius.get_radius(img, arr), img.size)

    #crop array to space we want
    arr = arr[upperLeft[1]:bottomRight[1], upperLeft[0]:bottomRight[0]]
    #make new image
    new_img = Image.fromarray(arr.astype('uint8'),'RGB')
    new_img = new_img.resize((newSize,newSize))

    #get the image we just saved into an array, normalize it, then make it again
    arr=np.array(np.asarray(new_img).astype('float'))
    normalize(arr)
    new_img_norm = Image.fromarray(arr.astype('uint8'),'RGB')
    
    return new_img, new_img_norm

resizeImages()

