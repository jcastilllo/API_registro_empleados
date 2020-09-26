from os import path,environ
basedir = path.abspath(path.dirname(__file__))

class Config():
  SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or \
      'sqlite:///' + path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
