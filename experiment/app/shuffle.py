# import modules

import numpy as np
import random

import pickle

import files,stimuli
from flask import session

### face identities
# n = number of identities and r = number of expressions
def identList(n,r):
    myList= []
    j = 0
    while j < n:
        i = 0
        while i < r:
            myList.append(j)
            i += 1
        j += 1
    return myList

### basic expressions
# n = number of expressions, r = number of identities
def expressList(n,r):
    myList= []
    j = 0
    while j < r:
        i = 0
        while i < n:
            myList.append(i)
            i += 1
        j += 1
    return myList


### shuffle all arrays in a yoked fashion
def shuffle(conds,idents,reps,xNum,yNum):

    randExpress = []
    randIdent = []
    randMask = []

    for rep in range(reps):
        ident = identList(idents,conds)
        express = expressList(conds,idents)
        assert len(ident) == len(express), "incompatible stimulus lists"

        randList = range(len(express))
        random.shuffle(randList)

        for entry in randList:

            randExpress.append(express[entry])
            randIdent.append(ident[entry])

            # make array for dynamic mask
            thisMask = range(xNum*yNum)
            random.shuffle(thisMask)
            randMask.append(thisMask)

    d = {'expressions':randExpress,
         'identities':randIdent,
         'masks':randMask}

    assert len(d['expressions']) == len(d['identities']) == len(d['masks']) , "arrays corrupted (different lengths)!"

    return d


#################################

xNum = stimuli.numRow
yNum = stimuli.numCol

conds = 7 # seven basic expressions
idents = 2 # two face identities
reps = 8 # repetitions within a block

blocks = 2 # maximal number of blocks

trials = conds*idents # total number of trials in one block

# trials_per_block is used by other modules!
trials_per_block = trials*reps

#################################

def save_array(what):
    array = files.arrayfile_dir + 'array' + str(session['userid']) + '.txt'
    with open(array, 'wb') as handle:
        pickle.dump(what, handle)

#################################

def makeShuffle():
    return shuffle(conds,idents,reps,xNum,yNum)

#################################
