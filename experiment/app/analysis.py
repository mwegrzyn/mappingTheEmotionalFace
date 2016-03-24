from flask import render_template, request, session
from app import app
import arrays, files, stimuli, shuffle, coursecredit, feedback, codegenerator

# import necessary python libraries
import math
import numpy as np
import random
import datetime

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import seaborn as sns
import pandas as pd

#PIL for image manipulation
import PIL
from PIL import Image
from PIL import ImageDraw


# folder where output is saved to
whereto = 'app/static/feedback/'
# folder where the logfiles are stored
logdir = files.logfile_dir



#####################
# this is the whole analysis mess...


# make a dataframe from the logfile
def makePandas(filename):
    # we load the csv into pandas
    df = pd.read_csv(open(filename,'r'),
                skiprows=6,
                header=0,
                sep='\t')

    # the index in passed into a column, so we do not loose it when reindexing
    df['id'] = df.index
    # we sort the data frame by the values we want to use for the (mulit)index
    df = df.sort('express')
    df = df.sort('ident')
    # we set which variables are the new multi-index
    df = df.set_index(['ident','express','id'],drop=False)
    # we rename the variables because to avoid ambiguity
    df.rename(columns={'ident': 'i', 'express': 'e','id':'#'}, inplace=True)
    ### ugly hack to make index hierarchical
    df = df.unstack(0).stack(1).unstack(0).stack(1).unstack(0).stack(1)

    return df



# get metrics from the dataframe

def getRevealedTable(df,ident,express,dims):
    # df to write to
    bigDf = pd.DataFrame()

    # we go through all items of one specific identity showing one specific expression
    for whichItem in df.ix[ident].ix[express].index:
        # we create a dict with zeroes, one for each possible possition
        d = {}
        for num in range(dims[0]*dims[1]):
            d[num] = 0

        # each time an mask is part of the list of revealed masks, we change
        # its value to one
        try:
            for num in df.ix[ident].ix[express].ix[whichItem]['maskList'].split('-'):
                d[int(num)] = 1
        # for the unlikely case that there is only one number, we cannot split by hyphen
        except:
            #print "only one item in list? better check that !"
            # in that case,there the only number is equal to the whole list
            num = df.ix[ident].ix[express].ix[whichItem]['maskList']
            d[int(num)] = 1

        # for each item, we create a df
        thisDf = pd.DataFrame(d,index=[whichItem])
        # we append to the big df
        try:
            bigDf = pd.concat([bigDf,thisDf])
        except:
            bigDf = thisDf
    return bigDf



def makeProbabTable(participant,df,dims):
    for ident in df.index.levels[0]:
        for express in df.index.levels[1]:
            thisRevealed = getRevealedTable(df,ident,express,dims)
            thisProbab = pd.DataFrame( thisRevealed.mean() ).T
            idx = pd.MultiIndex.from_tuples( [(participant,ident,express)]*len(thisProbab) )
            thisProbab.index = idx
            try:
                bigDf = pd.concat([bigDf,thisProbab])
            except:
                bigDf = thisProbab
    return bigDf


# probabilities for all participants
def makeGroupProbab(fileList,dims):
    # loop through the csv's of all participants
    for thisFile in fileList:
        # get the df of the current participant
        thisDf = makePandas('app/'+thisFile)

        # generate a name for the current participant
        participantNum = thisFile[len('./logfile'):thisFile.rfind('.')]
        participantName = 'p' + ('000' + participantNum)[-3:]

        # get the proabilities
        thisP = makeProbabTable(participantName,thisDf,dims)

        # append to group dataframe
        try:
            bigP = pd.concat([bigP,thisP])
        except:
            bigP = thisP

    return bigP

## visualisation

# make a list of all possible coordinates

def makeCoordinates(xNum,yNum,squareSize):
    myArray = []
    xDim=xNum*squareSize
    yDim=yNum*squareSize
    for x in np.arange(0,xDim,squareSize):
        for y in np.arange(0,yDim,squareSize):
            myArray.append( (x,y) )

    return myArray


# change alpha of certain cutout

