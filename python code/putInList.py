from PIL import Image
import time
import pickle

#loadPath = "/Users/Carson/Dropbox/wammy+carson/final_project/cropped"
#savePath = "/Users/Carson/Dropbox/Wammy+Carson/final_project"

def putInList(loadPath, startIndex, end):
    
    start = time.time()
    count = 0


    outerList = []

    for x in range(int(startIndex), int(end+1)):
        try:
            FILENAME = loadPath + "/" + str(x) + "_right_resize.jpeg"
            img = Image.open(FILENAME).convert('RGB')
            innerList = list(img.getdata())
            for i in range(len(innerList)):
                if(type(innerList[i]) == type(int(1))):
                    print("found an int")
                innerList[i] = innerList[i][0]
            outerList.append(innerList)


            FILENAME = loadPath + "/" + str(x) + "_left_resize.jpeg"
            img = Image.open(FILENAME).convert('RGB')
            innerList = list(img.getdata())
            for i in range(len(innerList)):
                if(type(innerList[i]) == type(int(1))):
                    print("found an int")
                innerList[i] = innerList[i][0]
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

























