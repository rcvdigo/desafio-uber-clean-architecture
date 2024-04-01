from bson import ObjectId
from datetime import date as datetime
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

            # Convertendo a lista em um dicionário onde a chave é o _id de cada elemento
            dict_result = {str(item['_id']): item for item in response}
            
            # Convertendo os valores _id ObjectId em str
            for key, value in dict_result.items():
                value['_id'] = str(value['_id'])

            return HttpResponse(
                body=dict_result,
                status_code=200
            )
        except Exception as e:
            raise e
        
    def select_mongo_db_id(self, id: dict[str, str]) -> HttpResponse:
        
        id = ObjectId(id['_id'])
        
        response = self.__collection.find_one(filter=id)
       
        response['_id'] = str(response['_id'])

        return HttpResponse(
            body=response,
            status_code=200
        )
    
    def update_mongo_db(self, filter: dict[str, str], request: dict[str, str]) -> HttpResponse:
        # Novo valor a ser definido
        new_value = {'$set': request}

        # Convertendo str para ObjectId
        filter['_id'] = ObjectId(filter['_id'])
        
        # Execução da ordem de Update
        self.__collection.update_one(filter, new_value)
        
        # Consulta do objeto que foi atualizado
        response = self.__collection.find_one(filter)
        return HttpResponse(
            body=response,
            status_code=200
            )

    def delete_mongo_db(self,
                         filter: dict[str, str]
                         )-> HttpResponse:
        # Convertendo str para ObjectId
        filter['_id'] = ObjectId(filter['_id'])

        # Removendo o documento
        response = self.__collection.delete_one(filter)

        # Se o dado for deletado com sucesso
        if response.acknowledged == 1.0:
            return HttpResponse(
                body=response.acknowledged,
                status_code=200
            )
        else:
            return HttpResponse(
                body=response.acknowledged,
                status_code=500
            )
