"""
Reproduce the graphs on overlapping data from “Fundamentals of Data 
Visualization” https://serialmentor.com/dataviz/overlapping-points.html that 
is figures 18.1 to 18.4, using matplotlib as subplots in a single figure. You 
can find the dataset on the UCI repository here: 
    http://archive.ics.uci.edu/ml/datasets/Auto+MPG 
The code should include reading the data from the web if possible, otherwise 
from a text file for csv file (to be included in the repository).

jitter reference
https://stackoverflow.com/questions/8671808/matplotlib-avoiding-overlapping-datapoints-in-a-scatter-dot-beeswarm-plot
legend
https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# jitter function
def rand_jitter(arr, weight=0.01):
    stdev = weight*(max(arr)-min(arr))
    return arr + np.random.randn(len(arr)) * stdev

# read file
df = pd.read_csv('mpg.csv', 
                 sep=',', 
                 header=0, 
                 index_col = 0)

# frame
fig, ax = plt.subplots(2, 2, figsize=(20, 15))

# look up table
drv_map = ['f', 'r', '4']
drv_name = ['FWD', 'RWD', '4WD']
color_map = ['orange', 'b', 'k']

# vertical line
ax[0][0].axvline(x=7.3, color = 'r', linewidth = 10)
ax[1][1].axvline(x=7.3, color = 'r', linewidth = 10)

# text string
textstr = 'bad'
ax[0][0].text(6.8,38,textstr,color = 'r', fontsize = 20)
ax[1][1].text(6.8,38,textstr,color = 'r', fontsize = 20)
# plot
for idx in range(3):
    partial_df = df[ df['drv']==drv_map[idx] ]
    x = partial_df['displ']
    y = partial_df['cty']
    
    for i in range(2):
        for j in range(2):
            # top left 18.1
            if i == j == 0:
                ax[i][j].scatter(x, y, 
                                 color = color_map[idx], 
                                 s = 100, 
                                 label = drv_name[idx])
                ax[i][j].set_title('Figure 18.1', fontsize = 20)
            # top right 18.2
            elif i == 0 and j == 1:
                ax[i][j].scatter(x, y, 
                                 color = color_map[idx], 
                                 s = 100, 
                                 label = drv_name[idx],
                                 alpha = 0.5,
                                 edgecolor = color_map[idx])
                ax[i][j].set_title('Figure 18.2: alpha', fontsize = 20)
            # bottom left 18.3
            elif i == 1 and j == 0:
                jitter_x = rand_jitter(x)
                jitter_y = rand_jitter(y)
                ax[i][j].scatter(jitter_x, jitter_y, 
                                 color = color_map[idx], 
                                 s = 100, 
                                 label = drv_name[idx],
                                 alpha = 0.5,
                                 edgecolor = color_map[idx])
                ax[i][j].set_title('Figure 18.3: alpha and jitter', 
                                   fontsize = 20)
            # bottom right 18.4
            else:
                jitter_x = rand_jitter(x,0.02)
                jitter_y = rand_jitter(y,0.02)
                ax[i][j].scatter(jitter_x, jitter_y, 
                                 color = color_map[idx], 
                                 s = 100, 
                                 label = drv_name[idx],
                                 alpha = 0.5,
                                 edgecolor = color_map[idx])
                ax[i][j].set_title('Figure 18.4: alpha and increase jitter', 
                                    fontsize = 20)
            
            # setup limit ticks labels legends
            ax[i][j].set_ylim(8, 38)
            ax[i][j].set_xlim(1.3, 7.3)
            ax[i][j].set_yticks([x for x in range(10,36,5)])
            ax[i][j].set_xlabel('displacement(I)', fontsize = 20)
            ax[i][j].set_ylabel('fuel economy (mpg)', fontsize = 20)
            ax[i][j].spines['right'].set_visible(False)
            ax[i][j].spines['top'].set_visible(False)
            leg = ax[i][j].legend(title = 'drive train',
                                  frameon=False, 
                                  fontsize =15,
                                  loc = 1)
            leg.get_title().set_fontsize(15)

# title
plt.suptitle('Handling overlapping points demo plots using fuel economy dataset', 
             fontsize= 35)
    
# save
plt.savefig('task23.png', format='PNG', bbox_inches =  'tight')