import numpy as np

params = {
    #'run_time' : [5000],
    #'Populations.py.n' : [1600],
    #'Modifiers.py.cells.end' : [0.12,0.13,0.14],
    #'Modifiers.py.properties.a' : [0.01, .02, 0.03],
    #'Populations.LTS.cellparams.a': [-1., -.5, -.1, -.05, 0., .05, .1, .5, .1],
    #'Populations.LTS.cellparams.b': [-1., -.5, -.1, -.05, 0., .05, .1, .5, .1],

    #'Populations.RS.cellparams.tau_m': [20., 30.], # 80nS BretteGerstner2005 figure 3D
    #'Populations.cell.cellparams.tau_w': [150., 250., 350., 450., 550., 650.], # 80nS BretteGerstner2005 figure 3D
    #'Populations.cell.cellparams.cm': [.1, .15, .18, .20, .22], # 80nS BretteGerstner2005 figure 3D

    'Populations.cell.cellparams.a': np.arange(1., 40., 2.),
    'Populations.cell.cellparams.b': np.arange(0., .4, .02),

    # search Thalamic to be confronted with the SlowDyn project TC results
    #'Populations.cell.cellparams.a' : [8.,9.,10.,11.,12.,13.,14.,15.,16.,17.],
    #'Populations.cell.cellparams.b' : [0.,0.01,0.02,0.03,0.04,0.05],

    # search Reticular to be confronted with the SlowDyn project TC results
    #'Populations.cell.cellparams.b':[-0.04,-0.03,-0.02,-0.01,0.,0.01,0.02,0.03,0.04,0.05,0.06],
    #'Populations.cell.cellparams.a' : [20.,22.,24.,26.,28.,30.,32.,34.,36.,38.,40.],

}

# LTS
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
# all interval
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}

#interessante per LTS bursting
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}


# candidate RE:
# rebound burst and adaptation

# best 11-11-06-45
#RS-{'Populations.RS.cellparams.a': 23.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15} !!!
#RS-{'Populations.RS.cellparams.a': 23.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.2}!!!
#RS-{'Populations.RS.cellparams.a': 23.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1} !!!
#RS-{'Populations.RS.cellparams.a': 23.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.2}
#RS-{'Populations.RS.cellparams.a': 23.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1} !!! burst
#RS-{'Populations.RS.cellparams.a': 23.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1} !!!
#RS-{'Populations.RS.cellparams.a': 23.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18} !!!
# ... up to
#RS-{'Populations.RS.cellparams.a': 23.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.22}

#11-11-06-32
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}

#11-11-06-33
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}

# 11-11-06-36 best
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 450.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}

# 11-11-06-37 best
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 450.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}

# 11-11-06-41
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 450.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1} !!!





# candidate TC:

# best so far (real rebound burst and little adapatation)
# 11-11-06-35 36
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18}
# 11-11-06-38
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
# 11-11-06-39
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.2}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 450.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.22}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.2}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.22}

#super
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
# 11-11-06-40
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.2}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1} !!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.2}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15} !!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18} !!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.22}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 450.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 450.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 450.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.2}
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 450.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15} !!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 450.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18} !!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1} !!!!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}!!!!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.2} !!!!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18}!!!!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}!!!!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.2} !!!!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}!!!!
#RS-{'Populations.RS.cellparams.a': 15.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18}!!!!

# 43
#RS-{'Populations.RS.cellparams.a': 23.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15} !!

#rebound burst no adaptation
#RS-{'Populations.RS.cellparams.a': 5.0, 'Populations.RS.cellparams.b': 0.1, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}

# 11-11-06-34
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.1}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.1}

# 11-11-06-35
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 150.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.0, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}

# 11-11-06-36
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 250.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 350.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.2}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 450.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 550.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 20.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.15}
#RS-{'Populations.RS.cellparams.a': 10.0, 'Populations.RS.cellparams.b': 0.01, 'Populations.RS.cellparams.tau_w': 600.0, 'Populations.RS.cellparams.tau_m': 30.0, 'Populations.RS.cellparams.cm': 0.18}











# network working ones

#re-{'Projections.tc_re.weight': 0.03, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}
#tc-{'Projections.tc_re.weight': 0.03, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#re-{'Projections.tc_re.weight': 0.03, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.05, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}
#tc-{'Projections.tc_re.weight': 0.03, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.05, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#re-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}
#tc-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#re-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}
#tc-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}

#re-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.05, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}
#tc-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.05, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#re-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.06, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}
#tc-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.06, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}

#re-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.1, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#tc-{'Projections.tc_re.weight': 0.03, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.1, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#tc-{'Projections.tc_re.weight': 0.03, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.1, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#re-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.05, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}

#tc-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.05, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}

#re-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.06, 'Populations.re.cellparams.b': 0.05, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}

#tc-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.06, 'Populations.re.cellparams.b': 0.05, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}

#re-{'Projections.tc_re.weight': 0.03, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 30.0, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#re-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.1, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}

#re-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 30.0, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#re-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.06, 'Populations.re.cellparams.b': 0.1, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}

#tc-{'Projections.tc_re.weight': 0.03, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 30.0, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#tc-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.1, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}

#tc-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.03, 'Populations.re.cellparams.b': 0.01, 'Populations.re.cellparams.a': 30.0, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.03}

#tc-{'Projections.tc_re.weight': 0.06, 'Projections.re_tc.weight': 0.06, 'Projections.re_re.weight': 0.06, 'Populations.re.cellparams.b': 0.1, 'Populations.re.cellparams.a': 20, 'Populations.tc.cellparams.a': 23.0, 'Projections.ext_tc.weight': 0.06}

#
