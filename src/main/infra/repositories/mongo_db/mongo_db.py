from datetime import date as datetime
from typing import Dict
from pymongo import MongoClient
from pymongo.cursor import Cursor
from src.main.core.http_response import HttpResponse
from src.main.adapters.database_mongodb_gateway import DatabaseMongodbGateway


class MongoDb(DatabaseMongodbGateway):

    def __init__(self,
                 mongo_client: MongoClient,
                 name_db: str,
                 name_collection: str
                 ) -> None:
        self.__mongo_client = mongo_client
        self.__database = self.__mongo_client[f'{name_db}']
        self.__collection = self.__database[f'{name_collection}']
    
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
                        ) -> HttpResponse:
        try:
            # Dados a serem inseridos
            request = {
                'name':name,
                'age':age,
                'value':value,
                'date':date,
                'key_pix':key_pix,
                'source':source,
                'to':to,
                'subject':subject,
                'body':body,
                'phone_numbers':phone_numbers
            }     
            
            # Inserindo os dados na coleção
            self.__collection.insert_one(request)

            return HttpResponse(
                body=request,
                status_code=200
            )
        except Exception as e:
            raise e

    def select_mongo_db(self) -> HttpResponse:
        try:
            response = []

            # Consultando todos os documentos na coleção
            docs: Cursor = self.__collection.find()
            
            # Iterando sobre os documentos e imprimindo-os
            for data in docs:
                response.append(data)

            return HttpResponse(
                body=response,
                status_code=200
            )
        except Exception as e:
            raise e
    
    def update_mongo_db(self, filter: dict[str, str], request: dict[str, str]) -> HttpResponse:
        new_value = {'$set': request}  # Novo valor a ser definido

        return HttpResponse(
            body=self.__collection.update_one(filter, new_value).raw_result,
            status_code=200
            )

    def delete_mongo_db(self):
        # Removendo um documento da coleção
        filter = {"chave": "valor"}  # Filtro para encontrar o documento a ser removido

        # Removendo o documento
        self.__collection.delete_one(filter)
