# Aedes Egg Localization

## Brief Description
Performing Aedes mosquito eggs localization based on HSV segmentation. 
Segmentation in HSV color space is done by picking value ranges for each channel for desired color to be segmented.
Since the eggs mostly are black, value ranges used in this implementation are:
```
Hue: 0 - 179
Saturation: 0-255
Value: 0-50
```
> to use this implementation for another object with different color, change to appropriate value range.

## Limitations and future improvement:
As this implementation only locating object based on color, any object in image with the same color will be located and counted.
The code also returns Regions of Interest (ROIs) and coordinate of each object detected in image. By using these ROIs and coordinate, further improvement could be done like classification to do object detection.

## Sample output:

![Output-1 - Copy](https://user-images.githubusercontent.com/70200533/151500288-be3dfc44-eb4d-4cd0-afe5-337a5298e24a.jpeg)
