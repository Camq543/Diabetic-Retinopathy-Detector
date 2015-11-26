import numpy as np
from PIL import Image
import time
import math
import sys

def get_corners(radius, size):
  center = [size[0]//2, size[1]//2]
  #added -.1*radius to help with corner stuff
  displacement = int(radius * math.cos(math.pi/4) - .05*radius)
  if center[1] - displacement < 0 or center[1] + displacement > size[1]:
    displacement = size[1] - center[1]
  upperLeft = [center[0] - displacement, center[1] - displacement]
  bottomRight = [center[0] + displacement, center[1] + displacement]
  return upperLeft, bottomRight

'''def get_corners(radius, size):
  center = [size[0]//2, size[1]//2]
  displacement = radius * math.cos(math.pi/4)
  upperLeft = [center[0] - displacement, center[1] + displacement]
  bottomRight = [center[0] + displacement, center[1] - displacement]
  return upperLeft, bottomRight'''

def get_radius(img, arr):

  midHeight = img.size[1]//2

  start = 0
  end = img.size[0]
  #hold onto previous 3 values to correct for noise
  for pixI in range(len(arr[midHeight])):
    if not is_Black(arr[midHeight][pixI]):
      start = pixI
      break

  for pixI in range(len(arr[midHeight])-1, -1, -1):
    if not is_Black(arr[midHeight][pixI]):
      end = pixI
      break

  return (end - start)//2

def is_Black(pixel):
    colors = []
    for color in pixel:
        colors.append(color)
    if max(colors) < 5: return True
    return False

def check_all_radii():
  start = time.time()
  count = 0
  for x in range(10, 44350):
    try:
        FILENAME = "/Users/Carson/Desktop/training_set/original/" + str(x) + "_right.jpeg"
        img = Image.open(FILENAME).convert('RGB')
        arr=np.array(np.asarray(img).astype('float'))
        rad, start, end = get_radius(img, arr)
        print(rad) 

        FILENAME = "/Users/Carson/Desktop/training_set/original/" + str(x) + "_left.jpeg"
        img = Image.open(FILENAME).convert('RGB')
        arr=np.array(np.asarray(img).astype('float'))
        rad1, start, end = get_radius(img,arr)
        print(rad1)
       
    except: pass
    count += 1
    
  '''if count % 10 == 0:
      print("Count =" + str(count))
      print("Elapsed time = " + str(time.time() - start) + " seconds")
      print("Estimated time = " + str((time.time()-start)//float(count)*44340//60) + " minutes")'''

def check_all_sides():
  start = time.time()
  count = 0

  for x in range(10, 45000):
    try:
       FILENAME = "/Users/Carson/Desktop/final_project/image_org/" + str(x) + "_right.jpeg"
       img = Image.open(FILENAME).convert('RGB')
       arr=np.array(np.asarray(img).astype('float'))

       rad = get_radius(img, arr)
       upleft, botright = get_corners(rad, img.size)
       width = int(botright[0] - upleft[0])
       height = int(upleft[1] - botright[1])
       if width != height: print("Problem")

       FILENAME = "/Users/Carson/Desktop/final_project/image_org/" + str(x) + "_left.jpeg"
       img = Image.open(FILENAME).convert('RGB')
       arr=np.array(np.asarray(img).astype('float'))

       rad = get_radius(img, arr)
       upleft, botright = get_corners(rad, img.size)
       width = botright[0] - upleft[0]
       height = upleft[1] - botright[1]
       if width != height or width == 0: print("Problem")
     
    except IOError: pass

def check_all_corners():
  start = time.time()
  count = 0

  for x in range(10, 45000):
    try:

       FILENAME = "/Users/Carson/Desktop/training_set/original/" + str(x) + "_right.jpeg"
       img = Image.open(FILENAME).convert('RGB')
       arr=np.array(np.asarray(img).astype('float'))

       rad = get_radius(img, arr)
       upleft, botright = get_corners(rad, img.size)
       if upleft[0] < 0 or upleft[0] > img.size[0] or botright[0] < 0 or botright[0] > img.size[0] \
       or upleft[1] < 0 or upleft[1] > img.size[1] or botright[1] < 0 or botright[1] > img.size[1]:
        print("Project")
       

       FILENAME = "/Users/Carson/Desktop/training_set/original/" + str(x) + "_left.jpeg"
       img = Image.open(FILENAME).convert('RGB')
       arr=np.array(np.asarray(img).astype('float'))

       rad = get_radius(img, arr)
       upleft, botright = get_corners(rad, img.size)
       if upleft[0] < 0 or upleft[0] > img.size[0] or botright[0] < 0 or botright[0] > img.size[0] \
       or upleft[1] < 0 or upleft[1] > img.size[1] or botright[1] < 0 or botright[1] > img.size[1]:
        print("Problem")
       count += 1
     
    except IOError: pass

    if count % 10 == 0:
      print("Count =" + str(count))
      print("Elapsed time = " + str(time.time() - start) + " seconds")
      print("Estimated time = " + str((time.time()-start)/float(count)*44340.0/60.0) + " minutes")

def demo_radius():
    FILENAME = "/Users/Carson/Desktop/final_project/image_org/" + str(15) + "_right.jpeg"
    img = Image.open(FILENAME).convert('RGB')
    start = time.time()
    arr=np.array(np.asarray(img).astype('float'))
    rad, start, end = get_radius(img, arr)
    print(rad, start, end)





