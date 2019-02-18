from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
    name= TextField('Name', [validators.Required("(Required)")])
    email= TextField('E-mail', [validators.Required("(Required)")])
    subject= TextField('Subject', [validators.Required("(Required)")])
    message= TextAreaField('Message', [validators.Required("(Required)")])
    