import os
import math
import csv

import numpy as np
from scipy import signal
from scipy.interpolate import spline
from scipy import optimize
import matplotlib.pyplot as plt
import matplotlib

t = []
s = []
d = []
dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171128/plate2/100Vpp10pXmm20mm40mm14'
for i in os.listdir(root):
    d.append(int(i.split('.')[0]))
    with open(os.path.join(root, i)) as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    rows = np.array(rows[2:])[:,:3].astype('float64')
    t.append(0.5*rows[:,0])
    s.append(1000*rows[:,2])

v = []
for (i, k) in zip(t, s):
    v.append(max(k))

z = np.polyfit(d, v, 3)
p = np.poly1d(z)

#dn = np.linspace(min(d), max(d), 20)
#vn = spline(d, v, dn)
#plt.plot(dn, vn)

plt.plot(d, v, 'o')
plt.plot(d, p(d))
plt.title('信号强度随探头间距变化', fontproperties=dfont)
plt.xlabel('距离/mm', fontproperties=dfont)
plt.ylabel('信号最大值/mV', fontproperties=dfont)
plt.show()

#b, a = signal.butter(3, 0.2, 'low')
#sf = signal.filtfilt(b, a, data[:,2])