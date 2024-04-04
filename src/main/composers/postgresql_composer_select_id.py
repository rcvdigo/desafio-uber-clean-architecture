import os


from src.main.infra.repositories.postgresql.postgresql import Postgresql
from src.main.application.database_service_postgresql import DatabaseServicePostgresql
from src.main.controllers.postgresql_controller_select_html_id import PostgresqlControllerSelectIdHtml


def postgresql_composer_select_id():
    uri = os.getenv('POSTGRESQL_URI')
    database_postgresql_use_case = Postgresql(connection_string=uri)
    database_postgresql_service = DatabaseServicePostgresql(postgresql_gateway=database_postgresql_use_case)
    controller = PostgresqlControllerSelectIdHtml(use_case=database_postgresql_service)
    
    return controller.handle
