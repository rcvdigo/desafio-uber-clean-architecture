from abc import ABC
from abc import abstractmethod
from typing import Dict


class EmailSenderUseCase(ABC):

    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> Dict: pass
