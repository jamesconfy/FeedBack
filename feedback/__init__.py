from flask import Flask
from config import Config
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)
db = SQLAlchemy(app)

from feedback import routes