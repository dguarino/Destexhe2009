"""
Copyright (c) 2016, Domenico GUARINO, Eloise SOULIER
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL GUARINO AND SOULIER BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import NeuroTools.signals
import numpy as np
import random as rd
import os
from pyNN.utility import Timer
import pickle
from pyNN.utility.plotting import Figure, Panel
import matplotlib.pyplot as plot
from datetime import datetime
from neo.core import AnalogSignalArray
import quantities as pq



def build_network(sim, params):
    sim.setup( timestep=params['dt'] )

    populations = {}
    for popKey,popVal in params['Populations'].iteritems():
        if isinstance(popVal['n'],dict):
            number = int(params['Populations'][popVal['n']['ref']]['n'] * popVal['n']['ratio'])
            populations[popKey] = sim.Population( number, popVal['type'], cellparams=popVal['cellparams'] )
        else:
            populations[popKey] = sim.Population( popVal['n'], popVal['type'], cellparams=popVal['cellparams'] )

    for key in populations.keys():
        populations[key].initialize()

    projections = {}
    for projKey,projVal in params['Projections'].iteritems():
        projections[projKey] = sim.Projection(
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


def run_simulation(sim, params):
    print "Running Network ..."
    timer = Timer()
    timer.reset()
    sim.run(params['run_time'])
    simCPUtime = timer.elapsedTime()
    print "... The simulation took %s ms to run." % str(simCPUtime)


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


def save_data(populations, folder, addon=''):
    print "saving data"
    for key,p in populations.iteritems():
        if key != 'ext':
            data = p.get_data()
            p.write_data(folder+'/'+key+addon+'.pkl', annotations={'script_name': __file__})


def analyse(params, folder='results', addon='', removeDataFile=False):
    print "analysing data"
    # populations key-recorders match
    populations = {}
    for popKey,popVal in params['Populations'].iteritems():
        if popKey != 'ext':
            populations[popKey] = params['Recorders'][popKey].keys()
            print popKey, populations[popKey]

    scores = {}

    # default results name folder
    if folder=='results':
        dt = datetime.now()
        date = dt.strftime("%d-%m-%I-%M")
        folder = folder+'/'+date

    # iteration over populations and selctive plotting based on available recorders
    for key,rec in populations.iteritems():
        print key

        neo = pickle.load( open(folder+'/'+key+addon+'.pkl', "rb") )
        data = neo.segments[0]

        panels = []
        if 'v' in rec:
            vm = data.filter(name = 'v')[0]
            panels.append( Panel(vm, ylabel="Membrane potential (mV)", xlabel="Time (ms)", xticks=True, yticks=True, legend=None) )

        if 'gsyn_exc' in rec:
            gsyn_exc = data.filter(name="gsyn_exc")[0]
            panels.append( Panel(gsyn_exc,ylabel = "Exc Synaptic conductance (uS)",xlabel="Time (ms)", xticks=True,legend = None) )

        if 'gsyn_inh' in rec:
            gsyn_inh = data.filter(name="gsyn_inh")[0]
            panels.append( Panel(gsyn_inh,ylabel = "Inh Synaptic conductance (uS)",xlabel="Time (ms)", xticks=True,legend = None) )

        if 'spikes' in rec:
            panels.append( Panel(data.spiketrains, xlabel="Time (ms)", xticks=True, markersize=1) )
            # Spike Count
            scores['SC'] = 0
            if hasattr(data.spiketrains[0], "__len__"):
                scores['SC'] = len(data.spiketrains[0])
            # ISI
            isitot = isi([data.spiketrains[0] * params['dt']])
            scores['ISI'] = 0.0
            scores['CV'] = 0.0
            if hasattr(isitot, "__len__"):
                scores['ISI'] = np.mean(isitot)/len(isitot)
                scores['CV'] = cv([data.spiketrains[0] * params['dt']])
            # firing rate
            fr = rate(params, data.spiketrains, bin_size=10)
            fig = plot.figure(56)
            plot.plot(fr,linewidth=2)
            plot.ylim([.0,1.])
            fig.savefig(folder+'/firingrate_'+key+addon+'.png')
            fig.clear()

        if params['Injections']:
            amplitude = np.array([0.]+params['Injections']['cell']['amplitude']+[0.])#[0.,-.25, 0.0, .25, 0.0, 0.]
            start = np.array([0.]+params['Injections']['cell']['start']+[params['run_time']])/params['dt']
            current = np.array([])

            for i in range(1,len(amplitude)):
                if current.shape == (0,):
                    current = np.ones((start[i]-start[i-1]+1,1))*amplitude[i-1]
                else:
                    current = np.concatenate((current,np.ones((start[i]-start[i-1],1))*amplitude[i-1]),0)
            current = AnalogSignalArray(current, units = 'mA',sampling_rate = params['dt']*pq.Hz)
            current.channel_index = np.array([0])
            panels.append( Panel(current,ylabel = "Current injection (mA)",xlabel="Time (ms)", xticks=True, legend=None) )

        Figure( *panels ).save(folder+'/'+key+addon+".png")

        # LFP
        if 'v' in rec and 'gsyn_exc' in rec:
            # LFP
            lfp = LFP(data)
            lfp = lfp.reshape(((params['run_time']/params['dt'])+1,1))
            vm = data.filter(name = 'v')[0]
            fig = plot.figure()
            plot.plot(lfp)
            fig.savefig(folder+'/LFP_'+key+addon+'.png')
            fig.clear()
            # Vm histogram
            fig = plot.figure()
            ylabel = key
            n,bins,patches = plot.hist(np.mean(vm,1),50)
            fig.savefig(folder+'/Vm_histogram_'+key+addon+'.png')
            fig.clear()

        # for systems with low memory :)
        if removeDataFile:
            os.remove(folder+'/'+key+addon+'.pkl')

    print scores
    return scores


def LFP(data):
    v = data.filter(name="v")[0]
    g = data.filter(name="gsyn_exc")[0]
    # We produce the current for each cell for this time interval, with the Ohm law:
    # I = g(V-E), where E is the equilibrium for exc, which usually is 0.0 (we can change it)
    # (and we also have to consider inhibitory condictances)
    i = g*(v) #AMPA
    # the LFP is the result of cells' currents
    avg_i_by_t = np.sum(i,axis=1)/i.shape[0] #
    sigma = 0.1 # [0.1, 0.01] # Dobiszewski_et_al2012.pdf
    lfp = (1/(4*np.pi*sigma)) * avg_i_by_t
    return lfp


def adaptation_index(data):
    # from NaudMarcilleClopathGerstner2008
    k = 2
    st = data.spiketrains
    #print st
    if st == []:
        return None
    # ISI
    isi = np.diff(st)
    #print isi
    running_sum = 0
    for i,interval in enumerate(isi):
        if i < k:
            continue
        print i, interval
        running_sum = running_sum + ( (isi[i]-isi[i-1]) / (isi[i]+isi[i-1]) )
    return running_sum / len(isi)-k-1



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



def rate( params, spiketrains, bin_size=10 ):
    """
    Binned-time Firing firing rate
    """
    if spiketrains == [] :
        return NaN
    # create bin edges based on number of times and bin size
    bin_edges = np.arange( 0, params['run_time'], bin_size )
    #print "bin_edges",bin_edges.shape
    # binning absolute time, and counting the number of spike times in each bin
    hist = np.zeros( bin_edges.shape[0]-1 )
    for spike_times in spiketrains:
        hist = hist + np.histogram( spike_times, bin_edges )[0]
    return hist / len(spiketrains)



def isi( spiketrains ):
    """
    Inter-Spike Intervals histogram for all spiketrains
    """
    if np.count_nonzero(np.array(spiketrains)) > 1:
        return np.diff( spiketrains )
    else:
        return None



def cv( spiketrains ):
    """
    Coefficient of variation
    """
    if np.count_nonzero(np.array(spiketrains)) > 1:
        return np.std(isi(spiketrains)) / np.mean(isi(spiketrains))
    else:
        return None
