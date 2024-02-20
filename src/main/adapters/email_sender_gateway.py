from abc import ABC
from abc import abstractmethod


class EmailSenderGateway(ABC):

    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> None: pass
