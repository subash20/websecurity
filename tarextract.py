#!/usr/bin/env python

import os
import tarfile
import sys


for item in os.listdir('/scripts'):
    if tarfile.is_tarfile(item):
        print item +"is tar file"
        data=tarfile.open(item,'r:gz')
        print "######### tar file info #########"
        #print data.name + " : size is :"+str(data.size)
        for thing in data:
            print "name :"+thing.name + "size :"+str(thing.size)
        print "**********************************"
        data.close()
       # for info in data:
       #     print info.list()
    else:
        print item +"is not tar file"

