QE-doc
======

*This work was supported in part by a grant from the National Sciences and Engineering 
Research Council of Canada, University of Saskatchewan, and the Department of Computational
Material Science of the Institute of Nuclear Physics, PAN, Cracow, Poland. 
The access to high performance supercomputers provided by Compute Canada 
(CLUMEQ and Westgrid) is acknowledged.*

QE-doc is a set of tutorials for Quantum-Espresso environment inside iPython
notebooks. It is connected with
the [QE-util](https://github.com/jochym/qe-util) and 
[Elastic](https://github.com/jochym/Elastic) 
packages developed by Paweł T. Jochym. Part of the development was done during
my stay at the University of Saskachwan.

The docs and examples in the form of a series of
[iPython](http://www.ipython.org/) notebooks are viewable from the links below.
If you open the links you can download the source from the page itself (icon in
the top-right corner of the page). The support files as well as source for the
tutorials are stored in the [repository](https://github.com/jochym/qe-doc) and
can be cloned or directly downloaded as a 
[zip archive](https://github.com/jochym/qe-doc/archive/master.zip).

Obviously, to get any use from these tutorials and to further use the software
in the QE-util and Elastic packages you need to have at least cursory
knowledge of the [python](http://www.python.org) language and iPython notebook
environment. Go ahead and to the iPython website to teach yourself - if you need
to. 

**But:** *no advanced knowledge of python is required for understanding the
tutorials and you will pick up the required skills quickly when you start to
experiment with the materials.*

You will also need to understand at least the basics of the 
[Quantum Espresso](http://www.quantumespresso.org) package. There is a large
body of documents on the Quantum Espresso website as well as in other places
(e.g. [Tutorials prepared by the Q-E group](http://www.fisica.uniud.it/~giannozz/QE-Tutorial/)). 
Since the whole system is based on the excellent
[ASE](https://wiki.fysik.dtu.dk/ase/) library you should study the documentation
on their website at some point in time as well. This may wait until you start
more serious experimentation. You should understand the tutorials without
detailed knowledge of the ASE system. Finally, of course you will need
understand the physics behind it all.

Installation
------------

You can *view* the tutorials with just your browser (just click the links below),
but to *work* on them (which is a whole point of having a tutorial!) you need 
a working environment - so you need to build and configure one.

The [Installation](http://nbviewer.ipython.org/gist/jochym/a7f552e8b1fced1bc996)
document will help with this task. Do not be scared off by the multiple steps in
the procedure. All should work quite smoothly, and at the end you will have an
environment useful not only for viewing and experimenting with the tutorials but
suitable for the day-to-day research work (it is actually a slimmed down and
cleaned up version of my working environment).

Alternatively, we have prepared a [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
image of a 
[fully installed and configured system](http://wolf.ifj.edu.pl/jochym/NiPy-VirtualBox-appliance.ova). 
Ready to be imported into
the virtualization software. It is not the most effective way to use the 
software - but it is definitively the fastest one (it takes 3-5 minutes from 
downloading the image to opening first tutorial).

Then proceed to the tutorials - view them from the links below, download
them (the download link is in the upper right corner of the tutorial page) and
play with them - this is the fastest way to get a grip on the software.

**Note:** The software is under active development, so do expect some changes in
the api from time to time.

Tutorials
---------

Here is the list of tutorials. It will probably grow in time a little. If you
wish to include your tutorial in the list we will be happy to add any material
which concerned with similar tasks.

* [Crystal structure](http://nbviewer.ipython.org/gist/jochym/603c0d13bc7d3dc8148d) -
    introduces the basic ideas of the system and presents a set of basic static
    calculations.
* [Remote execution](http://nbviewer.ipython.org/gist/jochym/d504ce067b99686e4ae8) - 
    shows how to set-up the remote execution of the Qeuantum Espresso over the
    network (e.g. in some supercomputing center).
* [Primitive unit cells](http://nbviewer.ipython.org/gist/jochym/d68d81026eed03467d69) - 
    demonstrates the concept of the primitive unit cell and shows a way the
    system deals with them.
* [Structure optimization](http://nbviewer.ipython.org/gist/jochym/f7b46f20640f3e2e7634) - 
    shows how to find minimum of energy of the system with more degrees of
    freedom (low symmetry structures etc.). The example of structure
    minimization for a simple structure is included in the first tutorial.
* [Elastic constants](http://nbviewer.ipython.org/gist/jochym/5fb472070a272b61f75c) - 
    introduces the Elastic package and shows the calculation of elastic
    constants using this tool.
* [Lattice dynamics](http://nbviewer.ipython.org/gist/jochym/f3f37daa4cf1884f02ad) - 
    shows the use of DFPT module in Quantum Espresso for calculation of
    vibration modes in the crystal as well as use of utility functions in the
    QE-util for easier analysis of the obtained data.
* [Quasi-Harmonic Approximation](http://nbviewer.ipython.org/gist/jochym/334b658cc8b3f6864c23) - 
    explains the procedure of calculating temperature-dependent behaviour in the
    framework of the QHA using the tools provided within the QE-util package.



