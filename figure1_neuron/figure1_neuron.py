# it requires
# - neuron installed (iv not necessary)
#   follow instructions on http://www.davison.webfactional.com/notes/installation-neuron-python/
#   (--without-iv)
# - compilation of IF_BG4.mod:
#   $ nrnivmodl IF_BG4.mod

from neuron import h, nrn, gui
from math import sqrt, pi

def area(sec):
    return sec.L * sec.diam * pi

h.load_file("nrngui.hoc")

h.dt = 0.1 # ms timestep
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
V_REST          = -65                           # figure1A
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

# Relevant parameters
soma.a_IF_BG4        = .001 # figure 1A
soma.b_IF_BG4        = 0.04 # figure 1A
soma.b_IF_BG4        = 0.02 # figure 1B
soma.b_IF_BG4        = 0.0075 # figure 1C

# stimulation
stim = h.IClamp(0.5, sec=soma)
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

# ------------------------------------------------------------------------------
# plotting
from matplotlib import pyplot
pyplot.figure(figsize=(8,4)) # Default figsize is (8,6)
pyplot.plot(t_vec, v_vec)
pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
pyplot.savefig('test.png')
