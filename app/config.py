class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/test1'
    SECRET_KEY = 'sefsef es fef wefwegwrg rgwfwefwegwrgergeth'
    SECURITY_PASSWORD_SALT = 'aergaergaergerg'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
