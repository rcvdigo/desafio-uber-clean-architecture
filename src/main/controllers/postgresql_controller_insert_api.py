from datetime import datetime
from src.main.core.controller_interface import ControllerInterface
from src.main.core.database_use_case import DatabaseUseCase
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse


class PostgresqlControllerInsertApi(ControllerInterface):

    def __init__(self, use_case: DatabaseUseCase) -> None:
        self.__use_case = use_case

    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:

        name = http_request.body["name"]
        age = http_request.body["age"]
        value = f'{http_request.body["value"]:.2f}'
        date = datetime.strptime(http_request.body["date"], "%d/%m/%Y").date()
        key_pix = http_request.body["key_pix"]
        source = http_request.body["source"]
        to = http_request.body["to"]
        subject = http_request.body["subject"]
        body = http_request.body["body"]
        phone_numbers = http_request.body["phone_numbers"]
        
        response = self.__use_case.insert_db(
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

        return response
