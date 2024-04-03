from datetime import date as datetime
from abc import ABC
from abc import abstractmethod
from typing import List


from src.main.models.messages import Messages


class DatabasePostgresqlGateway(ABC):

    @abstractmethod
    def insert_postgresql(self,
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
                        ) -> dict[str, str]: pass
   
    @abstractmethod
    def select_postgresql(self) -> List[Messages]: pass
    
    @abstractmethod
    def select_postgresql_id(self, id: int) -> List[Messages]: pass
    
    @abstractmethod
    def update_postgresql(self,
                        filter: int,
                        request: dict[str, str]
                        ) -> List[Messages]: pass
    
    @abstractmethod
    def delete_postgresql(self,
                        filter: int
                        )-> List[Messages]: pass
