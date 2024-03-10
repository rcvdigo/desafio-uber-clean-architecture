# pylint: disable=import-error
import json
from flask import Blueprint
from flask import request as request_flask
from flask import render_template
from flask import jsonify


# Import from adapters
from src.main.adapters.request_adapter import request_adapter


# Import from composers
from src.main.composers.send_sns_composer import send_sns_composer
from src.main.composers.send_email_composer import send_email_composer
from src.main.composers.sqs_consumer_composer import sqs_consumer_composer
from src.main.composers.email_sns_sender_composer import send_email_sns_composer


# Import error handler
from src.main.core.exceptions.error_handler import handler_errors


# Import validators
from src.main.validators.email_validator import email_validator


# Import class HttpResponse
from src.main.core.http_response import HttpResponse


# Apelidando o @app para @email_route_bp
email_route_bp = Blueprint("email_routes", __name__)


@email_route_bp.route("/", methods=["GET"])
def index():
    if request_flask.method == 'GET':
        return render_template('form.html')


@email_route_bp.route("/api/email/", methods=["POST"])
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


@email_route_bp.route("/api/email_sns/", methods=["POST"])
def send_email_sns():
    http_response_email = HttpResponse
    http_response_sns = HttpResponse
    http_response = HttpResponse
    is_request_js = request_flask.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if is_request_js:
        try:

            http_response = request_adapter(
                request=request_flask,
                controller=send_email_sns_composer()
            )

        except Exception as exeception:
            http_response = handler_errors(error=exeception)
        return jsonify(http_response.body), http_response.status_code
    
    if not is_request_js:
        try:
            # Protegendo a inserção de dados injetando o validator email_validator
            # email_validator(request=request_flask)

            http_response_email = request_adapter(
                request=request_flask,
                controller=send_email_composer()
            )

            http_response_sns = request_adapter(
                request=request_flask,
                controller=send_sns_composer()
            )

            if http_response_email.status_code == 200 and http_response_sns.status_code == 200:

                http_response = HttpResponse(
                    status_code=200,
                    body={
                        'email_response': http_response_email.body,
                        'sns_response': http_response_sns.body
                    }
                )
        except Exception as exeception:
            http_response = handler_errors(error=exeception)
        return jsonify(http_response.body), http_response.status_code


@email_route_bp.route("/consumer/", methods=["GET"])
def consumer():
    try:    
        http_response_sqs = HttpResponse(
            body=sqs_consumer_composer(),
            status_code=200
        )
    except Exception as exeception:
        http_response_sqs = handler_errors(error=exeception)
    if 'text/html' in request_flask.headers.get('Accept'):
        return render_template(
            'consumer.html',
            messages=http_response_sqs.body,
            status=http_response_sqs.status_code
            )
    else:
        return jsonify(http_response_sqs.body), http_response_sqs.status_code
