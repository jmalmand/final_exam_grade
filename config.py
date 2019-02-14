import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "a77429ef7b1d9036f82e246df921edea"
    DEBUG = True
    TESTING = True
    ENV = False
