from src.main.core.controller_interface import ControllerInterface
from src.main.core.database_use_case import DatabaseUseCase
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse


class MongodbControllerSelectIdHtml(ControllerInterface):

    def __init__(self, use_case: DatabaseUseCase) -> None:
        self.__use_case = use_case

    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:
        
        response = self.__use_case.select_db_id(id=http_request.path_params)

        return HttpResponse(
            status_code=response.status_code,
            body=response.body
        )