def getCut( im, pValue, h, v, squareSize ):

    # cut out a part
    cut = im.crop((h,v,h+squareSize,v+squareSize))
    pixdata=cut.load()

    # change its transparency by looping through all the pixels of the cutout
    for y in xrange(cut.size[1]):
        for x in xrange(cut.size[0]):
            r,g,b,a =  pixdata[x, y]
            #pixdata[x, y] = (r,g,b,int(255*pValue))
            pixdata[x, y] = (int(255*pValue),g,b,a) # alternative visualisation

    return cut


def applyTransparency(im,pDict,dims,squareSize):

    # dimension of the image
    width=dims[1]*squareSize
    height=dims[0]*squareSize
    # make all x,y coordinates for the image
    thisCoord = makeCoordinates(dims[1],dims[0],squareSize)
    # take the original image and convert it, so it has an alpha channel
    im = im.convert("RGBA")
    im = im.resize((width,height), PIL.Image.ANTIALIAS)
    imDim = im.getdata.im_self.size

    pixdata = im.load()

    # create an empty output image to which we will write
    imOut = Image.new("RGBA",
                      imDim,
                      (0,0,0))

    # for each position of a tile and its probability of being shown
    for key,pValue in pDict.iteritems():
        # get the position of the current square
        h,v = thisCoord[key]
        #if pValue !=nan:
        if pValue >= 0: # to exclude nans ...
            # cut that square and apply the proability value
            cut = getCut( im, pValue, h, v, squareSize )
            #cut = getCut( imOut, pValue, h, v, squareSize )
            # add the edited cutout to the output image
            imOut.paste(cut, (h,v))
        else:
            pass
    return imOut





def applyAllTransp(vNum,hNum,squareSize,df,participant,picList):

    # define figure dimensions

    # create a plot
    plt.figure(figsize=(12,4))

    # counter to keep track of subplot position
    axNum = 1

    # loop through the face identities
    for ident in df.index.levels[1]:
        # get the picture sublist for the current identity
        picIdent = picList[ident]

        # loop through all expressions of the current face identity
        for express in df.index.levels[2]:

            #get the picture with the right expression
            picExpress = picIdent[express]
            # load that face
            im = Image.open('app/static/'+picExpress,'r')

            # get the proability values for the current condition and
            # transform them into a dictionary
            thisP = df.ix[participant].ix[ident].ix[express].to_dict()
            #print thisP
            imOut = applyTransparency(im,
                                      thisP,
                                      (hNum,vNum),
                                      squareSize
                                     )
            # show the current image
            ax = plt.subplot(2,7,axNum)
            ax.set_xticks([]);ax.set_yticks([])

            ax.imshow(imOut) # show the current image
            # increase the axis counter by 1
            axNum+=1

    plt.suptitle('Deine Ergebnisse',fontsize=15)

    pltName = feedback.getPltname()
    pltDir = feedback.feedbackDir + pltName

    plt.savefig(pltDir,dpi=300)

    plt.close("all")

    outName = pltDir[pltDir.find('/')+1:]
    return outName


