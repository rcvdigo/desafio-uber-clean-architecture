import os
from flask import Flask
from src.main.routes.http_routes import email_route_bp

# Diretório do projeto
path=os.path.dirname(__file__)

# Diretório dos statics
static_folder = os.path.abspath(os.path.join(path, '../../..', 'static'))

# Diretório dos templates
template_folder = os.path.abspath(os.path.join(path, '..', 'templates'))

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

# Register Blueprints
app.register_blueprint(blueprint=email_route_bp)

# Define a configuração JSON_SORT_KEYS como False
app.config['JSON_SORT_KEYS'] = False