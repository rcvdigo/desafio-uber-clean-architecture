from abc import ABC
from abc import abstractmethod
from typing import Dict


class EmailSenderGateway(ABC):

    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> Dict: pass
