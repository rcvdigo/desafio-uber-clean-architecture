import os

from pymongo import MongoClient
from src.main.infra.repositories.mongo_db.mongo_db import MongoDb
from src.main.application.database_service import DatabaseService
from src.main.controllers.mongodb_controller_delete_api import MongodbControllerDeleteApi


def mongodb_composer_delete_api():
    uri = os.getenv('MONGO_URI')
    database_mongodb_use_case = MongoDb(
        mongo_client=MongoClient(uri),
        name_db='bancoMongoDB',
        name_collection='desafio_dio'
    )
    database_mongodb_service = DatabaseService(mongodb_gateway=database_mongodb_use_case)
    controller = MongodbControllerDeleteApi(use_case=database_mongodb_service)
    
    return controller.handle
