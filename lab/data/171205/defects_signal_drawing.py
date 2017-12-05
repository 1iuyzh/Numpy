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

time = []
refer = []
signal = []
t_b = []
dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171205/200v10p150mm2cm14defects'
for f in os.listdir(root):
    with open(os.path.join(root, f)) as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    rows = np.array(rows[2:])[:,:3].astype('float64')
    time.append(0.5*rows[:,0])
    refer.append(1000*rows[:,1])
    signal.append(1000*rows[:,2])

for (t, r) in zip(time, refer):
    for (pt, pr) in zip(t, r):
        if (pr > 500):
            t_b.append(pt)
            break

name = ['no defects', '0.5mm crack', '0.2mm crack', '20mm Aluminum sheet', '40mm Aluminum sheet']
vg = ['1322.36', '1219.21', '1260.17', '1286.09', '1268.69']

# 改成循环
for i in range(5):
    plt.subplot(5, 1, i+1)
    plt.axis([t_b[i], t_b[i]+600, -250, 250])
    plt.plot(time[i], refer[i])
    plt.plot(time[i], signal[i], label = 'group velocity: ' + vg[i])
    plt.xlabel('time/us', fontproperties=dfont)
    plt.ylabel('Volt/mV', fontproperties=dfont)
    plt.title(name[i], fontproperties=dfont)
    plt.legend()
    #plt.title(name[i], fontproperties=dfont)
plt.show()