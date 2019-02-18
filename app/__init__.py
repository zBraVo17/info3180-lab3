from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zbravo17'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '' # (was removed)
app.config['MAIL_PASSWORD'] = '' # (was removed)

mail = Mail(app)
from app import views