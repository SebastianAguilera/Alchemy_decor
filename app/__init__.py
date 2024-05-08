from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from app.config import config
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app() -> None:

  #Using an Application Factory

  app_context = os.getenv('FLASK_CONTEXT')

  #se crea una instancia de la aplicacion Flask
  app = Flask(__name__) 

  f = config.factory(app_context if app_context else 'development')
  app.config.from_object(f)
  f.init_app(app)
  db.init_app(app)
  ma.init_app(app)
  migrate.init_app(app, db)

  #Registra el blueprint 
  from app.resources import home, user
  app.register_blueprint(home, url_prefix='/api/v1')
  app.register_blueprint(user, url_prefix='/api/v1/user')

  @app.shell_context_processor    
  def ctx():
    return {
      "app": app,
      'db' : db
      }
  

  return app

  
