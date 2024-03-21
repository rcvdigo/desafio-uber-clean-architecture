from src.main.core.controller_interface import ControllerInterface
from src.main.core.database_use_case import DatabaseUseCase
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse


class MongodbControllerInsertHtml(ControllerInterface):

    def __init__(self, use_case: DatabaseUseCase) -> None:
        self.__use_case = use_case

    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:

        nome = http_request.body["mensagem"]["nome"]
        idade = http_request.body["mensagem"]["idade"]
        valor = f"{http_request.body['mensagem']['valor']:.2f}"
        data = http_request.body["mensagem"]["data"]
        chavePix = http_request.body["mensagem"]["chavePix"]
        telefone = http_request.body["mensagem"]["telefone"]
        remetente = http_request.body["mensagem"]["remetente"]
        destinatario = http_request.body["mensagem"]["destinatario"]
        assunto = http_request.body["mensagem"]["assunto"]
        corpoMensagem = http_request.body["mensagem"]["corpoMensagem"]

        response = self.__use_case.insert_db(
            name=nome,
            age=idade,
            value=valor,
            date=data,
            key_pix=chavePix,
            source=remetente,
            to=destinatario,
            subject=assunto,
            body=corpoMensagem,
            phone_numbers=telefone
        )
        response.body['_id'] = str(response.body['_id'])
        return HttpResponse(
            status_code=200,
            body=response.body
        )
