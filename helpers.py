import NeuroTools.signals
import numpy as np
import random as rd
import os
from numpy import *
from pyNN.nest import *
from pyNN.utility import Timer
import pickle
from pyNN.utility.plotting import Figure, Panel
import matplotlib.pyplot as plot
from datetime import datetime


def build_network(params):
    setup( timestep=params['dt'] )

    populations = {}
    for popKey,popVal in params['Populations'].iteritems():
        if isinstance(popVal['n'],dict):
            number = int(params['Populations'][popVal['n']['ref']]['n'] * popVal['n']['ratio'])
            populations[popKey] = Population( number, popVal['type'], cellparams=popVal['cellparams'] )
        else:
            populations[popKey] = Population( popVal['n'], popVal['type'], cellparams=popVal['cellparams'] )

    for key in populations.keys():
        populations[key].initialize()

    projections = {}
    for projKey,projVal in params['Projections'].iteritems():
        projections[projKey] = Projection(
            populations[ projVal['source'] ],
            populations[ projVal['target'] ],
            connector = projVal['connector'],
            synapse_type = projVal['synapse_type'](weight = projVal['weight']),
            receptor_type = projVal['receptor_type']
        )

    for modKey,modVal in params['Modifiers'].iteritems():
        if type(modVal['cells']['start']) == float:
            start = int(modVal['cells']['start'] * populations[modKey].local_size)
        else:
            start = modVal['cells']['start']
        if type(modVal['cells']['end']) == float:
           end = int(modVal['cells']['end'] * populations[modKey].local_size)
        else:
            end = modVal['cells']['end']

        cells = populations[modKey].local_cells
        for key,value in modVal['properties'].iteritems():
            populations[modKey][ populations[modKey].id_to_index(list(cells[ start:end ])) ].set(**{key:value})

    return populations


def perform_injections(params, populations):
    for modKey,modVal in params['Injections'].iteritems():
        if isinstance(modVal['start'], (list)):
            source = modVal['source'](times=modVal['start'], amplitudes=modVal['amplitude'])
        else:
            source = modVal['source'](amplitude=modVal['amplitude'], start=modVal['start'], stop=modVal['stop'])
        populations[modKey].inject( source )


def record_data(params, populations):
    for recPop, recVal in params['Recorders'].iteritems():
        for elKey,elVal in recVal.iteritems():
            #populations[recPop].record( None )
            if elVal == 'all':
                populations[recPop].record( elKey )
            else:
                populations[recPop][elVal['start']:elVal['end']].record( elKey )


def run_simulation(params):
    print "Running Network"
    timer = Timer()
    timer.reset()
    run(params['run_time'])
    simCPUtime = timer.elapsedTime()
    print "Simulation Time: %s" % str(simCPUtime)


def save_data(populations, addon=''):
    print "saving data"
    for key,p in populations.iteritems():
        if key != 'ext':
            data = p.get_data()
            p.write_data('results/'+key+addon+'.pkl', annotations={'script_name': __file__})



def plot_spiketrains(segment):
    for spiketrain in segment.spiketrains:
        y = np.ones_like(spiketrain) * spiketrain.annotations['source_id']
        plot.plot(spiketrain, y,linestyle='dashed', marker='o',markersize =1)
        plot.ylabel(segment.name)
        plot.setp(plot.gca().get_xticklabels(), visible=False)


def plot_signal(signal, index, colour='b'):
    label = "Neuron %d" % signal.annotations['source_ids'][index]
    plt.plot(signal.times, signal[:, index], colour, label=label)
    plt.ylabel("%s (%s)" % (signal.name, signal.units._dimensionality.string))
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.legend()


def load_spikelist( filename, t_start=.0, t_stop=1. ):
    spiketrains = []
    # Data is in Neo format inside a pickle file
    # open the pickle and get the neo block
    neo_block = pickle.load( open(filename, "rb") )
    # get spiketrains
    neo_spikes = neo_block.segments[0].spiketrains
    for i,st in enumerate(neo_spikes):
        for t in st.magnitude:
            spiketrains.append( (i, t) )

    spklist = SpikeList(spiketrains, range(len(neo_spikes)), t_start=t_start, t_stop=t_stop)
    return spklist


