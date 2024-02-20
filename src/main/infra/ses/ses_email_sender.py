# pylint: disable=raise-missing-from
# Imports AWS services
# import boto3 as AmazonSimpleEmailService
from boto3 import client as AmazonSimpleEmailService


# Imports Interfaces Adapters
from src.main.adapters.email_sender_gateway import EmailSenderGateway


# Imports Exception Errors
from src.main.core.exceptions.email_service_exception import EmailServiceException


class SesEmailSender(EmailSenderGateway):

    def __init__(
            self,
            amazon_simple_email_service: AmazonSimpleEmailService,
            aws_region: str = 'us-east-1'
            ) -> None:
        self.__amazon_simple_email_service = amazon_simple_email_service(
            'ses', region_name=aws_region)
        # self.__client = self.__amazon_simple_email_service.client('ses', region_name=aws_region)

    def send_email(self, to: str, subject: str, body: str) -> None:
        email_request = {
            # Substitua pelo seu endereço de e-mail verificado no SES
            'Source': 'your-email@example.com',  
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
