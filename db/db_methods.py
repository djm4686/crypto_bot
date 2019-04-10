from sqlalchemy import create_engine
from os.path import abspath, dirname

def _get_dir():
    return dirname(abspath(__file__))

def get_engine(db_name):
    return create_engine('sqlite:////{}/{}.db'.format(_get_dir(), db_name))
