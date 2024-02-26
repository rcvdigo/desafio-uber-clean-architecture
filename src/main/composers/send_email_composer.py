import os


from src.main.infra.ses.ses_email_sender import SesEmailSender
from src.main.application.email_sender_service import EmailSenderService
from src.main.controllers.email_sender_controller import SenderController


def send_email_composer():
    email_sender_gateway = SesEmailSender(
        service_name=os.getenv('SES'),
        region_name=os.getenv('REGIAO'),
        access_key=os.getenv('CHAVE_ACESSO'),
        secret_key=os.getenv('CHAVE_SECRETA')
        )
    email_sender_service = EmailSenderService(email_gateway=email_sender_gateway)
    controller = SenderController(use_case=email_sender_service)

    return controller.handle
