import os


from src.main.core.controller_interface import ControllerInterface
from src.main.core.sns_sender_use_case import SnsSenderUseCase
from src.main.core.email_sender_use_case import EmailSenderUseCase
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse
from typing import Dict

class EmailSnsSenderController(ControllerInterface):

    def __init__(self, use_case: SnsSenderUseCase | EmailSenderUseCase) -> None:
        self.__use_case = use_case

    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:
        
        topic_arn = os.getenv('TOPIC_ARN')
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

        response_sns = self.__use_case['sns'].send_sns(
            topic_arn=topic_arn,
            name=nome,
            age=idade,
            value=valor,
            date=data,
            key_pix=chavePix,
            phone_numbers=telefone,
            source=remetente,
            to=destinatario,
            subject=assunto,
            body=corpoMensagem
        )

        
        response_email = self.__use_case['email'].send_email(
            to=destinatario,
            subject=assunto,
            body=f"{corpoMensagem}.\nPix de: R${str(valor)} realizado com sucesso!" 
        )

        return HttpResponse(
            status_code=200,
            body={"data": {
                "sns": response_sns,
                "email": response_email
            }}
        )
