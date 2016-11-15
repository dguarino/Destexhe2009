import NeuroTools.signals
import numpy.random
import os
from pyNN.nest import *
from numpy import *
import matplotlib.pyplot as plot
from pyNN.utility import Timer
import sys, getopt

import helpers as h

usage_str = 'usage: run.py -p<param file> -a -f<data folder>'
doAnalaysisOnly = False
data_folder = 'results'

try:
    opts, args = getopt.getopt(sys.argv[1:], "haf:p:" )
except getopt.GetoptError:
    print usage_str,"error"
    sys.exit(2)
if len(opts)==0:
    print usage_str,"empty opts"
for opt, arg in opts:
    if opt == '-h':
        print usage_str
        sys.exit()
    elif opt == '-a':
        print "Running analysis and plotting only ..."
        doAnalaysisOnly=True
    elif opt == '-f':
        data_folder = arg
        print "Data will be saved in:", data_folder
    elif opt == '-p':
        print "Using parameter file:", arg
        external = __import__(arg)

if not doAnalaysisOnly:
    Populations = h.build_network(external.params)
    h.record_data(external.params, Populations)
    h.perform_injections(external.params, Populations)
    h.run_simulation(external.params)
    h.save_data(Populations, data_folder)
    end()

h.analyse(external.params, data_folder)
