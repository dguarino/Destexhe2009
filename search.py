{
    #'run_time' : [5000],
    #'Populations.py.n' : [1600],
    #'Modifiers.py.cells.end' : [0.12,0.13,0.14],
    #'Modifiers.py.properties.a' : [0.01, .02, 0.03],

    #'Populations.cell.cellparams.tau_m': [20., 30.],
    #'Populations.cell.cellparams.tau_w': np.arange(.01, 800., 40.),
    #'Populations.cell.cellparams.cm': np.arange(.01, .6, .03),
    'Populations.cell.cellparams.a': np.arange(8., 12., .2),
    'Populations.cell.cellparams.b': np.arange(.001, .08, .004),

    # search Thalamic to be confronted with the SlowDyn project TC results
    #'Populations.cell.cellparams.a' : [8.,9.,10.,11.,12.,13.,14.,15.,16.,17.],
    #'Populations.cell.cellparams.b' : [0.,0.01,0.02,0.03,0.04,0.05],

    # search Reticular to be confronted with the SlowDyn project TC results
    #'Populations.cell.cellparams.b':[-0.04,-0.03,-0.02,-0.01,0.,0.01,0.02,0.03,0.04,0.05,0.06],
    #'Populations.cell.cellparams.a' : [20.,22.,24.,26.,28.,30.,32.,34.,36.,38.,40.],

}
