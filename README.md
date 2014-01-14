QE-doc
======

QE-Doc is a set of examples for Quantum-Espresso environment inside iPython notebooks. 
It is connected with
the [qe-util](https://github.com/jochym/Elastic) and [elastic](https://github.com/jochym/Elastic) 
packages developed by Paweł T. Jochym. Part of the development was done during my stay 
at the University of Saskachwan, Canada with the joint support of:

* Department of Engeenering and Department of Physics of University of Saskachewan, Saskatoon, Canada
* Department of Computational Material Science of the Institute of Nuclear Physics, PAN, Cracow, Poland. 

The docs and examples in the form of a series of [iPython](http://www.ipython.org/) notebooks
are vieweble and downloadeble from the nbviewer links below. The support files are stored in 
this repository and can be cloned or directly downloded as 
a [zip archive](https://github.com/jochym/qe-doc/archive/master.zip).

Obviously, to get some use from these tutorials and to further use the software in 
the `qe-util` and `elastic` packages you need to have at least cursory knowledge of the 
[python](http://www.python.org) language and iPython notebook environment. 
Go ahead and go to the iPython website to teach yourself - if you need to. 
No advanced knowledge of python is required for understanding the tutorials and you will
pick up the knowledge quickly when you start to exoperiment.

You will also need to understand at least the basics of the 
[Quantum Espresso](http://www.quantumespresso.org) package ([Tutorials prepared by the Q-E group](http://www.fisica.uniud.it/~giannozz/QE-Tutorial/)) as well as the [ASE](https://wiki.fysik.dtu.dk/ase/) system. 
Finally, of course you will need understand the physics behind it all.

You should start with the configuration of your working environment. 
The [Installation](http://nbviewer.ipython.org/gist/jochym/a7f552e8b1fced1bc996) document will help with this task.
Do not be scared by the multiple steps in the procedure. Al should work quite smoothly and at the end you will have an environment usefull not only for viewing and exprerimenting with the tutorials but suitable for the day-to-day research work (it is actually a slimmed down and cleaned up version of my working environment).

Then preceed to the tutorials - view them from the links below and then download them (the download link is in the upper right corner of each tutorial page) and play with them - this is the fastest way to get a grip on the software.

**Note:** The software is under active development, so do expect some changes in the api from time to time.

Tutorials
---------

Here is the list of tutorials. It will probably grow in time a little. If you wish to include your tutorial in the list I will be happy to add any material which concerned with similar tasks.

* [Crystal structure](http://nbviewer.ipython.org/gist/jochym/603c0d13bc7d3dc8148d) - introduces the basic ideas of the system and presents a set of basic static calculations.
* [Remote execution](http://nbviewer.ipython.org/gist/jochym/d504ce067b99686e4ae8) - shows how to set-up the remote execution of the Qeuantum Espresso over the network (e.g. in some supercomputing center).
* [Elastic constants](http://nbviewer.ipython.org/gist/jochym/5fb472070a272b61f75c) - introduces the `elastic` package and shows the calculation of elastic constants using this tool.
* [Lattice dynamics](http://nbviewer.ipython.org/gist/jochym/f3f37daa4cf1884f02ad) - shows the use of DFPT module in Quantum Espresso for calculation of vibration modes in the crystal as well as use of utility functions in the `qe-util` for easier analysis of the obtained data.
* [Primitive unit cells](http://nbviewer.ipython.org/gist/jochym/d68d81026eed03467d69) - demonstrates the concept of the primitive unit cell and shows a way the system deals with them.
* [Structure optimization](http://nbviewer.ipython.org/gist/jochym/) - shows how to find minimum of energy of the system whith more degrees of freedom (low symmetry structures etc.). The example of structure minimization for a simple structure is included in the first tutorial.
* [Electronic structure calculation](http://nbviewer.ipython.org/gist/jochym/99f18778525832746d48) - shows how to extract the basic properties of the electronic structure of the crystal from the data produced by the calculation.




