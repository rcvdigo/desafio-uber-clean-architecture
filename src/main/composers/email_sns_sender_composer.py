import os


from src.main.infra.sns.sns_sender import SnsSender
from src.main.infra.ses.ses_email_sender import SesEmailSender
from src.main.application.sns_sender_service import SnsService
from src.main.application.email_sender_service import EmailSenderService
from src.main.controllers.email_sns_sender_controller import EmailSnsSenderController


def send_email_sns_composer():

    sns_gateway = SnsSender(
        service_name=os.getenv('SNS'),
        region_name=os.getenv('REGIAO'),
        access_key=os.getenv('CHAVE_ACESSO'),
        secret_key=os.getenv('CHAVE_SECRETA')
        )
    
    ses_gatway = SesEmailSender(
        service_name=os.getenv('SES'),
        region_name=os.getenv('REGIAO'),
        access_key=os.getenv('CHAVE_ACESSO'),
        secret_key=os.getenv('CHAVE_SECRETA')
    )

    sns_sender_service = SnsService(sns_gateway=sns_gateway)
    email_sender_service = EmailSenderService(email_gateway=ses_gatway)
    
    use_cases = {
                    'sns': sns_sender_service,
                    'email': email_sender_service
                }
    controller = EmailSnsSenderController(use_case=use_cases)

    return controller.handle
