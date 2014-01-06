QE-doc
======

Docs and examples for Quantum-Espresso environment inside iPython notebooks.

Installation
============

The use of the qe-util/nipy packages require some preparations to be made first.
You need to install and configure several packages first. 
The operation is fairly simple and contains just a few steps.

Pre-requisites
--------------

To run the programs you need a fairly recent linux system. 
Any decent and modern linux distribution will do but the code was developed and
tested on Ubuntu 13.10/64.

You will need the current python install with virtualenv system installed.

The installation instructions for the virtualenv package can be found on 
its web page: http://www.virtualenv.org/

Your system should also have a basic set of development packages installed:

 - gcc
 - g++
 - development libraries

Installation
------------

It is best to perform all your work in the python virtualenv. 
To create one go to the directory of your choice and run 
(nipy is a name of the environment we have chosen, you can use a different 
name, just stick with it):

    virtualenv nipy

This will create the nipy directory which is a place all software will be 
installed. You *do not need* to work in this directory! In fact it is better 
not too. If you have a recent and complete distribution and you know what you 
are doing  you can try to use a --site-packages option to virtualenv and skip 
the installation of packages already present in your system. Just remember that
this is not supported and tested variant (but it should work anyway).

Next step is activatiion. Execute in your terminal a following line:

    source nipy/bin/activate

replacing the nipy by your path to the environment directory. This command 
activates the environment. To deactivate simply run:

    deactivate

Next you need to install the software. Activate the environment and run:

    pip install ipython
    pip install pyzmq
    pip install jinja2
    pip install tornado
    pip install numpy
    pip install scipy
    pip install matplotlib

This will take some time but should execute without problems. 

Next go to the ASE website: https://wiki.fysik.dtu.dk/ase/download.html
and download a latest tarball. At this moment it is: 
https://wiki.fysik.dtu.dk/ase-files/python-ase-3.8.1.3440.tar.gz

Unpack it in some temporary place, enter its directory and run:

    python setup.py install

The last step is installation of the qe-util package. 
It is simple, just execute:

    pip install qeutil

Now you have a ready working environment.

Configuration
-------------

The system is configured by default to use a quantum espresso software 
present and configured locally. The installation of the Q-E software is beyond 
the scope of this tutorial. The debian and ubuntu distributions provide 
stable but fairly old versions of this package. It is highly recommended to 
obtain a recent version or, better still, to use one installed in some HPTC 
centre. The example of such remote configuration is provided in the examples.

Essentially you need to figure out how to transport files from your 
workstation to the computing machine and how to run jobs there. 
One very comfortable way of doing this is mounting the remote directory 
locally using sshfs and setting up the key-authentication execution over ssh
to the computing machine. Such a setup makes the "remoteness" of the 
calculations almost transparent.

Usage
-----

Since the qe-util package is designed to be used inside the iPython notebook
environment go to the directory where you downloaded the example notebooks 
(*.ipynb files - it should be *outside* of the nipy tree) and run (remember 
to have the nipy environment activated!) :

    ipython notebook --pylab=inline

Your web browser will open a page with a list of example notebooks. 
Open (click) the first and follow the instructions there.