#####
def plotGroupMean(vNum,hNum,squareSize,bigRevealed,picList):

    # group plot

    bigRevealedWithin = bigRevealed.stack().unstack(1).unstack(1).unstack(1)
    bigRevealedWithinAvg = pd.DataFrame( bigRevealedWithin.mean() ).unstack()
    bigRevealedWithinAvg.columns = bigRevealedWithinAvg.columns.droplevel()

    # get the average values from the plot
    bigRevealedWithinAvg = pd.DataFrame( bigRevealedWithin.mean() ).unstack()
    bigRevealedWithinAvg.columns = bigRevealedWithinAvg.columns.droplevel()

    # define figure dimensions
    plt.figure(figsize=(12,4))

    # counter to keep track of subplot position
    axNum = 1

    for ident in bigRevealedWithinAvg.index.levels[0]:
        # get the picture sublist for the current identity
        picIdent = picList[ident]

        # for each expression of the current face identity
        for express in bigRevealedWithinAvg.index.levels[1]:

            #get the picture with the right expression
            picExpress = picIdent[express]
            # load that face
            im = Image.open('app/static/'+picExpress,'r')

            # get the proability values for the current condition and
            # transform them into a dictionary
            thisP = bigRevealedWithinAvg.ix[ident].ix[express].to_dict()

            imOut = applyTransparency(im,
                                      thisP,
                                      (hNum,vNum),
                                      squareSize
                                     )
            # show the current image

            ax = plt.subplot(2,7,axNum)
            ax.set_xticks([]);ax.set_yticks([])
            ax.imshow(imOut)

            axNum+=1

    #show the whole plot
    numParticipants = len(bigRevealed.index.levels[0])
    plt.suptitle('Durchschnittliche Ergebnisse von '+str(numParticipants)+' TeilnehmerInnen',fontsize=15)
    #plt.show()


    pltName = feedback.getPltname()
    pltDir = feedback.feedbackDir + pltName

    plt.savefig(pltDir,dpi=300)

    plt.close("all")

    outName = pltDir[pltDir.find('/')+1:]
    return outName

##################


def makeEverything(logList):

    bigRevealed = makeGroupProbab(logList,(stimuli.numCol,stimuli.numRow))

    outName = plotGroupMean(stimuli.numRow,
                            stimuli.numCol,
                            stimuli.squareSize,
                            bigRevealed,
                            stimuli.stim)

    return outName

#####################
@app.route('/analysis', methods=['POST','GET'])
def analysis():

    # this exits the analysis window and shows the code generated for course credit
    if request.method == 'POST':
        if request.form.get('end_experiment'):
            if session['generated'] == False:
                # generate code for course credit
                session['runs'],session['time'],session['code']= codegenerator.make_code(session['userid'])
                session['generated'] = True
            else:
                # if someone revisists the site, the code stays the same, so you cannot cheat and generate mulitple codes
                pass

            return coursecredit.coursecredit()

    logview = 'static/logfiles/logfile' + str( session['userid'] ) + '.txt'

# this is currently implemented in a bad way and is computationally so expensive,
# that it blocks the whole server (which is bad when there are multiple users at the same time)
    # # this whole thing is wrapped up in one big try/except conditional,
    # # because if anything should go wrong here, we still want the participants to be
    # # able to continute and get their course credit. So this must not break, ever!
    # try:
    #
    #     # we append this logfile to the list of logfiles that consist of finished datasets
    #     # as at this point the participant must have properly finished at least one block,
    #     # the list will only contain proper data that can be used for the group plot
    #     logList = 'app/static/feedback/allFinished.csv'
    #
    #     # append only once (e.g. when some reloads the page, this will prevent multiple appending)
    #     if session['allFinished'] == False:
    #         write_this = open(logList, 'a').write(logview+'\n')
    #         # change the state
    #         session['allFinished'] = True
    #
    #     # get all logs (including the one just added)
    #     logArray = []
    #
    #     for entry in open(logList,'r'):
    #         logArray.append(entry[:-1])# [:-1] to get rid of backspace
    #
    #     #print logArray
    #
    #     # make the participant plot
    #     thisDf = makePandas( files.get_logfile() )
    #     pDf = makeProbabTable( 'dummy', thisDf, (stimuli.numRow,stimuli.numCol) )
    #
    #     singlePlot = applyAllTransp( stimuli.numRow,
    #                                  stimuli.numCol,
    #                                  stimuli.squareSize,
    #                                  pDf,
    #                                  list(pDf.index.levels[0])[-1],
    #                                  stimuli.stim
    #                             )
    #
    #     # make the group plot
    #     groupPlot = makeEverything(logArray)
    #     #print groupPlot
    #
    # # return empty filenames in the event that this doesnt work
    # except:
    #     singlePlot = ''
    #     groupPlot = ''

    # dummys for the time being
    singlePlot = ''
    groupPlot = ''

    # show the html page with the results
    return render_template('analysis.html',
                           singlePlot = singlePlot,
                           groupPlot = groupPlot,
                           this_log  = logview)
