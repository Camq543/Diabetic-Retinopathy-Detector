import radius_2 as radius
from normalize import normalize
import numpy as np
from PIL import Image
import time


def write_to_file(image, arr, outfile, color):
  upperLeft, bottomRight = radius.get_corners(radius.get_radius(image, arr), image.size)


  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if i < upperLeft[1] and i > bottomRight[1] and j < bottomRight[0] and j > upperLeft[0]:
        outfile.write(str(arr[i][j][color]))
        outfile.write(",")
  outfile.write("\n")

def main():
  norm_red = open("norm_and_red.txt", "w")
  just_red = open("just_red.txt", "w")
  norm_blue = open("norm_and_blue.txt", "w")
  just_blue = open("norm_and_blue.txt", "w")
  norm_green = open("norm_and_green.txt", "w")
  just_green = open("just_green.txt", "w")

  loadPath = "/Users/Carson/Desktop/training_set/original"

  start = time.time()
  count = 0
  for x in range(10, 1000):
    try:
        red_arr, norm_red_arr, blue_arr, norm_blue_arr, green_arr, norm_green_arr = [],[],[],[],[],[]
        FILENAME = loadPath + "/" + str(x) + "_right.jpeg"
        img = Image.open(FILENAME).convert('RGB')
        arr = np.array(np.asarray(img).astype('float'))
        upperLeft, bottomRight = radius.get_corners(radius.get_radius(img, arr), img.size)

        for i in range(int(upperLeft[1]), int(bottomRight[1] + 1)):
          for j in range(int(upperLeft[0]), int(bottomRight[0] + 1)):
              red_arr.append(str(int(arr[i][j][0])))
              '''green_arr.append(str(int(arr[i][j][1])))
              blue_arr.append(str(int(arr[i][j][2])))'''

        '''normalize(arr)
        for i in range(int(upperLeft[1]), int(bottomRight[1] + 1)):
          for j in range(int(upperLeft[0]), int(bottomRight[0] + 1)):
              norm_red_arr.append(str(int(arr[i][j][0])))
              norm_green_arr.append(str(int(arr[i][j][1])))
              norm_blue_arr.append(str(int(arr[i][j][2])))'''

        just_red.write(",".join(red_arr) + "\n")
        '''just_blue.write(",".join(blue_arr) + "\n")
        just_green.write(",".join(green_arr) + "\n")
        norm_red.write(",".join(norm_red_arr) + "\n")
        norm_blue.write(",".join(norm_blue_arr) + "\n")
        norm_green.write(",".join(norm_green_arr) + "\n")'''

        red_arr, norm_red_arr, blue_arr, norm_blue_arr, green_arr, norm_green_arr = [],[],[],[],[],[]
        FILENAME = loadPath = "/" + str(x) + "_left.jpeg"
        img = Image.open(FILENAME).convert('RGB')
        arr = np.array(np.asarray(img).astype('float'))
        upperLeft, bottomRight = radius.get_corners(radius.get_radius(img, arr), img.size)

        for i in range(int(upperLeft[1]), int(bottomRight[1] + 1)):
          for j in range(int(upperLeft[0]), int(bottomRight[0] + 1)):
              red_arr.append(str(int(arr[i][j][0])))
              '''green_arr.append(str(int(arr[i][j][1])))
              blue_arr.append(str(int(arr[i][j][2])))'''

        '''normalize(arr)
        for i in range(int(upperLeft[1]), int(bottomRight[1] + 1)):
          for j in range(int(upperLeft[0]), int(bottomRight[0] + 1)):
              norm_red_arr.append(str(int(arr[i][j][0])))
              norm_green_arr.append(str(int(arr[i][j][1])))
              norm_blue_arr.append(str(int(arr[i][j][2])))'''

        just_red.write(",".join(red_arr) + "\n")
        '''just_blue.write(",".join(blue_arr) + "\n")
        just_green.write(",".join(green_arr) + "\n")
        norm_red.write(",".join(norm_red_arr) + "\n")
        norm_blue.write(",".join(norm_blue_arr) + "\n")
        norm_green.write(",".join(norm_green_arr) + "\n")'''

        count += 1
        
    except IOError: pass#print("Skipping image " + x)
    
    if count % 1 == 0:
      print("Count =" + str(count))
      print("Elapsed time = " + str(time.time() - start) + " seconds")
      print("Estimated time = " + str((time.time()-start)/float(count)*100.0/60.0) + " minutes")

    if count == 100: break

  norm_red.close()
  just_red.close()
  norm_blue.close()
  just_blue.close()
  norm_green.close()
  just_green.close() 



main()