#!/opt/local/bin/python2.7
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# Load in the test image 
a=io.imread("../orig_image/pierce.png",as_grey=True)

# Check size
(y,x)=a.shape
print x,"by",y,"pixels"

# Plot the image
plt.imshow(a,cmap=plt.cm.gray)
plt.show()
