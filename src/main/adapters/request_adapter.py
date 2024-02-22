# pylint: disable=import-error
from typing import Callable
from flask import request as FlaskRequest
from src.main.core.http_request import HttpRequest
from src.main.core.http_response import HttpResponse


def request_adapter(
        request: FlaskRequest, # type: ignore
        controller: Callable
        ) -> HttpResponse:

    body = None

    if request.data:
        body = request.json

    http_request = HttpRequest(
        body=body,
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path
    )

    http_response =  controller(http_request)

    return http_response
