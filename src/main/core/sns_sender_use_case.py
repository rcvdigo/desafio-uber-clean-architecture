from datetime import date
from abc import ABC
from abc import abstractmethod
from typing import Dict


class SnsSenderUseCase(ABC):

    @abstractmethod
    def send_sns(self,
                 topic_arn: str,
                 name: str,
                 age: int,
                 value: float,
                 date: date,
                 key_pix: str,
                 source: str,
                 to: str,
                 subject: str,
                 body: str,
                 phone_numbers: str
                 ) -> Dict: pass
