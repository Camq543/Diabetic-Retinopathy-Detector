import numpy as np
from PIL import Image
import time

def get_sizes():
   start = time.time()
   count = 1
   sizes = []
   for x in range(10, 44350):
     try:
         FILENAME = "/Volumes/EXTRA/training_set/original/" + str(x) + "_right.jpeg"
         img = Image.open(FILENAME, 'r')
         sizes.append(img.size[0]*img.size[1])

         FILENAME = "/Volumes/EXTRA/training_set/original/" + str(x) + "_left.jpeg"
         img = Image.open(FILENAME, 'r')
         sizes.append(img.size[0]*img.size[1])
         
     except: pass
     count += 1
     if count % 1000 == 0:
         print("Count =" + str(count))
         print("Elapsed time = " + str(time.time() - start) + " seconds")
         print("Estimated time = " + \
          str((time.time()-start)/float(count)*(44340.0-float(count))) + " seconds")

   return sizes

def get_avg(sizes):
   total = 0
   for x in sizes:
      total += x
   return total/float(len(sizes))

sizes = get_sizes()
print("Max is: " + str(max(sizes)))
print("Min is: " + str(min(sizes)))
print("Avg is: " + str(get_avg(sizes)))