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
r = []
s = []
dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171205/csv/defects'
for f in os.listdir(root):
    with open(os.path.join(root, f)) as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    rows = np.array(rows[2:])[:,:3].astype('float64')
    t.append(0.5*rows[:,0])
    r.append(1000*rows[:,1])
    s.append(1000*rows[:,2])

plt.subplot(5, 1, 1)
plt.plot(t[0], s[0])
plt.plot(t[0], r[0])
plt.ylim(-250, 250)
plt.xlabel('time/us', fontproperties=dfont)
plt.ylabel('Volt/mV', fontproperties=dfont)
plt.title('无缺陷', fontproperties=dfont)
plt.subplot(5, 1, 2)
plt.plot(t[1], s[1])
plt.plot(t[1], r[1])
plt.ylim(-250, 250)
plt.xlabel('time/us', fontproperties=dfont)
plt.ylabel('Volt/mV', fontproperties=dfont)
plt.title('0.5mm深裂纹', fontproperties=dfont)
plt.subplot(5, 1, 3)
plt.plot(t[2], s[2])
plt.plot(t[1], r[2])
plt.ylim(-250, 250)
plt.xlabel('time/us', fontproperties=dfont)
plt.ylabel('Volt/mV', fontproperties=dfont)
plt.title('0.2mm深裂纹', fontproperties=dfont)
plt.subplot(5, 1, 4)
plt.plot(t[3], s[3])
plt.plot(t[1], r[3])
plt.ylim(-250, 250)
plt.xlabel('time/us', fontproperties=dfont)
plt.ylabel('Volt/mV', fontproperties=dfont)
plt.title('45层间20mm边长铝片', fontproperties=dfont)
plt.subplot(5, 1, 5)
plt.plot(t[4], s[4])
plt.plot(t[4], r[4])
plt.ylim(-250, 250)
plt.xlabel('time/us', fontproperties=dfont)
plt.ylabel('Volt/mV', fontproperties=dfont)
plt.title('89层间40mm边长铝片', fontproperties=dfont)
plt.show()