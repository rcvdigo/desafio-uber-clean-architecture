from flask import Flask
from src.main.routes.http_routes import email_route_bp


app = Flask(__name__)

# Register Blueprints
app.register_blueprint(blueprint=email_route_bp)
