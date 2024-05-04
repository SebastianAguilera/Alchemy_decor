from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.resources import home

db = SQLAlchemy()

def create_app() -> None:
  #se crea una instancia de la aplicacion Flask
  app = Flask(__name__) 
  #Registra el blueprint home en la aplicacion
  app.register_blueprint(home, url_prefix='/api/v1')
  return app

  
