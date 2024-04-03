from datetime import date as datetime
from src.main.core.database_use_case import DatabaseUseCase
from src.main.adapters.database_postgresql_gateway import DatabasePostgresqlGateway
from src.main.core.http_response import HttpResponse


class DatabaseServicePostgresql(DatabaseUseCase):

    def __init__(self,
                 postgresql_gateway: DatabasePostgresqlGateway
                 ) -> None:
        self.__postgresql_gateway = postgresql_gateway

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
            new_message = self.__postgresql_gateway.insert_postgresql(
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

            return HttpResponse(
                status_code=200,
                body=new_message
            )
        except Exception as e:
            raise e

    def select_db(self) -> HttpResponse:
        try:
            return self.__postgresql_gateway.select_postgresql()
        except Exception as e:
            raise e
        
    def select_db_id(self, id) -> HttpResponse:
        try:
            return self.__postgresql_gateway.select_postgresql_id(id=id)
        except Exception as e:
            raise e
    
    def update_db(self,
                  id: int,
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
            filter = id
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
            return self.__postgresql_gateway.update_postgresql(filter=filter, request=request)
        except Exception as e:
            raise e
    
    def delete_db(self, id: int) -> HttpResponse:
        try:
            filter = id
            return self.__postgresql_gateway.delete_postgresql(filter=filter)
        except Exception as e:
            raise e
