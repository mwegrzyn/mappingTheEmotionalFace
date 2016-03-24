# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import SelectMultipleField, SubmitField, validators, ValidationError, BooleanField, TextField, TextAreaField

##############################################################################################

class ContactForm(Form):
    message = TextAreaField("Vp-Nummer und Code bitte hier eingeben:", [ validators.Required('Code und Vp-Nummer eingeben.') ] )
    submit = SubmitField("Absenden")


##############################################################################################

class InformedConsent(Form):

    major = BooleanField(u"Ich bin 18 Jahre oder älter",  [validators.Required(u'Wenn Du nicht volljährig bist, kannst Du aus rechtlichen Gründen leider nicht an der Studie teilnehmen. Das tut uns leid.')])

    consent = BooleanField(u"Ich habe die Studieninformation verstanden und erkläre mich hiermit bereit, teilzunehmen",  [validators.Required(u'Du musst Deine Zustimmung geben, um an der Studie teilnehmen zu können.')])

    submit = SubmitField("Weiter")

##############################################################################################

class Demographics(Form):

    location = SelectMultipleField("Wie ist Deine aktuelle Arbeitsumgebung?",  [validators.Required(u'Bitte mache Angaben zu Deiner aktuellen Umgebung (oder wähle "keine Angabe")')],
                           choices=[#('0','zu Hause/ruhige Umgebung'),
                                    #('1','unruhige Umgebung'),
                                    ('2','Laborraum'),
                                    #('3','Sonstiges'),
                                    #('99','keine Angabe')
                                    ],
                          )


    age = SelectMultipleField("Alter",
                              [validators.Required(u'Bitte mache Angaben zu Deinem Alter (oder wähle "keine Angabe")')],
                      choices=[ ('18','18'),
                                ('19','19'),
                                ('20','20'),
                                ('21','21'),
                                ('22','22'),
                                ('23','23'),
                                ('24','24'),
                                ('25','25'),
                                ('26','26'),
                                ('27','27'),
                                ('28','28'),
                                ('29','29'),
                                ('30','30'),
                                ('31','31'),
                                ('32','32'),
                                ('33','33'),
                                ('34','34'),
                                ('35','35'),
                                ('36','36'),
                                ('37','37'),
                                ('38','38'),
                                ('39','39'),
                                ('40','40'),
                                ('99','keine Angabe')]
                     )

    gender = SelectMultipleField("Geschlecht",
                                 [validators.Required(u'Bitte mache Angaben zu Deinem Geschlecht (oder wähle "keine Angabe")')],
                         choices=[('0','weiblich'),
                                  ('1',u'männlich'),
                                  ('2','sonstige'),
                                  ('99','keine Angabe')]
                        )

    occupation = SelectMultipleField("Studium/Beruf",
                                     [validators.Required(u'Bitte mache Angaben zu Deinem Studiengang (oder wähle "keine Angabe")')],
                                     choices=[('0','Studium'),
                                              ('1','Ausbildung'),
                                              ('2',u'Berufstätig'),
                                              ('3','Sonstiges'),
                                              ('99','keine Angabe')])

    advertisement = SelectMultipleField("Wie hast Du von der Studie erfahren?",
                                        [validators.Required(u'Bitte mache Angaben dazu, wie Du von der Studie erfahren hast (oder wähle "keine Angabe")')],
                                        choices=[('0','Aushang an der Uni'),
                                                 ('1','Email-Verteiler'),
                                                 ('2','Freunde/Bekannte'),
                                                 ('3','Vorlesung/Seminar'),
                                                 ('4','Surfen im Internet'),
                                                 ('5','Sonstiges'),
                                                 ('99','keine Angabe')])

    #comment = TextAreaField("Sonstige Angaben/Bemerkungen")

    submit = SubmitField("Weiter")
