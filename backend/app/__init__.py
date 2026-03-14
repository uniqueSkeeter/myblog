from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    from app.routes.articles import bp as articles_bp
    from app.routes.categories import bp as categories_bp
    from app.routes.tags import bp as tags_bp

    app.register_blueprint(articles_bp, url_prefix='/api')
    app.register_blueprint(categories_bp, url_prefix='/api')
    app.register_blueprint(tags_bp, url_prefix='/api')

    return app

from app import models
