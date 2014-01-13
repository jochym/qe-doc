#!/usr/bin/python

from qeutil import RemoteQE

# Access info
RemoteQE.user='user'
RemoteQE.host='host.example.com'

# Working directories: local and remote
RemoteQE.wdir='/home/user/calc'
RemoteQE.rdir='calc'

# The job running script.
# You need to replace it by the proper script for your machine.
# Usually not much needs to be changed.
RemoteQE.pbs_template='''#!/bin/bash

cd $PBS_O_WORKDIR

echo "PWscf started at: `date`" 
%(command)s
echo "PWscf finished at: `date`
'''

