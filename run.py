import os
from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()

app = Flask(__name__)

app.secret_key = 'h@t3m0ng5TQ_'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'myopicjazz@gmail.com'
app.config["MAIL_PASSWORD"] = 'dsokuyzpcqmaqskz'

SECURITY_EMAIL_SENDER = 'myopicjazz@gmail.com'

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6Lcr9QgTAAAAADljN1lLogj0ijs4DqNq2OmG-tPP'
RECAPTCHA_PRIVATE_KEY = '6Lcr9QgTAAAAADjOzzijXkIh5HapfrBU4sxSsku2'
RECAPTCHA_OPTIONS = {'theme': 'white'}

mail.init_app(app)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/recollections/')
def recollections():
    return render_template('recollections.html')

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')

@app.route('/vintage/')
def vintage():
    return render_template('vintage.html')

@app.route('/reunion2010/')
def reunion2010():
    return render_template('reunion2010.html')

@app.route('/reunion2012/')
def reunion2012():
    return render_template('reunion2012.html')

@app.route('/tulsa2013/')
def tulsa2013():
    return render_template('tulsa2013.html')

@app.route('/reunion2014/')
def reunion2014():
    return render_template('reunion2014.html')

@app.route('/springdale2015/')
def springdale2015():
    return render_template('springdale2015.html')

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
 
    if request.method == 'POST':
        if form.validate() == False:
          flash('All fields are required.')
          return render_template('contact.html', form=form)
    if form.validate_on_submit():
        msg = Message(form.subject.data, sender='contact@bsureunion.com', recipients=['myopicjazz@gmail.com'])
        msg.body = """
        From: %s <%s>
        %s
        """ % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)
        
        return render_template('contact.html', success=True)
 
    elif request.method == 'GET':
      return render_template('contact.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(410)
def page_not_found(e):
    return render_template('410.html'), 410

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()