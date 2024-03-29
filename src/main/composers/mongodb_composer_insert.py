import os

from pymongo import MongoClient
from src.main.infra.repositories.mongo_db.mongo_db import MongoDb
from src.main.application.database_service import DatabaseService
from src.main.controllers.mongodb_controller_insert_html import MongodbControllerInsertHtml
from src.main.controllers.mongodb_controller_insert_api import MongodbControllerInsertApi


def mongodb_composer_insert_html():
    uri = os.getenv('MONGO_URI')
    database_mongodb_use_case = MongoDb(
        mongo_client=MongoClient(uri),
        name_db='bancoMongoDB',
        name_collection='desafio_dio'
    )
    database_mongodb_service = DatabaseService(mongodb_gateway=database_mongodb_use_case)
    controller = MongodbControllerInsertHtml(use_case=database_mongodb_service)
    
    return controller.handle


def mongodb_composer_insert_api():
    uri = os.getenv('MONGO_URI')
    database_mongodb_use_case = MongoDb(
        mongo_client=MongoClient(uri),
        name_db='bancoMongoDB',
        name_collection='desafio_dio'
    )
    database_mongodb_service = DatabaseService(mongodb_gateway=database_mongodb_use_case)
    controller = MongodbControllerInsertApi(use_case=database_mongodb_service)
    
    return controller.handle
