from typing import List
from datetime import date
from src.main.infra.repositories.postgresql.settings.connection import DbConnectionHandler
from src.main.infra.repositories.postgresql.entities.messages_entities import Messages as MessagesEntity
from src.main.adapters.database_postgresql_gateway import DatabasePostgresqlGateway
from src.main.models.messages import Messages


class Postgresql(DatabasePostgresqlGateway):
    def __init__(self, connection_string: str) -> None:
        self.__connection_string = connection_string

    def insert_postgresql(self,
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
                          ) -> dict[str, str]:
        with DbConnectionHandler(connection_string=self.__connection_string) as database:
            try:
                new_registry = MessagesEntity(
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
                database.session.add(new_registry)
                database.session.commit()
                new_registry = {
                    'name': name,
                    'age': age,
                    'value': value,
                    'date': date.strftime("%d/%m/%Y"),
                    'key_pix': key_pix,
                    'source': source,
                    'to': to,
                    'subject': subject,
                    'body': body,
                    'phone_numbers': phone_numbers
                }
                return new_registry
            except Exception as e:
                database.session.rollback()
                raise e

    def select_postgresql(self) -> List[Messages]:
        with DbConnectionHandler(connection_string=self.__connection_string) as database:
            try:
                messages = (
                    database.session
                    .query(MessagesEntity)
                    .all()
                )
                return messages
            except Exception as e:
                database.session.rollback()
                raise e
    

    def select_postgresql_id(self,
                             id: int
                             ) -> List[Messages]:
        with DbConnectionHandler(connection_string=self.__connection_string) as database:
            try:
                messages = (
                    database.session
                    .query(MessagesEntity)
                    .filter(MessagesEntity.id == id)
                    .all()
                )
                return messages
            except Exception as e:
                database.session.rollback()
                raise e

    def update_postgresql(self, filter: int, request: dict[str, str]) -> List[Messages]:
        with DbConnectionHandler(connection_string=self.__connection_string) as database:
            try:
                # Consultando objeto usando id como filtro
                messages_update = (
                    database.session
                    .query(MessagesEntity)
                    .filter(MessagesEntity.id == filter)
                    .all()
                )

                # Atualizando dados
                for data in messages_update:
                    data.name = request['name']
                    data.age = request['age']
                    data.value = request['value']
                    data.date = request['date']
                    data.key_pix = request['key_pix']
                    data.source = request['source']
                    data.to = request['to']
                    data.subject = request['subject']
                    data.body = request['body']
                    data.phone_numbers = request['phone_numbers']
                
                # Commit após atualização realizada
                database.session.commit()

                # Refazendo a consulta
                messages_update = (
                    database.session
                    .query(MessagesEntity)
                    .filter(MessagesEntity.id == filter)
                    .all()
                )
                return messages_update
            except Exception as e:
                database.session.rollback()
                raise e
    
    def delete_postgresql(self, filter: int) -> List[Messages]:
        with DbConnectionHandler(connection_string=self.__connection_string) as database:
            try:
                # Query para encontrar a mensagem com o ID fornecido
                message_to_delete = (
                    database.session
                    .query(MessagesEntity)
                    .filter(MessagesEntity.id == filter)
                    .one_or_none()
                )

                # Verificar se a mensagem foi encontrada
                if message_to_delete is not None:
                    # Excluir a mensagem
                    database.session.delete(message_to_delete)
                    database.session.commit()
                    return f"Mensagem com ID {filter} deletada com sucesso."
                else:
                    # Se a mensagem não foi encontrada, levantar uma exceção ou retornar uma mensagem de erro
                    raise ValueError(f"Mensagem com ID {filter} não encontrada.")
            except Exception as e:
                database.session.rollback()
                raise e
