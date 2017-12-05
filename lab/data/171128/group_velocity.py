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

def average(v):
    _sum = 0
    _len = 0
    for i in v:
        if i != 0:
            _sum += i
            _len += 1
    return _sum/_len

def deviation(v):
    _de = 0
    _len = 0
    ave = average(v)
    for i in v:
        if i != 0:
            _de += (i-ave)**2
            _len += 1
    return math.sqrt(_de/_len)

########################
## 2cm 40mm
########################

time = []
ref = []
sig = []
angle = []
dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171128/plate2/100Vpp10p50mm20mm40mmX'  # 修改路径
for i in ['13.csv', '14.csv', '15.csv']:
    angle.append(int(i.split('.')[0]))
    with open(os.path.join(root, i)) as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    rows = np.array(rows[2:])[:,:3].astype('float64')
    time.append(0.5*rows[:,0])
    ref.append(1000*rows[:,1])
    sig.append(1000*rows[:,2])

vg = []
t_start = 0
t_end = 0
for (t, r, s, a) in zip(time, ref, sig, angle):
    for (pt, pr, ps) in zip(t, r, s):
        if (pr > 50) and (t_start == 0):
            t_start = pt
        if (ps > 30) and (t_end == 0):
            t_end = pt
    if (t_end > t_start):
        distance = (50e-3+30e-3*2)-(2*45e-3*math.tan(a*np.pi/180)) # 单位m 修改45
        dt = t_end*1e-6-t_start*1e-6-2*(45e-3/math.cos(a*np.pi/180)-20e-3)/340 # 单位s 修改20
        vg.append(distance/dt)
    else:
        vg.append(0)
    t_start = 0
    t_end = 0

#print(vg)
print(average(vg), deviation(vg))

########################
## 3cm 40mm
########################

time = []
ref = []
sig = []
angle = []
dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171128/plate2/100Vpp10p50mm30mm40mmX'
for i in ['13.csv', '14.csv', '15.csv']:
    angle.append(int(i.split('.')[0]))
    with open(os.path.join(root, i)) as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    rows = np.array(rows[2:])[:,:3].astype('float64')
    time.append(0.5*rows[:,0])
    ref.append(1000*rows[:,1])
    sig.append(1000*rows[:,2])

vg = []
t_start = 0
t_end = 0
for (t, r, s, a) in zip(time, ref, sig, angle):
    for (pt, pr, ps) in zip(t, r, s):
        if (pr > 50) and (t_start == 0):
            t_start = pt
        if (ps > 50) and (t_end == 0):
            t_end = pt
    if (t_end > t_start):
        distance = (50e-3+30e-3*2)-(2*55e-3*math.tan(a*np.pi/180))
        dt = t_end*1e-6-t_start*1e-6-2*(55e-3/math.cos(a*np.pi/180)-20e-3)/340
        vg.append(distance/dt)
    else:
        vg.append(0)
    t_start = 0
    t_end = 0

#print(vg)
print(average(vg), deviation(vg))

########################
## 2cm 0mm
########################

time = []
ref = []
sig = []
angle = []
dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171128/plate2/100Vpp10p50mm20mm0mmX'
for i in ['13.csv', '14.csv', '15.csv']:
    angle.append(int(i.split('.')[0]))
    with open(os.path.join(root, i)) as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    rows = np.array(rows[2:])[:,:3].astype('float64')
    time.append(0.5*rows[:,0])
    ref.append(1000*rows[:,1])
    sig.append(1000*rows[:,2])

vg = []
t_start = 0
t_end = 0
for (t, r, s, a) in zip(time, ref, sig, angle):
    for (pt, pr, ps) in zip(t, r, s):
        if (pr > 50) and (t_start == 0):
            t_start = pt
        if (ps > 50) and (t_end == 0):
            t_end = pt
    if (t_end > t_start):
        distance = (50e-3+30e-3*2)-(2*45e-3*math.tan(a*np.pi/180))
        dt = t_end*1e-6-t_start*1e-6-2*(45e-3/math.cos(a*np.pi/180)-20e-3)/340
        vg.append(distance/dt)
    else:
        vg.append(0)
    t_start = 0
    t_end = 0

print(average(vg), deviation(vg))