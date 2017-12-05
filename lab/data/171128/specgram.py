import os
import math
import csv

import numpy as np
import scipy
from scipy import signal
from scipy.interpolate import spline
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import matplotlib

dfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/YaHei Consolas Hybrid.ttf')

root = 'lab/data/171128/plate2/100Vpp10p50mm20mm0mmX'
with open(os.path.join(root, '15.csv')) as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
rows = np.array(rows[2:])[:,:3].astype('float64')
tim = 0.5 * rows[:, 0]
ref = 1000 * rows[:, 1]
sig = 1000 * rows[:, 2]

plt.specgram(sig, NFFT=64, Fs = 2e6, noverlap=32, cmap = matplotlib.cm.gray_r, pad_to=64)
# 800kHz是什么?
# 增大采样频率
plt.show()