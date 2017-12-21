#!/usr/bin/python
import numpy as np
import sys

# This code provides an example of doing arithmetic on the binary set {0,1}. It
# takes advantage of the fact that the binary "+" and "*" operations are
# equivalent to the bitwise logic operators, which are built into Python. If
# you are unfamilar with bitwise operators, see the following page for more
# information:
#
# http://en.wikipedia.org/wiki/Bitwise_operation
#
# Binary addition is equivalent to the "exclusive or" or "XOR" operation, which
# is denoted by the "^" operator in Python. Hence, whenever we see a "+" or a
# "-", we replace it with a "^".
#
# Binary multiplication is equivalent to the "AND" operation, which is denoted
# by the "&" operator in Python. Hence, whenever we see a "*" we replace it
# with a "&".
#
# The following example code implements matrix multiplication on the binary
# set, using the above substitutions. In addition, since the bitwise operators
# only work on integers, each matrix is initialized to be integers using the
# option "dtype=np.int8".
#
# This code does not have any examples of division. However, implementing "x/y"
# can be done in the following way:
#   - if y==1 then x/y evaluates to x,
#   - if y==0 then an error is given.

# Function to calculate binary matrix multiplication
def bin_mul(c,d):
    
    # Check that the dimensions of the matrices are compatible
    (m,n)=c.shape
    (nn,p)=d.shape
    if n!=nn:
        print "Matrix size mismatch"
        sys.exit()

    # Initalize blank matrix of integer zeros
    e=np.zeros((m,p),dtype=np.int8)

    # Calculate each term, using "&" instead of "*" and "^" instead of "+"
    for i in range(m):
        for j in range(p):
            for k in range(n):
                e[i,j]=e[i,j]^(c[i,k]&d[k,j])
    return e

# Define the example L and U matrices
l=np.array([[1,0,0,0],[0,1,0,0],[1,1,1,0],[1,0,1,1]],dtype=np.int8)
u=np.array([[1,0,1,0],[0,1,1,1],[0,0,1,0],[0,0,0,1]],dtype=np.int8)

# Carry out binary matrix multiplication and print the result
a=bin_mul(l,u)
print a
