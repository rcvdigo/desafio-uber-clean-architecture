import os


from src.main.infra.repositories.postgresql.postgresql import Postgresql
from src.main.application.database_service_postgresql import DatabaseServicePostgresql
from src.main.controllers.postgresql_controller_insert_api import PostgresqlControllerInsertApi
from src.main.controllers.postgresql_controller_insert_html import PostgresqlControllerInsertHtml


def postgresql_composer_insert_html():
    uri = os.getenv('POSTGRESQL_URI')
    database_postgresql_use_case = Postgresql(connection_string=uri)
    database_postgresql_service = DatabaseServicePostgresql(postgresql_gateway=database_postgresql_use_case)
    controller = PostgresqlControllerInsertHtml(use_case=database_postgresql_service)
    
    return controller.handle

def postgresql_composer_insert_api():
    uri = os.getenv('POSTGRESQL_URI')
    database_postgresql_use_case = Postgresql(connection_string=uri)
    database_postgresql_service = DatabaseServicePostgresql(postgresql_gateway=database_postgresql_use_case)
    controller = PostgresqlControllerInsertApi(use_case=database_postgresql_service)
    
    return controller.handle
