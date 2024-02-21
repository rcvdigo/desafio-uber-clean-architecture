from flask import Blueprint, jsonify, request


from src.main.core.email_request import EmailRequest
from src.main.infra.ses.ses_email_sender import SesEmailSender
from src.main.application.email_sender_service import EmailSenderService
from src.main.controllers.email_sender_controller import EmailSenderController


email_sender_gateway = SesEmailSender(amazon_simple_email_service='ses')
email_sender_service = EmailSenderService(email_gateway=email_sender_gateway)
email_sender_controller = EmailSenderController(email_sender_service=email_sender_service)

user_route_bp = Blueprint("user_routes", __name__) # Apelidando o @app para @user_route_bp

@user_route_bp.route("/api/email", methods=["POST"])
def send_email():
    try:
        email_data = request.json
        email_request = EmailRequest(email_data['to'], email_data['subject'], email_data['body'])
        response, status_code = email_sender_controller.send_email(email_request)
        return jsonify(response), status_code
    except KeyError as e:
        return jsonify({'message': 'Invalid request data.', 'cause': str(e)}), 400
    except Exception as e:
        return jsonify({'message': 'Internal server error.', 'cause': str(e)}), 500
