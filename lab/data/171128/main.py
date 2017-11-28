import numpy as np
import matplotlib.pyplot as plt
import csv

with open('lab/data/20171128/plate2/50mm20mm0mmX/07.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    data = np.array(rows[2:])[:,:3].astype(float)
    #print(data.shape)
    plt.plot(data[:,0], data[:,1])
    plt.plot(data[:,0], data[:,2])
    plt.xlabel('time/us')
    plt.ylabel('Volt')
    plt.legend(['ch1', 'ch2'])
    plt.show()

with open('lab/data/20171128/plate2/50mm20mm0mmX/14.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    data = np.array(rows[2:])[:,:3].astype(float)
    #print(data.shape)
    plt.plot(data[:,0], data[:,1])
    plt.plot(data[:,0], data[:,2])
    plt.xlabel('time/us')
    plt.ylabel('Volt')
    plt.legend(['ch1', 'ch2'])
    plt.show()