import numpy as np
import csv
import matplotlib.pyplot as plot
import os

""" 
read the directory

fpath= r"D:\UG project\text file\csv file"

for file in os.listdir(fpath):
	print(os.path.join(fpath,file))
	break
"""	


s = np.loadtxt('metalic_20.csv',dtype=float,delimiter=',')

samplingFrequency   = 1

fig = plot.figure(frameon=False)

ax = plot.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

powerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(s, Fs=samplingFrequency)

fig.savefig('metalic_20.png',bbox_inches='tight', transparent='true')

plot.show()   

