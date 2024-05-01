from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app() -> None:
  #se crea una instancia de la aplicacion Flask
  app = Flask(__name__) 
  from app.resources import home
  #Registra el blueprint home en la aplicacion
  app.register_blueprint(home, url_prefix='/api/v1')
  return app

  
