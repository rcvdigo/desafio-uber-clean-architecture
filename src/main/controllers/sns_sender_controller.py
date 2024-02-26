from src.main.core.controller_interface import ControllerInterface
from src.main.core.sns_sender_use_case import SnsSenderUseCase
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse


class SenderController(ControllerInterface):

    def __init__(self, use_case: SnsSenderUseCase) -> None:
        self.__use_case = use_case

    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:

        topic_arn = http_request.body["topic_arn"]
        name = http_request.body["name"]
        age = http_request.body["age"]
        value = http_request.body["value"]
        date = http_request.body["date"]
        key_pix = http_request.body["key_pix"]
        source = http_request.body["source"]
        to = http_request.body["to"]
        subject = http_request.body["subject"]
        body = http_request.body["body"]
        phone_numbers = http_request.body["phone_numbers"]

        response = self.__use_case.send_sns(
            topic_arn=topic_arn,
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
            status_code=200,
            body={"data": response}
        )
