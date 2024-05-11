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
    app_context = os.getenv('FLASK_CONTEXT')
    
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.resources import home
    app.register_blueprint(home, url_prefix='/api/v1')
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app


