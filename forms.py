from flask.ext.wtf import Form, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange
from wtforms.fields.html5 import EmailField
 
class ContactForm(Form):
    name = StringField("Name", validators=[InputRequired('Please enter your name.')])
    email = EmailField("Email",  validators=[InputRequired("Please enter your email address."), Email("Please enter your email address.")])
    subject = StringField("Subject", validators=[InputRequired("Please enter the subject.")])
    message = TextAreaField("Message", validators=[InputRequired("Please enter your message.")])
    test = IntegerField("What is four times three?", validators=[NumberRange(12, 12, "Please recalculate.")])
    submit = SubmitField("Send")
