import matplotlib.pyplot as plt

q0, qf = [0,0,0], [2,3,4]
vmax, amax = 1, 10
ta = round(vmax / amax, 2)
t1f = round((qf[0] - q0[0]) / vmax + ta, 2)
t2f = round((qf[1] - q0[1]) / vmax + ta, 2)
t3f = round((qf[2] - q0[2]) / vmax + ta, 2)

if t2f > t1f and t2f > t3f: tf = t2f
elif t1f > t2f and t1f > t3f: tf = t1f
else: tf = t3f

vk, ak, a10, a11, a12, a20, a21, a30, a31, a32 = [], [], [], [], [], [], [], [], [], []
for i in range(3):
    vk.append((qf[i] - q0[i]) / (tf - ta))
    ak.append(vk[i]/ta)
    a10.append(q0[i])
    a11.append(0)
    a12.append(0.5 * ak[i])
    a20.append(q0[0] + 0.5 * ak[i] * ta ** 2 - vk[i] * ta)
    a21.append(vk[i])
    a30.append(qf[i] - 0.5 * ak[i] * tf ** 2)
    a31.append(ak[i] * tf)
    a32.append(-0.5 * ak[i])

q, v, acc, td = [[],[],[]], [[],[],[]], [[],[],[]], []

for tt in range(round(ta*100)):
    t = tt/100
    td.append(t)
    for j in range(3):
        q[j].append(a10[j] + a11[j] * t + a12[j] * t ** 2)
        v[j].append(a11[j] + 2 * a12[j] * t)
        acc[j].append(2*a12[j])
for tt in range(round(ta*100), round((tf - ta)*100)):
    t = tt/100
    td.append(t)
    for j in range(3):
        q[j].append(a20[j] + a21[j] * t)
        v[j].append(a21[j])
        acc[j].append(0)
for tt in range(round((tf - ta)*100), round(tf*100)):
    t = tt/100
    td.append(t)
    for j in range(3):
        q[j].append(a30[j] + a31[j] * t + a32[j] * t ** 2)
        v[j].append(a31[j] + 2 * a32[j] * t)
        acc[j].append(2 * a32[j])
colors = ['r', 'g', 'b']
coords = ['x', 'y', 'z']
"""

for j in range(3):
    plt.plot(td, v[j], color = colors[j], linestyle = 'solid',
         label = coords[j])
for j in range(3):
    plt.plot(td, acc[j], color = colors[j], linestyle = 'solid',
         label = coords[j])
"""
for j in range(3):
    plt.plot(td, q[j], color = colors[j], linestyle = 'solid',
         label = coords[j])

plt.legend(loc='upper right')
plt.show()