def analyse(params, folder='results'):
    print "analysing data"
    populations = {}
    for popKey,popVal in params['Populations'].iteritems():
        populations[popKey] = popVal
    pop_number = len(populations) - 1
    pop_index = 0
    score = {}

    if folder=='results':
        dt = datetime.now()
        date = dt.strftime("%d-%m-%I-%M")
        folder = folder+'/'+date

    for key,p in populations.iteritems():
        print key
        if key != 'ext':
            pop_index = pop_index + 1
            print pop_number,pop_index

            neo = pickle.load( open(folder+'/'+key+'.pkl', "rb") )
            data = neo.segments[0]

            #vm = data.filter(name = 'v')[0]
            #gsyn_exc = data.filter(name="gsyn_exc")
            #gsyn_inh = data.filter(name="gsyn_inh")
            #if not gsyn_exc:
            #    gsyn = gsyn_inh[0]
            #else:
            #    gsyn = gsyn_exc[0]

            Figure(
                #Panel(vm, ylabel="Membrane potential (mV)", xlabel="Time (ms)", xticks=True, yticks=True, legend=None),
                #Panel(gsyn,ylabel = "Synaptic conductance (uS)",xlabel="Time (ms)", xticks=True,legend = None),
                #Panel(rd.sample(data.spiketrains,100), xlabel="Time (ms)", xticks=True, markersize = 1)
                Panel(data.spiketrains, xlabel="Time (ms)", xticks=True, markersize=1)
            ).save(folder+'/'+key+".png")

            #fig = plot.figure(2)
            #plot.subplot(pop_number,1,pop_index)
            #ylabel = key
            #n,bins,patches = plot.hist(np.mean(vm,1),50)
            #fig.savefig('results/'+date+'/'+filename+'hist.png')

            ## metric supposed to characterize bimodality
            #bins = bins[:-1]
            #prop_left = sum([n[i] for i,data in enumerate(bins) if bins[i]<(np.mean(vm)-np.std(vm)/2)])/sum(n)
            #prop_right = sum([n[i] for i,data in enumerate(bins) if bins[i]>(np.mean(vm)+np.std(vm)/2)])/sum(n)
            #score[key] = float("{0:.2f}".format(prop_left*prop_right))
            #print "prop_left",prop_left, "prop_right",prop_right
            #print "score",prop_left*prop_right

            if pop_index == pop_number :
                fig.clear()

            if key == 'py':
                lfp = compute_LFP(data)
                lfp = lfp.reshape((50001,1))
                print lfp.shape
                vm = data.filter(name = 'v')[0]
                print vm.shape
                fig = plot.figure(1)
                plot.plot(lfp)
                fig.savefig(folder+'/'+'lfp.png')
                fig.clear()

            #TODO ; add parameter file to the result folder

            # for systems with low memory :)
            #os.remove('results/'+key+filename+'.pkl')

    return score


def compute_LFP(data):
    v = data.filter(name="v")[0]
    g = data.filter(name="gsyn_exc")[0]
    # We produce the current for each cell for this time interval, with the Ohm law:
    # I = g(V-E), where E is the equilibrium for exc, which usually is 0.0 (we can change it)
    # (and we also have to consider inhibitory condictances)
    #print 'v', v
    i = g*(v) #AMPA
    #print 'i',i
    # the LFP is the result of cells' currents
    avg_i_by_t = numpy.sum(i,axis=1)/i.shape[0] #
    #print 'avg',len(avg_i_by_t)
    sigma = 0.1 # [0.1, 0.01] # Dobiszewski_et_al2012.pdf
    lfp = (1/(4*numpy.pi*sigma)) *  avg_i_by_t
    return lfp
