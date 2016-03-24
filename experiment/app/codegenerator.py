# COLLECTION OF FUNCTIONS FOR GENERATING INDIVIDUAL CODES

# importing libraries
import random
import sys
import csv
import math
import numpy as np
import random
import pandas as pd

# own modules
import files

# get the code from the table and delete it
def get_and_delete(csv_file,j):
    # read the csv into a pandas dataframe
    df = pd.DataFrame.from_csv(csv_file)
    # get the code form the last row of the df and from column j
    your_code = df.ix[len(df.index)-1][j]
    # transform the df back to a csv, but omit the last row
    csv = pd.DataFrame.to_csv(df[:-1],csv_file)
    # return the code for this participant
    return your_code

# get the current participant
def getsubject(whichfolder, whichnumber):
    filename = whichfolder + 'logfile' + str(whichnumber) + '.txt'
    return filename

# get the time of all runs and add it up
def get_time(whichfolder,whichnumber):
    # get the participant's logfile
    filename = whichfolder + 'logfile' + str(whichnumber) + '.txt'
    this_file = open(filename,'r')
    # two lists where times are saved
    run_times = []
    cum_times = []
    # get the cumulated time out of each row
    for entry in this_file:
        if 'img' in entry:
            run_times.append(entry.split()[2])
        # when the current time is lower than the time before that,
        # it means that a new block must have started, so we append
        # the cumulated time of the last block
        try:
            if float(run_times[-1]) < float(run_times[-2]):
                cum_times.append(float(run_times[-2]))
        # at the beginning, there may not be an entry at -2,
        # so we use try/except here
        except:
            pass
    # we also need to append the very last time (of the last run)
    cum_times.append(float(run_times[-1]))
    # we return the time of all runs as a sum and the number of runs
    return sum(cum_times), len(cum_times)


# blur the time taken into 10-minute bins
def get_timebin(cum_time):
    # we make a list with time bins, a bin each ten minutes (=600sec)
    # it is reasonable to assume that no experiment will ever last
    # longer than three hours (3*6*600), so we can keep that value fixed
    time_bins= range(0,3600*3,600)
    # go through the list of 10-minute bins
    for entry in time_bins:
        # if the time the participant took is smaller than that bin...
        if cum_time < entry:
            # ...we return that time bin. That is, we return the first
            # bin that is larger then the time the participant actually took
            return int(entry/60)

# generate the code by taking the unique number from the list
# and the time taken. then transform the time into hex (to obscure it)
# and ouput the (human readable) time and number of runs as well as the
# CODE which the participants need to send via mail
def make_code(n):
    # get the time taken, in 10 Minuntes resolution
    file_folder = 'app/static/logfiles/'
    file_list = getsubject(file_folder,n)
    # the time bin of the participant is converted to hexadecimal,
    # so it is less obvious where the time taken is stored in the code
    real_time, runs = get_time(file_folder,n)
    bin_time = hex( get_timebin(real_time) )

    # get the unique code that ascertains that the participant
    # actually performed the experiment and which run she did reach
    csv = 'app/static/codes/codes.txt'
    this_code = get_and_delete(csv,runs-1)

    # the final code is a combination of both
    final_code = str(this_code) + str(bin_time)
    # we return the number of runs, the time (as integer), and the final code
    return runs, int(bin_time,16), final_code
