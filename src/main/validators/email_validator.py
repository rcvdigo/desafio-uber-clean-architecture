# pylint: disable=import-error
from cerberus import Validator
from src.main.core.exceptions.types.http_unprocessable_entity import HttpUnprocessableEntityError


def email_validator(request: any):
    body_validator = Validator(
        {
            "to": {
                "type": "string",
                "required": True,
                "empty": False
            },
            "subject": {
                "type": "string",
                "required": True,
                "empty": False
            },
            "body": {
                "type": "string",
                "required": True,
                "empty": False
            }
        }
    )

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(message=body_validator.errors)
