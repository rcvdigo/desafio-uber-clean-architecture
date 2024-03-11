# pylint: disable = raise-missing-from
# pylint: disable=import-error
# pylint: disable=too-many-arguments

# Imports .env
import json

# Imports Types
from typing import Dict
from datetime import date as datetime


# Imports AWS services
import boto3 as AmazonSimpleEmailService


# Imports Interfaces Adapters
from src.main.adapters.sns_sender_gateway import SnsSenderGateway


class SnsSender(SnsSenderGateway):

    def __init__(
            self,
            service_name: str,
            access_key: str,
            secret_key: str,
            region_name: str
        ) -> None:

        amazon_simple_notification_service = AmazonSimpleEmailService.client(
            service_name,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name
        )

        self.__amazon_simple_notification_service=amazon_simple_notification_service

    def send_sns(self,
                 topic_arn: str,
                 name: str,
                 age: int,
                 value: float,
                 date: datetime,
                 key_pix: str,
                 source: str,
                 to: str,
                 subject: str,
                 body: str,
                 phone_numbers: str
                 ) -> Dict:

        sns_request = {
            'name': name,
            'age': age,
            'value': value,
            'date': date,
            'key_pix': key_pix,
            'source': source,
            'to': to,
            'subject': subject,
            'body': body,
            'phone_numbers': phone_numbers
        }

        # Enviando a mensagem ao tópico SES
        try:
            self.__amazon_simple_notification_service.publish(
                TopicArn=topic_arn,
                Subject="API_DESAFIO_UBER",
                Message=json.dumps(sns_request),
            )
            if sns_request['phone_numbers'] == '5511941982086':
                self.__amazon_simple_notification_service.publish(
                    PhoneNumber=sns_request['phone_numbers'],
                    Message=sns_request['body'],
                )
        except Exception as e:
            # Trate qualquer exceção que possa ocorrer durante o envio do e-mail
            raise e
