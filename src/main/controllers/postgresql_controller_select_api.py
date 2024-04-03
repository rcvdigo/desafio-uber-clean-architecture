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

        messages: Messages = self.__use_case.select_db()
        
        # Converter a lista de objetos Messages em um dicionário onde as chaves são os IDs
        # messages_dict = {str(message.id): message.__dict__ for message in messages}
        messages_dict = {str(message.id): {
            'id': message.id,
            'name': message.name,
            'age': message.age,
            'value': message.value,
            'date': message.date,
            'key_pix': message.key_pix,
            'source': message.source,
            'to': message.to,
            'subject': message.subject,
            'body': message.body,
            'phone_numbers': message.phone_numbers
        } for message in messages}

        return HttpResponse(
            status_code=200,
            body=messages_dict
        )
