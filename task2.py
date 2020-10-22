from sympy import *
import matplotlib.pyplot as plt

Ainv = Matrix([[    1,     0,     0,      0,     0,    0],
               [    0,     1,     0,      0,     0,    0],
               [    0,     0,   1/2,      0,     0,    0],
               [ -5/4,  -3/2,  -3/4,    5/4,    -1,  1/4],
               [15/16,     1,   3/8, -15/16,   7/8, -1/4],
               [-3/16, -3/16, -1/16,   3/16, -3/16, 1/16]])
am = Matrix([Ainv*Matrix([0, 0, 0, 2, 0, 0]),
             Ainv*Matrix([0, 0, 0, 3, 0, 0]),
             Ainv*Matrix([0, 0, 0, 4, 0, 0])]).reshape(3,6)
q, v, a, td = [[],[],[]], [[],[],[]], [[],[],[]], []
for i in range(200):
    t = i/100
    td.append(i/100)
    for i in range(3):
        q[i].append(am[i,0]+am[i,1]*t+am[i,2]*t**2+am[i,3]*t**3+am[i,4]*t**4+am[i,5]*t**5)
        v[i].append(am[i,1] + 2 * am[i,2] * t + 3 * am[i,3] * t ** 2 + 4 * am[i,4] * t ** 3 + 5 * am[i,5] * t ** 4)
        a[i].append(2*am[i,2]+6*am[i,3]*t+12*am[i,4]*t**2+20*am[i,5]*t**3)
colors = ['r', 'g', 'b']
coords = ['x', 'y', 'z']
"""
for j in range(3):
    plt.plot(td, q[j], color = colors[j], linestyle = 'solid',
         label = coords[j])
for j in range(3):
    plt.plot(td, v[j], color = colors[j], linestyle = 'solid',
         label = coords[j])
for j in range(3):
    plt.plot(td, a[j], color = colors[j], linestyle = 'solid',
         label = coords[j])
"""
plt.legend(loc='upper right')
plt.show()