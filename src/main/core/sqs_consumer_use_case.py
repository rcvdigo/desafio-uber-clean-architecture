# pylint: disable=too-many-arguments
from abc import ABC
from abc import abstractmethod
from typing import List


class SqsConsumerUseCase(ABC):
    
    @abstractmethod
    def consumer(self) -> List:
        pass