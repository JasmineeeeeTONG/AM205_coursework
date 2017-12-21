#!/opt/local/bin/python2.7
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# Load in the test image 
a=io.imread("pierce.png",as_grey=True)

# Output as a matrix of zeros and ones
fi=open("pierce.txt","w")
(y,x)=a.shape
for j in range(y):
    fi.write(" ".join([str(1^int(a[j,i])) for i in range(x)])+"\n")
fi.close()
