import os
from dotenv import load_dotenv

load_dotenv(".env")

MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASS = os.environ.get('MYSQL_PASS')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_PORT = os.environ.get('MYSQL_PORT')

class DevConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER ='smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'b9a02efbbffd55'
    MAIL_PASSWORD = '7620e88d22059b'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(DevConfig):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'