from src.main.core.email_sender_use_case import EmailSenderUseCase
from src.main.adapters.email_sender_gateway import EmailSenderGateway


class EmailSenderService(EmailSenderUseCase):

    def __init__(self, email_gateway: EmailSenderGateway):
        self.__email_gateway = email_gateway

    def send_email(self, to: str, subject: str, body: str) -> None:
        self.__email_gateway.send_email(
            to=to,
            subject=subject,
            body=body
            )
