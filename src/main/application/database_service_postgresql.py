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
            messages=self.__postgresql_gateway.select_postgresql()

            messages_dict={str(message.id): {
                'id': message.id,
                'name': message.name,
                'age': message.age,
                'value': message.value,
                'date': message.date.strftime("%Y-%m-%d"),
                'key_pix': message.key_pix,
                'source': message.source,
                'to': message.to,
                'subject': message.subject,
                'body': message.body,
                'phone_numbers': message.phone_numbers
            } for message in messages}

            return HttpResponse(
                status_code=200,
                body=messages_dict
            )

        except Exception as e:
            raise e
        
    def select_db_id(self, id) -> HttpResponse:
        try:
            message=self.__postgresql_gateway.select_postgresql_id(id=id)

            for msg in message:
                message_dict={
                    'id': msg.id,
                    'name': msg.name,
                    'age': msg.age,
                    'value': msg.value,
                    'date': msg.date.strftime("%Y-%m-%d"),
                    'key_pix': msg.key_pix,
                    'source': msg.source,
                    'to': msg.to,
                    'subject': msg.subject,
                    'body': msg.body,
                    'phone_numbers': msg.phone_numbers
                    }

            return HttpResponse(
                status_code=200,
                body=message_dict
            )

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
                  ) -> HttpResponse:
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

            message_update = self.__postgresql_gateway.update_postgresql(filter=filter, request=request)

            for msg in message_update:
                message_dict={
                    'id': msg.id,
                    'name': msg.name,
                    'age': msg.age,
                    'value': msg.value,
                    'date': msg.date.strftime("%Y-%m-%d"),
                    'key_pix': msg.key_pix,
                    'source': msg.source,
                    'to': msg.to,
                    'subject': msg.subject,
                    'body': msg.body,
                    'phone_numbers': msg.phone_numbers
                    }

            return HttpResponse(
                status_code=200,
                body=message_dict
            )
        except Exception as e:
            raise e
    
    def delete_db(self, id: int) -> HttpResponse:
        try:
            filter = id
            return self.__postgresql_gateway.delete_postgresql(filter=filter)
        except Exception as e:
            raise e
