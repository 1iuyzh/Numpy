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

dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171128/plate2/100Vpp10p50mm20mm40mmX'

with open(os.path.join(root, '14.csv')) as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
rows = np.array(rows[2:])[:,:3].astype('float64')
t = 0.5 * rows[:, 0]
r = 1000 * rows[:, 1]
s = 1000 * rows[:, 2]

plt.plot(t, s)
plt.title('信号', fontproperties=dfont)
plt.xlabel('time/us', fontproperties=dfont)
plt.ylabel('Volt/mV', fontproperties=dfont)
plt.show()