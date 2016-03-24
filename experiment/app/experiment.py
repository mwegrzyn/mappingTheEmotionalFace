# basic flask modules
from flask import render_template, request, session, jsonify
from app import app

# file operation modules
import sys, csv

# timing modules
import time, datetime

# own modules
import files, stimuli, shuffle, arrays, analysis, logwrite, feedback


@app.route('/stopEcho/', methods=['GET'])
def stopEcho():
    countData = {"value": request.args.get('countValue')}
    bigData = {"value": request.args.get('bigValue')}
    stopData = {"value": request.args.get('stopValue')}

    session['maskr'] = countData['value']
    session['bigstr'] = str(bigData['value'])
    session['stopRT'] = float(stopData['value'])


    # for debugging:
    #print 'stop',session['stopRT']
    #print "-x-x-",session['maskr']
    #print "-y-y-",session['bigstr']
    #print "-z-z-",session['rt_js']
    return jsonify(countData)

@app.route('/choiceEcho/', methods=['GET'])
def choiceEcho():
    choiceData = {"value": request.args.get('choiceValue')}
    session['choiceRT'] = float(choiceData['value'])

    thisAns = {"value": request.args.get('ansValue')}
    session['thisAns'] = thisAns['value']

    #print 'choice',session['choiceRT']
    return jsonify(choiceData)


@app.route('/experiment', methods=['POST','GET'])

def experiment():

    if request.method == 'POST':

        # get the current value of i
        i = session['i']
        j = session['j']
        # for debugging:
        #print "i: ", i, " j: ", j

        # end experiment and show results if aborted

        if request.form.get('end') or j >= shuffle.blocks: #<<<
            return analysis.analysis()
        if request.form.get('quit'):
            #print "experiment stopped. exit to DOS..."
            return analysis.analysis()
        if request.form.get('abort'):
            #print "experiment aborted. exit to DOS..."
            return analysis.analysis()
        if request.form.get('resume'):
            #print "here we go!"

            # a new array is generated (not nice: the old one is overwritten)
            shuffle.save_array( shuffle.makeShuffle() )

            session['tracker'] = []
            session['timing'] = []

            # count a new block
            session['j'] +=1
            # reset i
            session['i'] = 0

            ###
            i = session['i']
            j = session['j']
            #print "this is the resume status:  i: ", i, " j: ", j


            # end experiment and show results if aborted
            j = session['j']
            if j >= shuffle.blocks: #<<<
                return analysis.analysis()

        # get the array generated for this participant
        array_name = files.get_array()
        this_array = files.load_this(array_name)

        # timing logging
        session['timing'].append( time.time() )
        real_time = str( datetime.datetime.now() )
        real_time = real_time[:real_time.find('.')]


        # if the experiment has not started yet (i=-1), we set it up
        if i < 0:
            # count up -- this will make i == 0 and the next trial will be a real trial
            session['i'] +=1

            # empty the tracker for the new participant

            session['tracker'] = []
            session['timing'] = []

            #print "--- ES GEHT LOS! ---" # for debugging
            # show the starting screen
            return render_template('experiment.html',
                                   i=i,
                                   length=shuffle.trials_per_block )



        # if the experiment has started
        if i >= 0 and i < shuffle.trials_per_block:

            # get the data for the next trial (which will be rendered subsequently)
            express = this_array['expressions'][i]
            ident = this_array['identities'][i]
            mask = this_array['masks'][i]
            # since we will be popping from the mask list in js, we invert it
            mask = mask[::-1]

            # get the stimulus for the next trial
            img = stimuli.stim[ident][express]

            # the array tracking the experiment progression gets a new entry
            # which is a dict containing all properties
            session['tracker'].append(arrays.make_entry())

            # the data of the next trial are appended to the end of the tracker;
            # they can be accessed later
            session['tracker'][-1]['express'] =  express
            session['tracker'][-1]['ident'] = ident
            session['tracker'][-1]['filenames'] = img
            session['tracker'][-1]['time'] = real_time

        # as long as the counter does not exceed the number of trials,
        # run the experiment !
        if i >= 1 and i < shuffle.trials_per_block:
            logwrite.track_response(-2)

            # prevent session tracker from becoming too large (this is an issue because cookies cant exceed 4kb...)
            if len(session['tracker']) > 3:
                del session['tracker'][0]

        # if the run is over
        if i == shuffle.trials_per_block:
            logwrite.track_response(-1)

            # make a plot
            pltname = feedback.plotThis(feedback.feedbackDir,feedback.feedbackFile)

            # the page gets returned, but without stimuli
            return render_template('experiment.html',

                                   i = shuffle.trials_per_block,
                                   j = j,
                                   blocks = (shuffle.blocks-1),
                                   length=shuffle.trials_per_block,
                                   pltname = 'static/feedback/'+pltname

                                  )


        # we increase the counter by one
        session['i'] +=1

        # the page with stimuli and everything gets returned
        # if the experiment is ongoing (i>0 and <length)
        return render_template('experiment.html',
                                # trial tracking
                                i = i,
                                length=shuffle.trials_per_block,
                                # presentation properties
                                squareSize = stimuli.squareSize,
                                waitTime = stimuli.waitTime,
                                numRow = stimuli.numRow,
                                numCol = stimuli.numCol,
                                isi = stimuli.isi,
                                # trial properties
                                express = express,
                                mask = mask,
                                img = img
                              )
