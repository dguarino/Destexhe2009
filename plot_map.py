import csv
import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plot
from params import params

def plot_map( csvfile, factor=100, ref={} ):
    data = list(csvfile)
    header1 = data.pop(0)[0]
    text1, p1 = header1.strip('#').split(':')
    p1 = eval(p1)
    header2 = data.pop(0)[0]
    text2, p2 = header2.strip('#').split(':')
    p2 = eval(p2)
    #axis1 = [ i for j in p2 for i in p1 ]
    axis1 = [ i for j in p2 for i in p1[:-1] ]
    #axis2 = [ j for j in p2 for i in p1 ]
    axis2 = [ j for j in p2 for i in p1[:-1] ]
    combinations = len(p1) * len(p2)
    area = np.zeros(combinations)
    colors = np.zeros(combinations)
    marks = ['o' for i in range(combinations)]
    texts = ['0' for i in range(combinations)]
    font = {'family': 'serif',
            'color':  'grey',
            'weight': 'normal',
            'size': 6,
            }

    i = 0
    for row in data:
        for col in row[:-1]:
            #print col
            scores = eval(col)
            texts[i] = scores[0]
            colors[i] = np.mean(float(scores[1])) # color for ISI
            #area[i] = np.sqrt((ref['CV']-scores[2])**2) * factor # area for CV
            area[i] = scores[2] * factor # area for CV
            i=i+1

    # normalize colors for matplotlib
    fig = plot.figure(1)
    norm = ml.colors.Normalize(vmin=min(colors), vmax=max(colors), clip=True)
    mapper = ml.cm.ScalarMappable(norm=norm, cmap=plot.cm.jet)
    mapper._A = [] # hack to plot the colorbar http://stackoverflow.com/questions/8342549/matplotlib-add-colorbar-to-a-sequence-of-line-plots
    #mapper.set_clim(0.,20.)
    plot.title(ref)
    plot.xlabel(text1)
    plot.ylabel(text2)
    plot.xticks(p1, rotation='vertical')
    plot.yticks(p2)
    #plot.xlim([.0000001,.1]) # TODO: remove!!!! hack just to plot the TC param search
    for x,y,a,c,m,t in zip(axis1,axis2,area,colors,marks,texts):
        #print x,y,a,c
        plot.text( x, y, t, fontdict=font )
        plot.scatter( x, y, s=a, c=mapper.to_rgba(c), marker=m, edgecolors='none' )
    cbar = plot.colorbar(mapper)
    cbar.ax.set_ylabel('mean ISI', rotation=270)
    plot.tick_params(axis='both', which='major', labelsize=8)
    plot.tick_params(axis='both', which='minor', labelsize=8)
    #plot.xscale('log') # TODO: remove!!!! hack just to plot the TC param search
    plot.savefig('search_map.png')
    fig.clear()



# using the function...
factor = 100
#ref = { 'neuron':'1A', 'SC': 7, 'ISI': 7.42, 'CV': 0.8 } # figure 1E neuron
#ref = { 'neuron':'1E', 'SC': 7, 'ISI': 1.4, 'CV': 0.3 } # figure 1E neuron
reader = csv.reader( open('results/figure1_search/map.csv', 'rb') )
plot_map(reader, factor, "interval for figure 1")
