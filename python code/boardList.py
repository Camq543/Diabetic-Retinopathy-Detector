from PIL import Image
import numpy as np
import time

#blockLen is the width len of the amount of blocks you want (5 will give you 25 blocks)
def getBlockList(loadPath, startIndex, end, blockLen):
    
    start = time.time()
    count = 0


    outerList = []

    for x in range(int(startIndex), int(end+1)):
        try:
            FILENAME = loadPath + "/" + str(x) + "_right_resize.jpeg"
            img = Image.open(FILENAME).convert('RGB')
            innerList = list(img.getdata())
            innerList = getBlock(innerList, blockLen, img.size[0])
            outerList.append(innerList)


            FILENAME = loadPath + "/" + str(x) + "_left_resize.jpeg"
            img = Image.open(FILENAME).convert('RGB')
            innerList = list(img.getdata())
            innerList = getBlock(innerList, blockLen, img.size[0])
            outerList.append(innerList)
        
            count += 1
        except IOError: pass
       
        
        #if count % 20 == 0:
        #    print("Count =" + str(count))
        #    print("Elapsed time = " + str(time.time() - start) + " seconds")
        #    #print("Estimated time = " + str((time.time()-start)/float(count)*2000.0/60.0) + " minutes")
        #    print("Estimated time = " + str((time.time()-start)/float(x)*(float(end-start))/60.0) + "minutes")

    #print(time.time() - start)
    print("\nDone inserting")

    return outerList

def getBlock(innerList, length, size):
    outerList = []
    step = size/length
    for i in range(length):
        for j in range(length):
            block = []
            for x in range(i*step, i*step+step):
                for y in range(j*step, j*step+step):
                    block.append(innerList[x*size+y][0])
            outerList.append(getAvg(block))
    return outerList

def getAvg(l):
    return sum(l)/len(l)
























