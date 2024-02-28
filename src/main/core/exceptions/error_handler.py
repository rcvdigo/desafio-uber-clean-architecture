from src.main.core.http_response import HttpResponse
from .types import HttpUnprocessableEntityError
from .types import HttpBadRequestError
from .types import HttpNotFoundError


def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(
            error,
                (
                    HttpNotFoundError,
                    HttpBadRequestError,
                    HttpUnprocessableEntityError
                )
            ):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": {
                    "title": error.name,
                    "detail": error.message
                }
            }
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": {
                "title": "Erro genérico, contate o administrador do sistema",
                "detail": str(error)
            }
        }
    )
