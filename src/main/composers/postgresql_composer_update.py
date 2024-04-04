import os


from src.main.infra.repositories.postgresql.postgresql import Postgresql
from src.main.application.database_service_postgresql import DatabaseServicePostgresql
from src.main.controllers.postgresql_controller_update_api import PostgresqlControllerUpdateApi


def postgresql_composer_update():
    uri = os.getenv('POSTGRESQL_URI')
    database_postgresql_use_case = Postgresql(connection_string=uri)
    database_postgresql_service = DatabaseServicePostgresql(postgresql_gateway=database_postgresql_use_case)
    controller = PostgresqlControllerUpdateApi(use_case=database_postgresql_service)
    
    return controller.handle
