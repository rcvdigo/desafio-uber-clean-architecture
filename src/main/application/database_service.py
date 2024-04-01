from datetime import date as datetime
from src.main.core.http_response import HttpResponse
from src.main.core.database_use_case import DatabaseUseCase
from src.main.adapters.database_mongodb_gateway import DatabaseMongodbGateway


class DatabaseService(DatabaseUseCase):

    def __init__(self,
                 mongodb_gateway: DatabaseMongodbGateway
                 ) -> None:
        self.__mongodb_gateway = mongodb_gateway

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
                  ) -> HttpResponse:
        try:
            return self.__mongodb_gateway.insert_mongo_db(
                name=name,
                age=age,
                value=value,
                date=date,
                key_pix=key_pix,
                source=source,
                to=to,
                subject=subject,
                body=body,
                phone_numbers=phone_numbers
            )
        except Exception as e:
            raise e

    def select_db(self) -> HttpResponse:
        try:
            return self.__mongodb_gateway.select_mongo_db()
        except Exception as e:
            raise e
        
    def select_db_id(self, id) -> HttpResponse:
        try:
            return self.__mongodb_gateway.select_mongo_db_id(id=id)
        except Exception as e:
            raise e
    
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
                  ):
        try:
            filter = {'_id': _id}
            request = {
                'name': name,
                'age': age,
                'value': value,
                'date': date,
                'key_pix': key_pix,
                'source': source,
                'to': to,
                'subject': subject,
                'body': body,
                'phone_numbers': phone_numbers
            }
            return self.__mongodb_gateway.update_mongo_db(filter=filter, request=request)
        except Exception as e:
            raise e
    
    def delete_db(self, _id: str) -> HttpResponse:
        try:
            filter = {'_id': _id}
            return self.__mongodb_gateway.delete_mongo_db(filter=filter)
        except Exception as e:
            raise e
