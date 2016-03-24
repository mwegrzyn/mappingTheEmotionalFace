# main imports

import os
import fnmatch

import numpy as np
import random as rd

import PIL
from PIL import Image
from PIL import ImageDraw

from IPython.display import Image as pyimg 

import pandas as pd
pd.set_option('max_columns', 100)
pd.set_option('max_rows', 1000)

import seaborn as sns
import matplotlib.pyplot as plt

# load image

def getPicList():
    # get the current working dir so we know where to return to later
    thisDir = os.getcwd()
    # go  the the directory with the experiment files
    os.chdir('../experiment/app/')
    # load the array with the stimuli, as used in the experiment
    from stimuli import stim
    # go back to where we are
    os.chdir(thisDir)
    # store a copy of the stimlist as the variable picList
    import copy
    picList = copy.deepcopy(stim)
    
    return picList

def getPics(picList):

    # add the folder prefix
    for i,sub in enumerate(picList):
        for j,entry in enumerate(sub):
            picList[i][j] = '../experiment/app/static/'+entry
    
    # we split it into a female and male array
    picF=picList[0]
    picM=picList[1]
    # we only return the subarrays, as the main array was imported, so no need to return it
    return picF,picM


picList = getPicList()
picF,picM = getPics(picList)

# get logfiles

def getFile(where, what):
    
    # empty array where picture list is stored
    fileList = []
    # for all files in the folder
    for filename in os.listdir(where):
        # whenever the file matches is one of the pictures we search for
        if fnmatch.fnmatch(filename, what):
            # we append to the picture list
            fileList.append(where+filename)
    
    fileList.sort()
    # output the picture list
    return fileList

# get labels for emo expressions

def emoLabels(picList):
    d = {}
    for index,entry in enumerate(picList[-1]):
        thisEmo = entry[entry.find('_')+1:entry.rfind('_')]
        otherEmo = picList[0][index][ picList[0][index].find('_')+1:picList[0][index].rfind('_')]
        assert thisEmo == otherEmo, "emo order does not match for different identities"
        d[index] = thisEmo
    return d


myLabels = emoLabels(picList)


# dict to move from numbers to strings
identDict = {0:'f',1:'m'}
emoDict = {0:'hap',1:'sad',2:'ang',3:'fea',4:'dis',5:'sup',6:'ntr'}

# dict to move from string to number
identReverse = {y:x for x,y in identDict.iteritems()}
emoReverse = {y:x for x,y in emoDict.iteritems()}




# basic plotting function
def interactiveWeights(n):

    fig = plt.figure( figsize=(16,8) )

    ax = plt.subplot(1,1,1)
    ax.imshow(Image.open( thesePics[n]) ) # cave: thesePics is a global variable!
    ax.set_yticks([]); ax.set_xticks([])

    return fig


# some color conversion
#http://stackoverflow.com/a/214657
def rgb2hex(rgb):
    return '#%02x%02x%02x' % rgb

# colors for emos
stackColors = sns.color_palette("Set1", 7)

sns.set_context("talk", font_scale=1.4)
sns.set_style("white")