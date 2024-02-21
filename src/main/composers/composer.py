from src.main.infra.ses.ses_email_sender import SesEmailSender
from src.main.application.email_sender_service import EmailSenderService
from src.main.controllers.email_sender_controller import EmailSenderController


def composer():
    email_sender_gateway = SesEmailSender(amazon_simple_email_service='ses')
    email_sender_service = EmailSenderService(email_gateway=email_sender_gateway)
    email_sender_controller = EmailSenderController(email_sender_service=email_sender_service)

    return email_sender_controller.send_email
