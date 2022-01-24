import os
from dotenv import load_dotenv

load_dotenv(".env")

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER ='smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'b9a02efbbffd55'
    MAIL_PASSWORD = '7620e88d22059b'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/feedback'

class ProdConfig(Config):
    DATABASE_URI = f''