# it requires
# - neuron installed (iv not necessary)
#   follow instructions on
#   http://www.davison.webfactional.com/notes/installation-neuron-python/
#   http://www.neuron.yale.edu/neuron/download/compile_linux
#   Simplest installation under Linux with support for python:
#   ./configure --without-iv --with-nrnpython
#   $ make
#   $ sudo make install

#   create the file nrnenv in /usr/local/nrn with the content:
#    export N=/usr/local/nrn
#    export CPU=x86_64 # example, put your own
#    export PATH="$N/$CPU/bin:$PATH"

#   add the following line to the .bashrc file:
#    source /usr/local/nrn/nrnenv

#   compile the python interpreter and install it in your virtualenv folder:
#   $ cd src/nrnpython
#   $ python setup.py install --prefix=$HOME/Envs/pynn

# - compile neuron modules for pyNN:
#   $ cd $HOME/Envs/pynn/local/lib/python2.7/site-packages/pyNN/neuron/nmodl
#   $ nrnivmodl

# - compilation of IF_BG4.mod:
#   $ nrnivmodl IF_BG4.mod

from neuron import h, nrn, gui
from math import sqrt, pi
import pickle
import numpy as np

def area(sec):
    return sec.L * sec.diam * pi

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



h.load_file("nrngui.hoc")

# -----------------------
h.dt = 0.01 # ms timestep
h.steps_per_ms = 1.0/0.1
tstart = 0
h.tstop = 1000
h.v_init = -60.0

# Cell parameters
LENGTH          = sqrt(20000/pi)                # in um
DIAMETER        = sqrt(20000/pi)                # in um
AREA            = 1e-8 * pi * LENGTH * DIAMETER # membrane area in cm2
TAU             = 20                            # time constant in ms
CAPACITANCE     = 1                             # capacitance in muF/cm2
G_L             = 1e-3 * CAPACITANCE / TAU      # leak conductance in S/cm2
V_REST          = -60                           # resting potential
#V_REST          = -65                           # figure1A
TAU_W           = 600
DELTA           = 2.5
# Spike parameters
VTR             = -50           # threshold in mV
VTOP            = 40            # top voltage during spike in mV
VBOT            = -60           # reset voltage in mV
REFRACTORY      = 5.0/2         # refractory period in ms (correction for a bug in IF_CG4)


# Destexhe2009 figure 1 cells
soma = nrn.Section()
soma.insert('pas')
soma.insert('IF_BG4')
#nclist = []

soma.L               = LENGTH # 20000 um^2
soma.diam            = DIAMETER
soma.e_pas           = V_REST
soma.g_pas           = G_L

soma.Vtr_IF_BG4      = VTR
soma.Ref_IF_BG4      = REFRACTORY
soma.Vtop_IF_BG4     = VTOP
soma.Vbot_IF_BG4     = VBOT
soma.tau_w_IF_BG4    = 600
soma.EL_IF_BG4       = soma.e_pas
soma.GL_IF_BG4       = soma.g_pas
soma.delta_IF_BG4    = 2.5
soma.surf_IF_BG4     = area(soma)

# Relevant parameters to reproduce figure1
soma.a_IF_BG4        = .001 # figure 1ABC Destexhe2009
#soma.a_IF_BG4        = .02 # figure 1D Destexhe2009
#soma.a_IF_BG4        = .04 # figure 1E Destexhe2009
#soma.a_IF_BG4        = .08 # figure 1F Destexhe2009

soma.b_IF_BG4        = .04     # figure 1A
#soma.b_IF_BG4        = .005    # figure 1B Destexhe2009
#soma.b_IF_BG4        = .02     # figure 1B closer to figure
#soma.b_IF_BG4        = .0      # figure 1CDE Destexhe2009
#soma.b_IF_BG4        = .03     # figure 1F Destexhe2009
#soma.b_IF_BG4        = .0075   # figure 1C closer to figure

# stimulation
stim = h.IClamp(0.5, sec=soma)
stim.amp = -.25 # Destexhe2009
stim.amp = .25 # nA
stim.delay = 200.0 # ms
stim.dur = 400.0 ## Some float

# recording
v_vec = h.Vector()             # Membrane potential vector
t_vec = h.Vector()             # Time stamp vector
v_vec.record( soma(0.5)._ref_v )
t_vec.record( h._ref_t )

# run the simulation
h.init()
h.run()

with open('t_vec.p', 'w') as t_vec_file:
    pickle.dump(t_vec.to_python(), t_vec_file)
with open('v_vec.p', 'w') as v_vec_file:
    pickle.dump(v_vec.to_python(), v_vec_file)

# check saved data
#with open('v_vec.p') as vec_file:
#    py_v_vec = pickle.load(vec_file)
#    #print py_v_vec

# analysis
vm = np.array( v_vec.to_python() )
#print vm.shape
spiketrains = np.where(vm >= 30.)[0] * h.dt
print "SC",len(spiketrains)
isi_tot = isi([spiketrains])
print 'ISI:', isi_tot
print 'mean ISI:', np.mean(isi_tot)/ len(spiketrains)
print 'CV:', cv([spiketrains])

# ------------------------------------------------------------------------------
# plotting
from matplotlib import pyplot
pyplot.figure(figsize=(8,4)) # Default figsize is (8,6)
pyplot.plot(t_vec, v_vec)
pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
pyplot.savefig('figure1.png')
