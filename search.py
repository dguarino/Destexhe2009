
params = {
    #'run_time' : [5000],
    #'Populations.py.n' : [1600],
    #'Modifiers.py.cells.end' : [0.12,0.13,0.14],
    #'Modifiers.py.properties.a' : [0.01, .02, 0.03],
    #'Populations.LTS.cellparams.a': [-1., -.5, -.1, -.05, 0., .05, .1, .5, .1],
    #'Populations.LTS.cellparams.b': [-1., -.5, -.1, -.05, 0., .05, .1, .5, .1],

    'Populations.LTS.cellparams.a': [13.], # 80nS BretteGerstner2005 figure 3D
    'Populations.LTS.cellparams.b': [0.], # 80nS BretteGerstner2005 figure 3D
    'Populations.LTS.cellparams.tau_w': [720.], # ms, BretteGerstner2005 figure 3D
    'Populations.LTS.cellparams.v_rest': [-60.], # ms, BretteGerstner2005 figure 3D
    'Populations.LTS.cellparams.v_reset': [-45.], # ms, BretteGerstner2005 figure 3D

}
