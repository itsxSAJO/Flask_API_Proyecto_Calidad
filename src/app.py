from flask import Flask
from flask_cors import CORS

from config import config

# Routes
from routes import Terapeuta
from routes import Paciente
from routes import Sesion
from routes import Autenticacion

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


def page_not_found(e):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    # Blueprints
    app.register_blueprint(Terapeuta.main, url_prefix='/api/terapeuta')
    app.register_blueprint(Paciente.main, url_prefix='/api/paciente')
    app.register_blueprint(Sesion.main, url_prefix='/api/sesion')
    app.register_blueprint(Autenticacion.main, url_prefix='/api/auth')
    
    # Error handler
    app.register_error_handler(404, page_not_found)
    app.run()
