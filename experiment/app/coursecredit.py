# basic flask modules
from flask import render_template, session, request, flash


from app import app

# file operation modules
import sys, csv

# own modules
import codegenerator, sendmail
from forms import ContactForm


@app.route('/coursecredit', methods=['POST','GET'])
def coursecredit():
    # in the file codegenerator are the functions to make a code
    # by using information in the logfile of the current participant
    # we get the number of  runs, the (rounded) time taken and the
    # resulting code

    # send a mail with the code and the participant's code
    form = ContactForm()
    success = False
    if request.method == 'POST':
        if form.validate():
            sendmail.send_email(form.message.data)
            success = 'Deine Nachricht wurde verschickt. Vielen Dank.'
    # we return the site and tell the participant how long she took,
    # how many trials she completed and what her code is
    return render_template('coursecredit.html',
                           runs = session['runs'],
                           time = session['time'],
                           code = session['code'],
                           form = form,
                           success = success)
