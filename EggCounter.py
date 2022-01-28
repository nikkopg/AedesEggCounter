import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.filedialog import askopenfilename
from ImgProcessing import *

IP = ImgProcessing()

# Importing image file
root = tk.Tk()
root.update()
filename = askopenfilename(filetypes=[("images","*.jpg *.jpeg")])
object_img = cv2.imread(filename)
root.destroy()
print('[INFO]: Image Loaded.')

H, W = object_img.shape[0], object_img.shape[1]
scale_size = 50
kernel = np.ones((3,3),np.uint8)
# HSV value range for mosquito eggs' color, which are mostly black
min_H, max_H = 0, 179
min_S, max_S = 0, 255
min_V, max_V = 0, 50

# Transforming to HSV colorspace
hsv_img = cv2.cvtColor(object_img, cv2.COLOR_BGR2HSV)
# Masking, resulting binary image
mask = cv2.inRange(hsv_img, (min_H, min_S, min_V),
                  (max_H, max_S, max_V))
# Opening morphology operation, removing small segmented objects and smoothing
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
print('[INFO]: Image Processed.')

img_to_show = cv2.cvtColor(object_img.copy(), cv2.COLOR_BGR2RGB)
gamma = 5
boxes = list()
props = list()
font_size = (H/W)

try:
    contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for i, c in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        
        # Filtering objects that are too small
        if float(h)/H  >= 0.007 or float(w)/W >= 0.007:
            cv2.rectangle(img_to_show, (x-gamma, y-gamma), (x+w+gamma, y+h+gamma), (0,255,0), 2)
            if x-gamma < 0 or y-gamma < 0:
                roi = object_img[0:y+h+gamma, 0:x+w+gamma]
            else:
                roi = object_img[y-gamma:y+h+gamma, x-gamma:x+w+gamma]
            
            # Saving objects coordinate in picture and Region of Interest (each objects image) 
            # to lists for further processing.
            boxes.append((x,y,w,h))
            props.append(roi)
            
            # Drawing boxes and texts
            cv2.putText(img_to_show, f'{i+1}', (int(x)-gamma, int(y)-gamma),
                    cv2.FONT_HERSHEY_SIMPLEX, font_size, (255, 0, 0), 3)     
    cv2.putText(img_to_show, f'Total objects detected: {i+1}', (50,100),
                    cv2.FONT_HERSHEY_SIMPLEX, font_size, (255, 255, 0), 3)
except Exception as e:
    print(e)

print(f'[INFO]: Total objects detected: {i+1}')
plt.figure(figsize=(10,15))
plt.imshow(img_to_show)
plt.show()
