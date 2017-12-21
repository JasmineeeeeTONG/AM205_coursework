import numpy as np
from math import *
import matplotlib.pyplot as plt
import sys

# Returns a scaled value of a function in the range 0 to 1, truncating it if
# necessary
def fscale(v,vmin,vsca):
    vs=(v-vmin)*vsca
    if vs<0: vs=0
    if vs>1: vs=1
    return vs

# Returns a red->white->blue color scheme
def palette1(v):
    v*=2
    if(v>1):
        v=2-v
        return (v,v,min(1,0.5+3*v))
    else:
        return (min(1,0.5+3*v),v,v)

# Outputs a 2D image from a field using the palette1 color scheme
# fn: the filename to save to
# p: the 2D field to plot
# wa: the matrix describing walls to overlay
# (vmin,vmax): the field range
# ups: the upsampling factor to use (so each field point is convert into an ups
#      by ups square)
def plot1(fn,p,wa,vmin,vmax,ups):

    # Check matrix dimensions are the same
    (m,n)=p.shape
    if (m,n)!=wa.shape:
        print("Matrix dimension mismatch")

    # Set up output array and scaling constant
    o=np.zeros((m*ups,n*ups,3))
    vsca=1.0/(vmax-vmin)

    # Assemble the output array
    for i in range(m):
        iu=i*ups
        for j in range(n):
            ju=j*ups
            if wa[i,j]==1:
                o[iu:iu+ups,ju:ju+ups,0]=0
                o[iu:iu+ups,ju:ju+ups,1]=0
                o[iu:iu+ups,ju:ju+ups,2]=0
            else:
                (re,gr,bl)=palette1(fscale(p[i,j],vmin,vsca))
                o[iu:iu+ups,ju:ju+ups,0]=re
                o[iu:iu+ups,ju:ju+ups,1]=gr
                o[iu:iu+ups,ju:ju+ups,2]=bl
    
    # Save the image
    plt.imsave(fn,o)

# Returns a black->red->yellow color scheme (matching Gnuplot's PM3D scheme)
def palette2(v):
    if v>0.5:
        vs=0
    else:
        vs=sin(2*pi*v)
    return (sqrt(v),v*v*v,vs)

# Outputs a 2D image from a field using the palette2 color scheme
# fn: the filename to save to
# p: the 2D field to plot
# wa: the matrix describing walls to overlay
# (vmin,vmax): the field range
# ups: the upsampling factor to use (so each field point is convert into an ups
#      by ups square)
def plot2(fn,p,wa,vmin,vmax,ups):
    
    # Check matrix dimensions are the same
    (m,n)=p.shape
    if (m,n)!=wa.shape:
        print("Matrix dimension mismatch")

    # Set up output array and scaling constant
    o=np.zeros((m*ups,n*ups,3))
    vsca=1.0/(vmax-vmin)

    # Assemble the output array
    for i in range(m):
        iu=i*ups
        for j in range(n):
            ju=j*ups
            if wa[i,j]==1:
                o[iu:iu+ups,ju:ju+ups,0]=1
                o[iu:iu+ups,ju:ju+ups,1]=1
                o[iu:iu+ups,ju:ju+ups,2]=1
            else:
                (re,gr,bl)=palette2(fscale(p[i,j],vmin,vsca))
                o[iu:iu+ups,ju:ju+ups,0]=re
                o[iu:iu+ups,ju:ju+ups,1]=gr
                o[iu:iu+ups,ju:ju+ups,2]=bl

    # Save the image
    plt.imsave(fn,o)

