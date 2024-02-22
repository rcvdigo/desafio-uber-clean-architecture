import os


from dotenv import load_dotenv


from src.main.infra.ses.ses_email_sender import SesEmailSender
from src.main.application.email_sender_service import EmailSenderService
from src.main.controllers.sender_controller import SenderController


def send_email_composer():
    email_sender_gateway = SesEmailSender(
        service_name=os.getenv('NOME_DO_SERVICO'),
        region_name=os.getenv('REGIAO'),
        access_key=os.getenv('CHAVE_ACESSO'),
        secret_key=os.getenv('CHAVE_SECRETA')
        )
    email_sender_service = EmailSenderService(email_gateway=email_sender_gateway)
    controller = SenderController(use_case=email_sender_service)

    return controller.handle
