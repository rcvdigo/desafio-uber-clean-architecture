#pylint: disable = raise-missing-from
# Imports AWS services
import boto3 as AmazonSimpleEmailService

# Imports Interfaces Adapters
from src.main.adapters.email_sender_gateway import EmailSenderGateway

# Imports Exception Errors
from src.main.core.exceptions.email_service_exception import EmailServiceException

class SesEmailSender(EmailSenderGateway):

    def __init__(
            self,
        #     amazon_simple_email_service:
        #  AmazonSimpleEmailService = AmazonSimpleEmailService.client(
        # 'ses', region_name='us-east-1')
            service_name: str,
            access_key: str,
            secret_key: str,
            region_name: str
        ) -> None:
        amazon_simple_email_service = AmazonSimpleEmailService.client(
            service_name,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name
        )
        self.__amazon_simple_email_service = amazon_simple_email_service

    def send_email(self, to: str, subject: str, body: str) -> None:
        email_request = {
            # Substitua pelo seu endereço de e-mail verificado no SES
            'Source': 'rcvdigo@gmail.com',  
            'Destination': {'ToAddresses': [to]},
            'Message': {
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body}}
            }
        }

        # Envie o e-mail usando o client SES
        try:
            self.__amazon_simple_email_service.send_email(**email_request)
        except Exception as e:
            # Trate qualquer exceção que possa ocorrer durante o envio do e-mail
            raise EmailServiceException(
                message="Falha ao enviar o email: ",
                cause=e
            )
