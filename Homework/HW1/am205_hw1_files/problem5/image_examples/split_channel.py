import numpy as np
from skimage import io

# Read Rubik's cube image 
a=io.imread("rubik.png")
(y,x,z)=a.shape

# Output each channel
for k in range(3):
    b=np.zeros((y,x,z))
    b[:,:,k]=a[:,:,k]/255.0
    io.imsave("channel%d.png" % (k),b)
