import os
import math
import csv

import numpy as np
from scipy import signal
from scipy.interpolate import spline
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import matplotlib

t = []
s = []
r = []
dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171128/plate2/100Vpp10p50mm20mm40mmX'
for i in os.listdir(root):
    r.append(int(i.split('.')[0]))
    with open(os.path.join(root, i)) as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    rows = np.array(rows[2:])[:,:3].astype('float64')
    t.append(0.5*rows[:,0])
    s.append(1000*rows[:,2])

v = []
for (i, k) in zip(t, s):
    v.append(max(k))

def func(p, x):
    a, b, c = p
    return a*np.exp(-((x-b)/c)**2)

def error(p, x, y):
    return (func(p, x)-y)**2

p0 = [210, 14, 4]
para = leastsq(error, p0, args=(r, v))
vs = func(para[0], r)

rn = np.linspace(min(r), max(r), 50)
vn = spline(r, vs, rn)

plt.plot(r, v, 'o')
plt.plot(rn, vn)
plt.title('信号强度随转角变化', fontproperties=dfont)
plt.xlabel('转角/°', fontproperties=dfont)
plt.ylabel('信号最大值/mV', fontproperties=dfont)
plt.show()

#b, a = signal.butter(3, 0.2, 'low')
#sf = signal.filtfilt(b, a, data[:,2])