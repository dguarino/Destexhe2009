from pyNN.nest import *
#from pyNN.neuron import *
from pyNN.utility import Timer

params = {

    'run_time': 1000., # ms
    'dt': 0.01, # ms

    'Populations' : {
        'cell' : {
            'n': 1, # units
            'type': EIF_cond_alpha_isfa_ista,
            'cellparams': {
                'tau_m'      : 20.0,  # ms, time constant of leak conductance
                'tau_syn_E'  : 5.0,   # ms, time constant of exponential decay of conductance shift
                'tau_syn_I'  : 10.0,  # ms, as above
                'tau_refrac' : 2.5,   # ms, refractory period
                'v_rest'     : -60.0, # mV, resting potential
                'v_reset'    : -60.0, # mV, reset after spike
                'v_thresh'   : -50.0, # mV, spike threshold
                'v_spike'    : 40.0,  # mV, spike detection
                'delta_T'    : 2.5,   # mV, steepness of exponential approach to threshold
                'tau_w'      : 600.0, # ms, time constant of adaptation variable
                'cm'         : 0.200, # nF, 1 uF/cm^2 with 20000 um^2 is the membrane area
                'a'          : 0.001, # uS, spike-frequency adaptation
                'b'          : .005,  # nA, increment to the adaptation variable
                #'i_offset'   : 0.25,  # nA, constant injected current
            }
        },
    },

    'Projections' : {
    },

    'Injections' : {
        'cell' : {
            'source' : StepCurrentSource,
            'amplitude' : [.25, .0], #[-.25, 0.0, .25, 0.0],
            'start' : [200., 600.], #[200., 600., 1000., 1400.],
            'stop' : 0.0
        },
    },

    'Recorders' : {
        'cell' : {
            'spikes' :  'all',
            'v' : 'all',
            #'v' : {
            #    'start':0,
            #    'end':1
            #}
        },
    },

    'Modifiers' :{
    }

}
