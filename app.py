from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
mi = Migrate()
ma = Marshmallow()

def create_app(config=Config):
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)
  mi.init_app(app, db)
  ma.init_app(db)

  from api import api
  app.register_blueprint(api, url_prefix='/api/')

  return app


app = create_app()

from models import Empleado, Turno

@app.shell_context_processor
def make_shell_context():
  return {'db':db, 'Empleado':Empleado, 'Turno':Turno}
