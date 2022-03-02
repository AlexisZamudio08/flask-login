#This is a config file taken by the flask main app.
from distutils.debug import DEBUG

from gevent import config

#This key is used to encrypt the session data is needed.
class Config:
    SECRET_KEY = 'create_here_your_secret_key'

#This parameter is used to reach database connection.
class DevelopmentConfig(Config):
    db_user = 'your_user'
    db_password = 'your_password'
    DEBUG=True
    MYSQL_DATABASE_HOST ='localhost'
    MYSQL_DATABASE_USER = db_user
    MYSQL_DATABASE_PASSWORD = db_password
    MYSQL_DATABASE_DB ='dbo'

config = {
    'development': DevelopmentConfig
}
