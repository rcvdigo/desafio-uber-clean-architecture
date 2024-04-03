from datetime import datetime
from src.main.core.controller_interface import ControllerInterface
from src.main.core.database_use_case import DatabaseUseCase
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse


class PostgresqlControllerInsertHtml(ControllerInterface):

    def __init__(self, use_case: DatabaseUseCase) -> None:
        self.__use_case = use_case

    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:

        name = http_request.body["mensagem"]["nome"]
        age = http_request.body["mensagem"]["idade"]
        value = f'{http_request.body["mensagem"]["valor"]:.2f}'
        date = datetime.strptime(http_request.body["mensagem"]["data"], "%Y-%m-%d").date()
        key_pix = http_request.body["mensagem"]["chavePix"]
        source = http_request.body["mensagem"]["remetente"]
        to = http_request.body["mensagem"]["destinatario"]
        subject = http_request.body["mensagem"]["assunto"]
        body = http_request.body["mensagem"]["corpoMensagem"]
        phone_numbers = http_request.body["mensagem"]["telefone"]

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
