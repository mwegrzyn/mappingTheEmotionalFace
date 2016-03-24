# basic flask modules
from flask import request,session

# timing modules
import time, datetime

import numpy as np
# own modules
import files, stimuli, shuffle, arrays, analysis



# big CAVE: if you dont index from the end (with negative numbers, this will be totally meaningless!)
def track_response(n):
    assert n < 0 , 'when tracking responses, index from the end (because we shorten them!)'
    # get the response made
    if session['thisAns'] == 'hap':
        session['button'] = 'hap'
    elif session['thisAns'] == 'sad':
        session['button'] = 'sad'
    elif session['thisAns'] == 'ang':
        session['button'] = 'ang'
    elif session['thisAns'] == 'fea':
        session['button'] = 'fea'
    elif session['thisAns'] == 'dis':
        session['button'] = 'dis'
    elif session['thisAns'] == 'sup':
        session['button'] = 'sup'
    elif session['thisAns'] == 'ntr':
        session['button'] = 'ntr'
    else:
        session['button'] = 'miss'

    # check if the response is correct
    if session['button'] == 'hap':
        session['tracker'][n]['button'] = 'hap'
        if session['tracker'][n]['express'] == 0:
            session['tracker'][n]['evaluation'] = 'HIT'
        else:
            session['tracker'][n]['evaluation'] = 'ERR'
    elif session['button'] == 'sad':
        session['tracker'][n]['button'] = 'sad'
        if session['tracker'][n]['express'] == 1:
            session['tracker'][n]['evaluation'] = 'HIT'
        else:
            session['tracker'][n]['evaluation'] = 'ERR'
    elif session['button'] == 'ang':
        session['tracker'][n]['button'] = 'ang'
        if session['tracker'][n]['express'] == 2:
            session['tracker'][n]['evaluation'] = 'HIT'
        else:
            session['tracker'][n]['evaluation'] = 'ERR'
    elif session['button'] == 'fea':
        session['tracker'][n]['button'] = 'fea'
        if session['tracker'][n]['express'] == 3:
            session['tracker'][n]['evaluation'] = 'HIT'
        else:
            session['tracker'][n]['evaluation'] = 'ERR'
    elif session['button'] == 'dis':
        session['tracker'][n]['button'] = 'dis'
        if session['tracker'][n]['express'] == 4:
            session['tracker'][n]['evaluation'] = 'HIT'
        else:
            session['tracker'][n]['evaluation'] = 'ERR'
    elif session['button'] == 'sup':
        session['tracker'][n]['button'] = 'sup'
        if session['tracker'][n]['express'] == 5:
            session['tracker'][n]['evaluation'] = 'HIT'
        else:
            session['tracker'][n]['evaluation'] = 'ERR'
    elif session['button'] == 'ntr':
        session['tracker'][n]['button'] = 'ntr'
        if session['tracker'][n]['express'] == 6:
            session['tracker'][n]['evaluation'] = 'HIT'
        else:
            session['tracker'][n]['evaluation'] = 'ERR'

    elif session['button'] == 'miss':
        session['tracker'][n]['button'] = 'miss'
        session['tracker'][n]['evaluation'] = 'MISS'

    # cumulated time of trial: start of trial minus start of experiment
    cumul_time = round((session['timing'][-2]-session['timing'][0]),5)
    session['tracker'][n]['cumtime'] = cumul_time

    this_logfile = files.get_logfile()
    write_this = open(this_logfile, 'a').write(
        str(session['tracker'][n]['time'])+'\t'+ # real time of day
        str(session['tracker'][n]['cumtime'])+'\t'+ # cumulative experiment time
        str(session['tracker'][n]['express'])+'\t'+ # condition
        str(session['tracker'][n]['ident'])+'\t'+ # pairing
        session['thisAns']+'\t'+
        str(session['tracker'][n]['filenames'])+'\t'+ # name of files
        str(session['tracker'][n]['evaluation'])+'\t'+ # evaluation of response
        str(session['stopRT'])+'\t'+
        str(session['choiceRT'])+'\t'+
        session['maskr']+'\t'+ # number of masks revealed
        session['bigstr'][1:]+'\n' # indices of masks revealed
    )
