from src.main.core.controller_interface import ControllerInterface
from src.main.core.database_use_case import DatabaseUseCase
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse


class PostgresqlControllerUpdateApi(ControllerInterface):

    def __init__(self, use_case: DatabaseUseCase) -> None:
        self.__use_case = use_case

    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:

        id = http_request.body["id"]
        name = http_request.body["name"]
        age = http_request.body["age"]
        value = f'{http_request.body["value"]:.2f}'
        date = http_request.body["date"]
        key_pix = http_request.body["key_pix"]
        source = http_request.body["source"]
        to = http_request.body["to"]
        subject = http_request.body["subject"]
        body = http_request.body["body"]
        phone_numbers = http_request.body["phone_numbers"]

        response: HttpResponse = self.__use_case.update_db(
            id=id,
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
            status_code=response.status_code,
            body=response.body
        )
