from math import *
import numpy as np
import matplotlib.pyplot as plt

def cubic_poly(x, b):
	n = len(b) - 1
	y = b[0]
	for i in range(1, n):
		y *= x
		y += b[i]
	return y

# Initialize x and function values y
x = np.array([0., 1., 2., 3.])
y = np.array([0., 0., 1., 2.])

# get Vandermonde of x
V = np.vander(x)
# print(V)

# Solve b for Vb=y
b=np.linalg.solve(V,y)
#print(b)

print("The cubic polynomial interpolant using monomial basis is:")
print("y = %fx^3 + %fx^2 + %fx + %f" % (b[0], b[1], b[2], b[3]))

# Plot interpolant
xx=np.linspace(-1,4,300)
yy_v=np.array([cubic_poly(q,b) for q in xx])
plt.figure()
plt.plot(xx,yy_v)
plt.xlabel('x')
plt.ylabel('y')
plt.show()