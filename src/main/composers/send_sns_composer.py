import os


from src.main.infra.sns.sns_sender import SnsSender
from src.main.application.sns_sender_service import SnsService
from src.main.controllers.sns_sender_controller import SenderController


def send_sns_composer():
    sns_gateway = SnsSender(
        service_name=os.getenv('SNS'),
        region_name=os.getenv('REGIAO'),
        access_key=os.getenv('CHAVE_ACESSO'),
        secret_key=os.getenv('CHAVE_SECRETA')
        )
    email_sender_service = SnsService(sns_gateway=sns_gateway)
    controller = SenderController(use_case=email_sender_service)

    return controller.handle
