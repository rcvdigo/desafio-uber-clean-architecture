from abc import ABC
from abc import abstractmethod
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse


class ControllerInterface(ABC):
    
    @abstractmethod
    def handle(
        self,
        http_request: HttpRequest,
    ) -> HttpResponse: pass
