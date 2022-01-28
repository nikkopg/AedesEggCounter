# Aedes Egg Counter

Performing Aedes mosquito eggs counter based on HSV segmentation. 
Segmentation in HSV color space is done by picking value ranges for each channel.
Since the eggs mostly are black, value ranges used in this implementation are:
```
Hue: 0 - 179
Saturation: 0-255
Value: 0-50
```
> to use this implementation for another object with different color, change to appropriate value range.

Sample output:

![Output-1 - Copy](https://user-images.githubusercontent.com/70200533/151500288-be3dfc44-eb4d-4cd0-afe5-337a5298e24a.jpeg)
