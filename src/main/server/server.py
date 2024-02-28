import os
from flask import Flask
from src.main.routes.http_routes import email_route_bp


path=os.path.dirname(__file__)
# template_folder = os.path.join(path, '..', 'templates')
template_folder = os.path.abspath(os.path.join(path, '..', 'templates'))

app = Flask(__name__, template_folder=template_folder)

# Register Blueprints
app.register_blueprint(blueprint=email_route_bp)
