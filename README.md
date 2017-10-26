# Replication study of Destexhe 2009 paper

This repository is aimed at replicating with PyNN the full paper of Alain Destexhe "Self-sustained asynchronous irregular states and Up/Down states in thalamic, cortical and thalamocortical networks of nonlinear integrate-and-fire neurons" (Journal of Computational Neuroscience 27: 493-506, 2009).

See also Andrew Davison's post on porting to PyNN one figure of this paper (http://andrewdavison.info/notes/porting-NEURON-PyNN/).


## Installation of NEST, NEURON, and pyNN

###1. Create a virtualenv
with either virtualenv, virtualenwrapper, or conda.

In the reminder of this text we will use the name 'pynn' for our virtualenv.

###2. Install pyNN
~~~~
(pynn)$ pip install pyNN
~~~~

###3. Add the requirements for numpy and scipy
~~~~
$ sudo apt-get install libblas-dev libblas-doc libblas3 liblapack-dev liblapack-doc liblapack3 liblapacke liblapacke-dev
~~~~

###4. Add requirements for matplotlib
~~~~
$ sudo apt-get install libfreetype6 libfreetype6-dev libpng12-0 libpng12-dev
~~~~

###5. Download the latest version of NEST that is compatible with PyNN
- Compatibility: http://neuralensemble.org/docs/PyNN/installation.html#installing-nest-and-pynest
- Versions of NEST: http://www.nest-simulator.org/download/


###6. Install NEST
Follow the instructions at http://www.nest-simulator.org/installation/ or

####6.1. Prerequisites for NEST
Install the following packages (they will be installed system-wide):
~~~~
$ sudo apt-get install build-essential autoconf automake libtool libltdl7-dev libreadline6-dev libncurses5-dev libgsl0-dev python-all-dev python-numpy python-scipy python-matplotlib ipython
$ sudo apt-get install openmpi-bin openmpi-common libopenmpi-dev
~~~~

####6.2 Download and install the latest NEST
~~~~
(pynn)$ tar -xvf nest-2.10.0.tar.gz
(pynn)$ cd nest-2.10.0/
(pynn)$ ./configure --with-mpi  --prefix=$HOME/opt/nest
(pynn)$ make
(pynn)$ make install
(pynn)$ make installcheck
~~~~

####6.3 Tell bash how to find NEST
~~~~
(pynn)$ vi .bashrc
~~~~

and add the following lines at the end of the file:
~~~~
export PATH=$PATH:$HOME/opt/nest/bin
export PYTHONPATH=$HOME/opt/nest/lib/python2.7/site-packages:$PYTHONPATH
~~~~

####6.4 fast test
> (pynn)$ python

~~~~
>>> import nest
-- N E S T --

Copyright (C) 2004 The NEST Initiative
Version 2.10.0 Jun 24 2016 13:15:45

This program is provided AS IS and comes with
NO WARRANTY. See the file LICENSE for details.

Problems or suggestions?
Visit http://www.nest-simulator.org

Type 'nest.help()' to find out more about NEST.
>>>
~~~~

####6.5 Tell NEST how to use mpi
~~~~
$ vi .nestrc
~~~~
and uncomment the command mpirun at the beginning of nestrc

###7. Install NEURON
Read the instructions on:

- http://www.davison.webfactional.com/notes/installation-neuron-python/
- http://www.neuron.yale.edu/neuron/download/compile_linux

####7.1 Simple installation
Under Linux (with admin privilege) with support for python will be:
~~~~
./configure --without-iv --with-nrnpython
(pynn)$ make
(pynn)$ sudo make install
~~~~

Create the file nrnenv in /usr/local/nrn with the content:
~~~~
#    export N=/usr/local/nrn
#    export CPU=x86_64 # example, put your own
#    export PATH="$N/$CPU/bin:$PATH"
~~~~

Add the following line to the .bashrc file:
~~~~
#    source /usr/local/nrn/nrnenv
~~~~

Compile the python interpreter and install it in your virtualenv folder:
~~~~
#   $ cd src/nrnpython
#   $ python setup.py install --prefix=$HOME/Envs/pynn
~~~~

Compile neuron modules for pyNN:
~~~~
#   $ cd $HOME/Envs/pynn/local/lib/python2.7/site-packages/pyNN/neuron/nmodl
#   $ nrnivmodl
~~~~


###8. Verify your environment:
~~~~
(pynn)$ pip freeze
~~~~

You should get something like:
~~~~
ConnPlotter==0.7a0  #comes with NEST
lazyarray==0.2.8
neo==0.3.3
numpy==1.11.0
PyNEST==2.10.0   #comes with NEST
PyNN==0.8.1
quantities==0+unknown
Topology==2.10.0     #comes with NEST
matplotlib==1.5.1
NEURON==7.4
NeuroTools==0.3.1
quantities==0+unknown
scipy==0.17.1
~~~~
