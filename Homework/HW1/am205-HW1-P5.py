import numpy as np
from skimage import io
import matplotlib.pyplot as plt

def load_and_split(img_dir): 
    # Read regular image 
    a = io.imread(img_dir)
    (y,x,z) = a.shape
    print(x,y,z)
    
    # Output each channel
    for k in range(3):
        b = np.zeros((y,x,z))
        b[:,:,k]=a[:,:,k]/255.0
        output_dir = img_dir.replace('.png', '')+'_channel'+str(k)+'.png'
        io.imsave(output_dir, b)

load_and_split('objects/regular.png')
load_and_split('objects/low1.png')
load_and_split('objects/low2.png')
load_and_split('objects/low3.png')

# Load in channel 0, 1, and 2 of the regular image
A0 = io.imread('objects/regular_channel0.png', as_grey=True) 
A1 = io.imread('objects/regular_channel1.png', as_grey=True) 
A2 = io.imread('objects/regular_channel2.png', as_grey=True) 

B0 = io.imread('objects/low1_channel0.png', as_grey=True)
B1 = io.imread('objects/low1_channel1.png', as_grey=True)
B2 = io.imread('objects/low1_channel2.png', as_grey=True)

C0 = io.imread('objects/low2_channel0.png', as_grey=True)
C1 = io.imread('objects/low2_channel1.png', as_grey=True)
C2 = io.imread('objects/low2_channel2.png', as_grey=True)

D0 = io.imread('objects/low3_channel0.png', as_grey=True)
D1 = io.imread('objects/low3_channel1.png', as_grey=True)
D2 = io.imread('objects/low3_channel2.png', as_grey=True)

# Check size
(N, M) = A0.shape
print(M, 'by', N, 'pixels')

A0 = A0.reshape(M*N, )
A1 = A1.reshape(M*N, )
A2 = A2.reshape(M*N, )

B0 = B0.reshape((M*N, 1))
B1 = B1.reshape((M*N, 1))
B2 = B2.reshape((M*N, 1))

C0 = C0.reshape((M*N, 1))
C1 = C1.reshape((M*N, 1))
C2 = C2.reshape((M*N, 1))

D0 = D0.reshape((M*N, 1))
D1 = D1.reshape((M*N, 1))
D2 = D2.reshape((M*N, 1))

ones = np.ones((M*N, 1))
X = np.concatenate((B0, B1, B2, C0, C1, C2, D0, D1, D2, ones), axis = 1)
h0 = np.linalg.lstsq(X, A0)[0]
h1 = np.linalg.lstsq(X, A1)[0]
h2 = np.linalg.lstsq(X, A2)[0]

Reconstruct0 = np.dot(X, h0).reshape((N, M, 1))
Reconstruct1 = np.dot(X, h1).reshape((N, M, 1))
Reconstruct2 = np.dot(X, h2).reshape((N, M, 1))
Reconstruct = np.concatenate((Reconstruct0, Reconstruct1, Reconstruct2), axis = 2)

from scipy.misc import imsave
imsave('objects/reconstruct.png', Reconstruct)