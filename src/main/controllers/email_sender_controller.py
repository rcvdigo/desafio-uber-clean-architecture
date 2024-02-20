from flask import jsonify
from src.main.core.email_request import EmailRequest
from src.main.application.email_sender_service import EmailSenderService
from src.main.core.exceptions.email_service_exception import EmailServiceException


class EmailSenderController():

    def __init__(self, email_sender_service: EmailSenderService) -> None:
        self.__email_sender_service = email_sender_service

    def send_email(self, email_request: EmailRequest):
        try:
            self.__email_sender_service.send_email(
                email_request.to, email_request.subject, email_request.body)
            return jsonify({'message': 'Email sent successfully!'}), 200
        except EmailServiceException as ex:
            return jsonify({'message': 'Email sending failed.', 'cause': ex}), 500
