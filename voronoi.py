import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
import cv2  
from PIL import Image
import random

# Load the image
image = Image.open('drive/MyDrive/Untitled.jpeg')
image.resize((300,300)) 
image_array = np.array(image)

num_points = 500  
points = np.array([[random.randint(0, image_array.shape[1]), random.randint(0, image_array.shape[0])] for _ in range(num_points)])

vor = Voronoi(points)

output_image = np.zeros_like(image_array)
polygons = []
colors = []
for region_index in range(len(vor.regions)):
    region = vor.regions[region_index]
    if not -1 in region and len(region) > 0:
        polygon = [vor.vertices[i] for i in region]
        polygon = np.array(polygon, dtype=np.int32)

        mask = np.zeros((image_array.shape[0], image_array.shape[1]), dtype=np.uint8)
        cv2.fillPoly(mask, [polygon], 255)

        region_pixels = image_array[mask == 255]
        if len(region_pixels) > 0:
            color = np.mean(region_pixels, axis=0)
            color = tuple(map(int, color))  
            cv2.fillPoly(output_image, [polygon], color)
            polygons.append(polygon)
            colors.append(color)

fle = open("drive/MyDrive/info.txt",'w')
def genvert(poly):
  verts = ''
  verts += '['
  for i in range(len(poly)):
    verts  += '['
    verts += str(min(abs(poly[i][0]),300))
    verts += ','
    verts += str(min(abs(300-poly[i][1]),300))
    verts += ']'
    if(i!= len(poly)-1):
      verts += ','
    verts += '\n'
  verts += ']'
  return verts

for i in range(len(polygons)):
  fle.write(genvert(polygons[i])+",\n")

fle.write("\n\n\nCOLORS\n\n\n")
for i in range(len(polygons)):
  fle.write(str(colors[i])+",\n")

fle.close()

plt.imshow(output_image)
plt.axis('off')
plt.show()
