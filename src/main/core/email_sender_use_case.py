from abc import ABC
from abc import abstractmethod


class EmailSenderUseCase(ABC):

    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> None: pass
