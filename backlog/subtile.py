import os, shutil
import cv2
from PIL import Image

def tile4(img, name, destination):
  tile1 = img[0:32, 0:32]
  tile2 = img[0:32, 32:64]
  tile3 = img[32:64, 0:32]
  tile4 = img[32:64, 32:64]
  name = name.replace('.jpeg', '')
  cv2.imwrite(destination + name + '_1.jpeg' , tile1)
  cv2.imwrite(destination + name + '_2.jpeg' , tile2)
  cv2.imwrite(destination + name + '_3.jpeg' , tile3)
  cv2.imwrite(destination + name + '_4.jpeg' , tile4)

n = os.listdir('python/AFB/include/image/tile/a_64/negative')
for i in range(len(n)):
  #print(i + '/' + len(n))
  i = n[i]
  img = cv2.imread('python/AFB/include/image/tile/a_64/negative/' + i)
  tile4(img, i, 'Desktop/negative/')

p = os.listdir('python/AFB/include/image/a_64/tile/positive')
for i in range(len(p)):
  #print(i + '/' + len(p))
  i = p[i]
  img = cv2.imread('python/AFB/include/image/tile/a_64/positive/' + i)
  tile4(img, i, 'Desktop/positive/')
