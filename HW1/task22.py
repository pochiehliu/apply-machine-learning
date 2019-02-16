"""
Create a pair-plot of the iris dataset similar to Figure 1-3 in IMLP using 
only numpy and matplotlib (you can use scikit-learn to load the data with 
sklearn.datasets.load_iris, you are not allowed to use pandas). Ensure all 
axes are labeled. The diagonals need to contain histograms, the different 
species need to be distinguished by color or glyph, and there needs to be a
legend for the species.

reference for generating single legend for multiple subplots
https://stackoverflow.com/questions/9834452/how-do-i-make-a-single-legend-for-many-subplots-with-matplotlib
https://matplotlib.org/examples/pylab_examples/figlegend_demo.html
no ticks
https://stackoverflow.com/questions/12998430/remove-xticks-in-a-matplotlib-plot
no white space
https://stackoverflow.com/questions/41071947/how-to-remove-the-space-between-subplots-in-matplotlib-pyplot
super title
https://stackoverflow.com/questions/7066121/how-to-set-a-single-main-title-above-all-the-subplots-with-pyplot
adjust subplot marginal space
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots_adjust.html 
"""

import matplotlib.pyplot as plt
import sklearn.datasets

# import data
df = sklearn.datasets.load_iris()

# extract x and y
x, y = df['data'], df['target']

# save for labels
feature_names =  df['feature_names']
target_names = df['target_names']

# constants 
row = col = 4
color_map =['b','r','g']

# frame, ax can be accessed as matrix form ax[i][j]
fig, ax = plt.subplots(row, col, figsize=(15, 15))
handle_collection = []

# set up title
plt.suptitle('Pair plot of the Iris dataset, colored by class label', 
             fontsize= 35)

# generate plot
for i in range(row):
    for j in range(col):
        # diagonal: plot histogram
        if i == j:
            ax[i][j].hist(x[:, i], bins=20, color='b', edgecolor='k')
        # others
        else:
            for idx in range(3):
                partial_x = x[y==idx]
                handle = ax[i][j].scatter(partial_x[:,j], 
                                          partial_x[:,i],
                                          color = color_map[idx],
                                          edgecolor='k',
                                          s = 90,
                                          alpha = 0.6,
                                          label=target_names[idx])
                handle_collection.append(handle)
# set up ticks
for i in range(row):
    for j in range(col):
        if (i < 3):
            ax[i][j].set_xticks([])
            ax[i][j].set_xticklabels([])
        if (j > 0):
            ax[i][j].set_yticks([])
            ax[i][j].set_yticklabels([])

# set up labels
for i in range(row):
    ax[i][0].set_ylabel(feature_names[i], fontsize = 20)
     
for j in range(col):                   
    ax[3][j].set_xlabel(feature_names[j], fontsize = 20)

# remove white spalce
plt.subplots_adjust(wspace=0, hspace=0)

# legend
fig.legend(handle_collection, 
           target_names, 
           loc = 'lower center', 
           ncol = 3,
           fontsize = 20)

# adjust edge
plt.subplots_adjust(bottom=0.09, top=0.94, right=0.93, left=0.07)

# save
plt.savefig('task22.png', format='PNG', bbox_inches =  'tight')