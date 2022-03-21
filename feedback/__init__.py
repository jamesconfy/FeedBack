from flask import Flask
from config import ProdConfig
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

mail = Mail()
db = SQLAlchemy()

def create_app():
    app = Flask("feedback")
    app.config.from_object(ProdConfig)
    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from feedback import routes
        db.create_all()

    return app