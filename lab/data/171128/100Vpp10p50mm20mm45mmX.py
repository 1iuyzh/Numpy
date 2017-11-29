import os
import math
import csv

import numpy as np
from scipy import signal
from scipy.interpolate import spline
import matplotlib.pyplot as plt
import matplotlib

t = []
s = []
r = []
dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171128/plate2/100Vpp10p50mm20mm45mmX'
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

plt.plot(r, v)
plt.title('信号强度随转角变化', fontproperties=dfont)
plt.xlabel('转角/°', fontproperties=dfont)
plt.ylabel('信号最大值/mV', fontproperties=dfont)
plt.show()

#b, a = signal.butter(3, 0.2, 'low')
#sf = signal.filtfilt(b, a, data[:,2])