# basic flask modules
from flask import render_template, request, session, flash, jsonify
from app import app

# file operation modules
import sys, csv, os

# timing modules
import time, datetime

# own modules
import files, stimuli, shuffle, arrays, analysis, experiment
from forms import InformedConsent, Demographics, ContactForm

app.secret_key = os.urandom(24)

@app.route('/instruction', methods=['POST','GET'])

def instruction():

    ###
    session['tracker'] = []
    session['timing'] = []
    session['button'] = 'dummy'
    session['thisAns']  = 'dummy'
    
    # set the counting variables for this participant
    session['userid'] = files.get_participant()
    session['i'] = -1
    session['j'] = 0
    # this makes sure that people don't generate multiple logfiles by going back
    session['generated'] = False
    # this makes sure that a logfile is only added once to the loglist for online analysis
    session['allFinished'] = False

    #print ">>> sess >>>", session["userid"]
    #print ">>> fin >>>", session["allFinished"]

    # create the form object
    form = InformedConsent()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required')
            return render_template('instruction.html',form=form)

        #print '--> major',request.form['major']
        #print '--> consent',request.form['consent']

        # increment participant number in txt file
        # for the first participant this means an increment from zero to one
        files.add_participant()
        # make an array with condition orders for this participant
        shuffle.save_array( shuffle.makeShuffle() )
        # make an empty logfile for this participant
        this_logfile = files.get_logfile()
        return render_template('demographics.html',form=Demographics())

    # if the button is not pressed that means that the page is loaded initally
    return render_template('instruction.html',form=form)

#############################################################################

@app.route('/demographics', methods=['GET','POST'])

def demographics():

    form = Demographics()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required')
            return render_template('demographics.html',form=form)

        this_logfile = files.get_logfile()
        write_this = open(this_logfile, 'a').write(
            '\nage: '+request.form['age']+
            ' ,gender: '+request.form['gender']+
            ' ,environ: '+request.form['location']+
            ' ,occup: '+request.form['occupation']+
            ' ,advert: '+request.form['advertisement']+
            '\n###################################################################\n'+
            '\ntime\tcumtime\texpress\tident\tbutton\tfilename\tevaluation\tstopRT\tchoiceRT\tmaskNum\tmaskList\n'
         )

        return experiment.experiment()

    elif request.method == 'GET':
        return render_template('demographics.html', form=form)

###########################################################################

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    return render_template('index.html')

############################################################################

@app.route('/impressum', methods=['POST','GET'])
def impressum():
    return render_template('impressum.html')


############################################################################


@app.route('/pub', methods=['POST','GET'])
def pub():
    return render_template('pub.html')
