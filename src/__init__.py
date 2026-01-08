from flask import Flask

from src.settings.config import Config
from src.settings.extensions import db, migrate, ma

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    # Inicialização das exterções
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    
    # Registrado models
    from src.models.contato_model import Contato
    
    # Registrar as rotas
    from src.routes.contatos_routes import contatos_bp
    app.register_blueprint(contatos_bp)
    
    
    return app