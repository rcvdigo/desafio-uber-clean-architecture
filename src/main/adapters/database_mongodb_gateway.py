from datetime import date as datetime
from abc import ABC
from abc import abstractmethod
from src.main.core.http_response import HttpResponse


class DatabaseMongodbGateway(ABC):

    @abstractmethod
    def insert_mongo_db(self,
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
                        ) -> HttpResponse: pass
   
    @abstractmethod
    def select_mongo_db(self) -> HttpResponse: pass
    
    @abstractmethod
    def update_mongo_db(self,
                        filter: dict[str, str],
                        request: dict[str, str]
                        ) -> HttpResponse: pass
    
    @abstractmethod
    def delete_mongo_db(self): pass
