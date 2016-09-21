# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join

mypath = "ILSVRC2013_DET_val"
with open("ILSVRC2013_DET_val.txt",'w') as outfile:
    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            outfile.writelines(f + '	1\n')
