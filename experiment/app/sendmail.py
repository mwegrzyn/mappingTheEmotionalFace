from flask import Flask
app = Flask(__name__)
from flask.ext.mail import Mail, Message

import maildata

# email server
app = Flask(__name__)
app.config.update(dict(
        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT = 587, # 465 if SSL true
        MAIL_USE_TLS = True,
        MAIL_USE_SSL = False,
        MAIL_USERNAME = maildata.username,
        MAIL_PASSWORD = maildata.password
    ))


# administrator list
ADMINS = [maildata.username]

mail = Mail(app)

def send_email(body):
    msg = Message('message from cogut', sender=ADMINS[0], recipients=ADMINS)
    msg.body = ''
    msg.html = body
    mail.send(msg)
