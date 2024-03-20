from datetime import date as datetime
from src.main.core.http_response import HttpResponse
from src.main.core.database_use_case import DatabaseUseCase
from src.main.adapters.database_mongodb_gateway import DatabaseMongodbGateway


class DatabaseService(DatabaseUseCase):

    def __init__(self,
                 use_case: DatabaseMongodbGateway
                 ) -> None:
        self.__use_case = use_case

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
            return self.__use_case.insert_mongo_db(
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

    def select_db(self):
        try:
            return self.__use_case.select_mongo_db()
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
            filter = {'_id':_id}
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
            return self.__use_case.update_mongo_db(filter=filter, request=request)
        except Exception as e:
            raise e
    
    def delete_db(self):
        pass
