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
signal = []
refer = []
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

vg = []
t_start = 0
t_end = 0
for (t, r, s) in zip(time, refer, signal):
    for (pt, pr, ps) in zip(t, r, s):
        if (pr > 0) and (t_start == 0):
            t_start = pt
        if (ps > 20) and (t_end == 0):
            t_end = pt
    if (t_end > t_start):
        # 150mm 加上两个30mm 减去(20+25)mm乘以tan
        distance = (150e-3+30e-3*2)-(2*45e-3*math.tan(14*np.pi/180)) # 单位m 修改45
        dt = t_end*1e-6-t_start*1e-6-2*(45e-3/math.cos(14*np.pi/180)-20e-3)/340 # 单位s 修改20
        vg.append(distance/dt)
    else:
        vg.append(0)
    t_start = 0
    t_end = 0

print(vg)