# pylint: disable=too-many-arguments
from typing import Dict
from datetime import date as datetime


from src.main.core.sns_sender_use_case import SnsSenderUseCase
from src.main.adapters.sns_sender_gateway import SnsSenderGateway


class SnsService(SnsSenderUseCase):

    def __init__(self, sns_gateway: SnsSenderGateway):
        self.__sns_gateway = sns_gateway

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

        self.__sns_gateway.send_sns(
            topic_arn=topic_arn,
            name=name,
            age=age,
            value=value,
            date=date,
            key_pix=key_pix,
            source=source,
            to=to,
            subject=subject,
            body=body,
            phone_numbers=phone_numbers
        )

        response = self.__format_response(
            topic_arn=topic_arn,
            name=name,
            age=age,
            value=value,
            date=date,
            key_pix=key_pix,
            source=source,
            to=to,
            subject=subject,
            body=body,
            phone_numbers=phone_numbers
        )
        return response

    @classmethod
    def __format_response(
        cls,
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

        response = {
            "type": "SNS",
            "count": 1,
            "attributes": {
                "topic_arn": topic_arn,
                "name": name,
                "age": age,
                "value": value,
                "date": date,
                "key_pix": key_pix,
                "source": source,
                "to": to,
                "subject": subject,
                "body": body,
                "phone_numbers": phone_numbers,
            }
        }
        return response
