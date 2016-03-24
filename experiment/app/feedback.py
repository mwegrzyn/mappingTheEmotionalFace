# flask modules
from flask import session

# python modules
import datetime

import math
import numpy as np
import random

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# own modules
import files, stimuli


# where is the output written to
feedbackDir = 'app/static/feedback/'
feedbackFile = 'feedback.csv'

# what is the name of the image file that is being written
def getPltname():
    # to write a new image each time a participant has finished a run,
    # we get the current date and time to use in the image filename
    dateName = ''
    currentDate = str(datetime.datetime.now())
    for e in currentDate:
        if e != ' ':
            if e == ':' or e == '.':
                dateName += '-'
            else:
                dateName += e

    pltName = str(session['userid']) + dateName + '.png'
    return 'fdbck'+pltName


# load the current logfile
def makePandas(filename):
    # we load the csv into pandas
    df = pd.read_csv(open(filename,'r'),
                skiprows=6,
                header=0,
                sep='\t')

    return df


# compute hits
def computeHits(df):
    hits = 0
    count = 0

    for x in list(df['evaluation']):
        if x == 'HIT':
            hits +=1
        count +=1

    percentageHits = (float(hits)/count)*100

    return percentageHits


# compute number of hidden tiles
def computeTiles(df,xNum,yNum):
    tiles=0

    for tile in list(df['maskNum']):
        tiles+=tile
    tileAverage = float(tiles)/len(list(df['maskNum']))

    percentageTiles = 100-(float(tileAverage/(xNum*yNum))*100)
    return percentageTiles


# append to big df
def makeDf(percentageHits,percentageTiles):

### this kind of didnt work (dont know why), so since there already was
#   a logfile there, i commented the case out where the file has to be
#   written anew (this will only be the case for the very first participant).
#   therefore, this works, but only if the file already exists.
#    try:
        # load bigDf from csv
    bigDf = pd.read_csv(feedbackDir+feedbackFile,index_col=0)
    # append the values of the current participant to the big df
    bigDf.ix[str(session['userid'])] = [percentageHits,percentageTiles]


#    except:
#        # make an empty feedback file (this will only be necessary for the first participant)
#        open(feedbackDir+feedbackFile, 'w').write('id,hits,tiles')
#        # load bigDf from csv
#        bigDf = pd.read_csv(feedbackDir+feedbackFile,index_col=0)
#        # append the values of the current participant to the big df
#        bigDf.ix[str(session['userid'])] = [percentageHits,percentageTiles]

    # get the data of everybody but the current participant from the df
    everybodyElse = bigDf.drop( str(session['userid']) )

    # get the data of the current participant from the df (this is somewhat redundant but at least consistent)
    thisParticipant = bigDf.ix[str(session['userid'])]

    # save it as csv (as this is compatible across-platform and can be inspected visually; pickle has proven unreliable (e.g. does not load in anaconda) )
    bigDf.to_csv(feedbackDir+feedbackFile)

    return everybodyElse, thisParticipant


# make a scatter plot with the values of all participant but the current one
# and plot the current participant's value as a point with a marker
def makeScatterPlot(feedbackDir,feedbackFile):
    # get the data of the current participant
    participantDf = makePandas( files.get_logfile() )

    #print participantDf

    percentageHits = computeHits(participantDf)
    percentageTiles = computeTiles(participantDf,stimuli.numRow,stimuli.numCol)

    #get the data by updating the big df
    everybodyElse, thisParticipant = makeDf(percentageHits,percentageTiles)

    # create a plot
    fig = plt.figure(1,figsize=(8,5))
    ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])

    # the data of the present participant
    ax.scatter(percentageTiles,percentageHits, c='r')

    # annotate the current participant's value
    ann = ax.annotate('Dein Ergebnis!', xy=(percentageTiles,percentageHits),
                      xycoords='data', xytext=(35, 0), textcoords='offset points',
                      size=20, va="center",
                      bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec="none"),
                      arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                                      fc=(1.0, 0.7, 0.7),
                                      ec="none",
                                      relpos=(0.2, 0.5),
                                     )
                     )

    # everybody else
    feedbackDf = pd.read_csv(feedbackDir+feedbackFile,index_col=0)

    ax.scatter([y for y in feedbackDf['tiles']] , [x for x in feedbackDf['hits']])


    # plot settings
    ax.set_xlabel('Prozentsatz verdeckter Kacheln')
    ax.set_ylabel('Prozentsatz richtiger Antworten')

    ax.set_title('Zwischenauswertung')

    pltName = getPltname()
    pltDir = feedbackDir + pltName
    plt.savefig(pltDir,dpi=300)
    plt.close("all")

    return pltName


#################################

def plotThis(feedbackDir,feedbackFile):
    try:
        pltName = makeScatterPlot(feedbackDir,feedbackFile)
    except:
        pltName = 'sorry_does_not_work'

    return pltName
