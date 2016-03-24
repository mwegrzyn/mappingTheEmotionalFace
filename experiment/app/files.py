# COLLECTION OF FUNCTIONS FOR FILE MANAGEMENT
# allowing to create, write, open and edit different textfiles
# containing logfiles, array information etc.

# importing libraries
from flask import session
import random
import pickle
import sys
import csv
import datetime


# defining folders where logfiles are written and global counters for the exeriment are stored

logfile_dir = 'app/static/logfiles/'
arrayfile_dir = 'app/static/arrays/'
countfile_dir = 'app/static/counter/'

def get_logfile():
    this_logfile= logfile_dir + 'logfile' + str(session['userid']) + '.txt'
    return this_logfile

def make_log(logname):
    write_this = open(logname, 'w').write(
        '####### THIS IS A LOGFILE FOR THE DYNAMIC MASKING FACE EXPERIMENT ######'+
        '\nParticipant Number: ' + str(session['userid']) +
        '\nDate and Time: '+str(datetime.datetime.now())
    )

def make_csv(csv_filename,csv):
    write_this = open(csv_filename, 'w').write(csv)

def add_participant():
    # get file where participant number is stored
    filename = countfile_dir + 'participants.txt'
    participants = open(filename,'r')
    # get the number out of the file
    for entry in participants:
        participants_list = entry
    # increment that number by one
    participants_list = str(int(participants_list) + 1 )
    # write the new number into that file
    write_this = open(filename,'w').write(participants_list)
    # make a logfile where the new number is appended to the file name
    logfile_name = get_logfile()
    # create heading in the new logfile
    make_log(logfile_name)

def get_participant():
    filename = countfile_dir + 'participants.txt'
    participants = open(filename,'r')
    for entry in participants:
        return int(entry)


#################################################################################

def save_this(what):
    data_dir = logfile_dir + 'data.txt'
    with open(data_dir, 'wb') as handle:
        pickle.dump(what, handle)

def load_this(what):
    with open(what, 'rb') as handle:
        thisdata = pickle.loads(handle.read())
    return thisdata

def get_array():
    array = arrayfile_dir + 'array' + str(session['userid']) + '.txt'
    return array
