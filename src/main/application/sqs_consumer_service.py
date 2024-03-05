import json
from typing import Dict
from src.main.core.sqs_consumer_use_case import SqsConsumerUseCase
from src.main.adapters.sqs_consumer_gateway import SqsConsumerGateway


class SqsService(SqsConsumerUseCase):
    
    def __init__(self, use_case: SqsConsumerGateway) -> None:
        self.__use_case = use_case
    
    def consumer(self):
        response = self.__use_case.consumer_sqs()
        return self.__format_response(response=response)

    @classmethod
    def __format_response(cls, response):
        response_format_dict = {}
        response_format_list = []
        for item in response:
            data = json.loads(item[0])

            response_format = {
            "type": "SQS",
            "attributes": {
                "name": data["name"],
                "age": data["age"],
                "value": data["value"],
                "date": data["date"],
                "key_pix": data["key_pix"],
                "source": data["source"],
                "to": data["to"],
                "subject": data["subject"],
                "body": data["body"],
                "phone_numbers": data["phone_numbers"],
                }
            }

            response_format_list.append(response_format)
            
        response_format_dict.update({'count': len(response_format_list), 'data': response_format_list})
        return response_format_dict
