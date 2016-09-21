# -*- coding: utf-8 -*-


from os import listdir
from os.path import isfile, join, isdir
import numpy as np

lePath = "ILSVRC2014_DET_train"

synsets = [d for d in listdir(lePath) if isdir(join(lePath,d))]

synsetDict = {syn: listdir(join(lePath, syn)) for syn in synsets}

synsetLen = np.array([len(k) for k in synsetDict.values()])

usableSets = [syn for syn in synsets if len(synsetDict[syn])>=400]

np.random.seed(0)
selectedSets = np.random.choice(usableSets, 100)

with open("ILSVRC2014_DET_train.txt",'w') as outfile:
    for idx, syn in enumerate(list(selectedSets)):
        images = np.random.choice(synsetDict[syn],400)
        for image in images:
            outfile.writelines(join(syn, image) + '\t' + "{0}".format(idx) + '\n')
