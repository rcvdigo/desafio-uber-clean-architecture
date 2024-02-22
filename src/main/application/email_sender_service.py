from typing import Dict


from src.main.core.email_sender_use_case import EmailSenderUseCase
from src.main.adapters.email_sender_gateway import EmailSenderGateway


class EmailSenderService(EmailSenderUseCase):

    def __init__(self, email_gateway: EmailSenderGateway):
        self.__email_gateway = email_gateway

    def send_email(self, to: str, subject: str, body: str) -> Dict:
        self.__email_gateway.send_email(
            to=to,
            subject=subject,
            body=body
            )
        
        response = self.__format_response(
            to=to,
            subject=subject,
            body=body
        )
        return response

    @classmethod
    def __format_response(
        cls,
        to: str,
        subject: str,
        body: int
    ) -> Dict:
        response = {
            "type": "E-mail",
            "count": 1,
            "attributes": {
                "to": to,
                "subject": subject,
                "body": body,
            }
        }
        return response