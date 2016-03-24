import random
import pickle

import sys
import csv

import datetime

# each trial in the tracker list is represented by a dict that carries all important
# information. This function creates such a dict each time a new trial occurs
def make_entry():
    d = {
        'time':{},
        'cumtime':{},
        'express':{},
        'ident':{},
        'button':{},
        'filenames':{},
        'evaluation':{}
    }
    return d
