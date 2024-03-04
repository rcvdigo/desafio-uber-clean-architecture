# pylint: disable=too-many-arguments
from abc import ABC
from abc import abstractmethod
from typing import Dict


class SqsConsumerGateway(ABC):
    
    @abstractmethod
    def consumer_sqs(self): pass
