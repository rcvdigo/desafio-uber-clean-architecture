from datetime import date as datetime
from abc import ABC
from abc import abstractmethod
from src.main.core.http_response import HttpResponse


class DatabaseUseCase(ABC):

    @abstractmethod
    def insert_db(self,
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
    def select_db(self) -> HttpResponse: pass

    @abstractmethod
    def select_db_id(self, id) -> HttpResponse: pass
    
    @abstractmethod
    def update_db(self,
                  _id: str,
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
    def delete_db(self,
                  _id: str
                  )-> HttpResponse: pass
