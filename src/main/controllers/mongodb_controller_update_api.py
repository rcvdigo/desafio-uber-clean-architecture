from src.main.core.controller_interface import ControllerInterface
from src.main.core.database_use_case import DatabaseUseCase
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse


class MongodbControllerUpdateApi(ControllerInterface):

    def __init__(self, use_case: DatabaseUseCase) -> None:
        self.__use_case = use_case

    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:

        _id = http_request.body["_id"]
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

        response = self.__use_case.update_db(
            _id=_id,
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
        response.body['_id'] = str(response.body['_id'])
        return HttpResponse(
            status_code=200,
            body=response.body
        )
