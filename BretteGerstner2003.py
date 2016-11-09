from pyNN.nest import *
from pyNN.utility import Timer

params = {

    'run_time': 1000., # ms
    'dt': 0.01, # ms

    'Populations' : {
        'LTS' : {
            'n': 1, # units
            'type': EIF_cond_alpha_isfa_ista,
            'cellparams': {
                # tau_m = gleak/C, BretteGerstner2005: 30 nS / .281 nF = 106.76
                'tau_m'      : 20, # ms, time constant of leak conductance
                'tau_syn_E'  : 5.0,   # ms, time constant of exponential decay of conductance shift
                'tau_syn_I'  : 10.0,  # ms, as above
                'tau_refrac' : 2.5,   # ms, refractory period
                'v_rest'     : -70.6, # mV, resting potential (Eleak)
                'v_reset'    : -60.0, # mV, reset after spike
                'v_thresh'   : -50.4, # mV, spike threshold
                'delta_T'    : 2.,   # mV, steepness of exponential approach to threshold
                'tau_w'      : 144.0, # ms, time constant of adaptation variable
                'cm'         : 0.281, # nF,
                'a'          : 0.08,  # uS, spike-frequency adaptation for LTS BretteGerstner2005
                'b'          : .0805,  # nA, increment to the adaptation variable
                #'i_offset'   : 0.25,  # nA, constant injected current
            }
        },
    },

    'Projections' : {
    },

    'Injections' : {
        'LTS' : {
            'source' : DCSource,
            'amplitude' : -.8,
            'start' : 20.0,
            'stop' : 420.0
        },
    },

    'Recorders' : {
        'LTS' : {
            #'spikes' :  'all',
            'v' : 'all',
            #'v' : {
            #    'start':0,
            #    'end':1
            #}
        }
    },

    'Modifiers' :{
    }

}
