from flask import Flask
from flask_marshmallow import Marshmallow
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from app.route import RouteApp

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app() -> None:
    app_context = os.getenv('FLASK_CONTEXT')
    
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    route = RouteApp()
    route.init_app(app)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
     
    @app.shell_context_processor
    def ctx():
        return {"app": app}
    
    return app
