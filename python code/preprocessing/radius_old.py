import numpy as np
from PIL import Image
import time

def get_radius(img, arr):

   midHeight = img.size[1]//2
   blackBef = True
   start = 0
   end = img.size[0]
   #hold onto previous 3 values to correct for noise
   for pixI in range(len(arr[midHeight])):
      if(blackBef):
        print("0"),
        if not is_Black(arr[midHeight][pixI]):
          start = pixI
          blackBef = False
      else:
        print("1"),
        if is_Black(arr[midHeight][pixI]):
          end = pixI
          blackBef = True

   return (end - start)//2, start, end

def is_Black(pixel):
    colors = []
    for color in pixel:
        colors.append(color)
    if max(colors) < 5: return True
    return False

def check_all_radii():
  start = time.time()
  bad = []
  count = 0
  for x in range(10, 44350):
    try:
        FILENAME = "/Users/Carson/Desktop/training_set/original/" + str(x) + "_right.jpeg"
        img = Image.open(FILENAME).convert('RGB')
        arr=np.array(np.asarray(img).astype('float'))
        rad = get_radius(img, arr)
        if rad < 50: print(x)
 

        FILENAME = "/Users/Carson/Desktop/training_set/original/" + str(x) + "_left.jpeg"
        img = Image.open(FILENAME).convert('RGB')
        arr=np.array(np.asarray(img).astype('float'))
        rad1 = get_radius(img,arr)

        if rad1 < 50: print(x)
       
    except: pass
    count += 1
    
    if count % 10 == 0:
        print("Count =" + str(count))
        print("Elapsed time = " + str(time.time() - start) + " seconds")
        print("Estimated time = " + str((time.time()-start)//float(count)*44340//60) + " minutes")

  print(bad)


def demo_radius():
    FILENAME = "/Users/Carson/Desktop/final_project/image_org/" + str(15) + "_right.jpeg"
    img = Image.open(FILENAME).convert('RGB')
    start = time.time()
    arr=np.array(np.asarray(img).astype('float'))
    rad, start, end = get_radius(img, arr)
    print(rad, start, end)

demo_radius()






