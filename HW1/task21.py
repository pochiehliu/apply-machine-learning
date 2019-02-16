"""
Pick a graph from http://www.tylervigen.com/spurious-correlations and recreate 
it using matplotlib (you can also use numpy and pandas). The code can read the 
data from the web or from a text file or csv file (to be included in the 
repository). Ensure the axes are labeled properly.

reference used for fixing twinx twiny axis alignment 
https://stackoverflow.com/questions/20243683/matplotlib-align-twinx-tick-marks 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# read data
df = pd.read_csv('task21.csv',
                 sep = ',',
                 header = 0,
                 quotechar = '"')

# generate smooth line using spline method
x = np.linspace(df['year'].min(), df['year'].max(), 101)
spline1 = make_interp_spline(df['year'], df.iloc[:,1], 3)
line1 = spline1(x)
spline2 = make_interp_spline(df['year'], df.iloc[:,2], 3)
line2 = spline2(x)

# generate plot and ticks
fig = plt.figure(figsize = (10,5))
x_tick = [x for x in df['year']]
x_label = [str(x) for x in df['year']]
y1_tick = [x for x in range(15,35,5)]
y1_label = ['$' + str(x)+' billion' for x in range(15,35,5)]
y2_tick = [x for x in range(4000,10001, 2000)]
y2_label = [str(x) + ' suicides' for x in range(4000,10001, 2000)]

# frame
ax = fig.add_subplot(111)
ax1 = ax.twiny()
ax2 = ax.twinx()

# line 1 for US spending
ref1, = ax.plot(x, line1, 'r-',
                marker = 'o',
                markevery = 10)
ax.set_yticks(y1_tick)
ax.set_yticklabels(y1_label)
ax.tick_params(axis='y', colors='red')
ax.set_ylabel('US spending on science',size=12, color = 'r')

# dummy upper x for xticks
ax1.plot(range(1999,2010),np.ones(11)*15, alpha = 0) 
ax1.set_xticks(x_tick)
ax1.set_xticklabels(x_label)
ax1.set_ylim([15,30])
ax1.tick_params(axis='x', colors='red')

# line 2
ref2, = ax2.plot(x, line2, 'k-', 
                 marker = 'd', 
                 markevery = 10)
ax2.set_xticks(x_tick)
ax2.set_xticklabels(x_label)
ax2.set_yticks(y2_tick)
ax2.set_yticklabels(y2_label)
ax2.set_ylabel('Hanging suicides',size=12)

# remove box
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)

# add grid line
plt.grid(color='k', axis = 'y', alpha =0.5)

# set title
plt.title("US spending on science, space and techonology \n"  
          "correlate with \n" 
          "Suicides by hanging, stangulation and suffocation \n" 
          "correlation: 99.79% (r=0.99789126)",
           y=1.09, fontweight='bold')

# set legend
plt.legend([ref2, ref1], 
           ['Hanging suicides', 'US spending on science'], 
           loc='upper center', 
           bbox_to_anchor = (0.5, -0.1), 
           ncol = 2)

# save fig
plt.savefig('task21.png', format = 'PNG', bbox_inches =  'tight')

