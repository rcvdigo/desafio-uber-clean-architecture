# from src.presentation.interfaces.controller_interface import ControllerInterface
from src.main.core.controller_interface import ControllerInterface
# from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.main.core.email_sender_use_case import EmailSenderUseCase
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse


class SenderController(ControllerInterface):
    
    def __init__(self, use_case: EmailSenderUseCase) -> None:
        self.__use_case = use_case
    
    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse:

        to = http_request.body["to"]
        subject = http_request.body["subject"]
        b = http_request.body["body"]

        response = self.__use_case.send_email(
            to=to,
            subject=subject,
            body=b
        )

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
