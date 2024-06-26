from datetime import datetime
from src.main.core.controller_interface import ControllerInterface
from src.main.core.database_use_case import DatabaseUseCase
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse
from src.main.models.messages import Messages


class PostgreControllerSelectApi(ControllerInterface):

    def __init__(self, use_case: DatabaseUseCase) -> None:
        self.__use_case = use_case

    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:

        messages = self.__use_case.select_db()

        return HttpResponse(
            status_code=messages.status_code,
            body=messages.body
        )
