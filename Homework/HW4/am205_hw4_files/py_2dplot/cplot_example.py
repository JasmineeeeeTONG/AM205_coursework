#!/usr/bin/python
import numpy as np
import custom_plot as cplt
from math import sin

# Load in the wall matrix
q=np.loadtxt("pierce.txt",dtype=np.int8)

# Create an empty array and fill it with some made-up data
w=np.zeros((100,200))
for i in range(100):
    x=0.1*i
    for j in range(200):
        y=0.1*j
        w[i,j]=sin(x+0.5*y)

# Call the first custom plotting routine
cplt.plot1("test1.png",w,q,-1.1,1.1,3)

# Call the second custom plotting routine
cplt.plot2("test2.png",w,q,-1.1,1.1,3)
