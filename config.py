import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'K\xdf\xb4\xd0J\x91\xb9\xdc?^\xfce\x04\xfaX['

    MONGODB_SETTINGS = {'db': 'UTA-Enrollment'}