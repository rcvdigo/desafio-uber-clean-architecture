# pylint: disable=import-error
from flask import Blueprint
from flask import request as request_flask
from flask import jsonify

# Import from adapters
from src.main.adapters.request_adapter import request_adapter

# Import from composers
from src.main.composers.send_email_composer import send_email_composer

# Import error handler
from src.main.core.exceptions.error_handler import handler_errors

# Import validators
from src.main.validators.email_validator import email_validator


# Apelidando o @app para @email_route_bp
email_route_bp = Blueprint("email_routes", __name__)

@email_route_bp.route("/api/email", methods=["POST"])
def send_email():
    http_response = None

    try:
        # Protegendo a inserção de dados injetando o validator email_validator
        email_validator(request=request_flask)

        http_response = request_adapter(
            request=request_flask,
            controller=send_email_composer()
        )

    except Exception as exeception:
        http_response = handler_errors(error=exeception)

    return jsonify(http_response.body), http_response.status_code
