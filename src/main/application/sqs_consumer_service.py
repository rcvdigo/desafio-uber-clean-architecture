import json
from typing import Dict
from src.main.core.sqs_consumer_use_case import SqsConsumerUseCase
from src.main.adapters.sqs_consumer_gateway import SqsConsumerGateway


class SqsService(SqsConsumerUseCase):
    
    def __init__(self, use_case: SqsConsumerGateway) -> None:
        self.__use_case = use_case
    
    def consumer(self):
        response = self.__use_case.consumer_sqs()
        format_response = self.__format_response(response=response)
        # print(format_response)
        return format_response

    @classmethod
    def __format_response(cls, response):
        response_format_list = []
        for item in response:
            data = json.loads(item[0])
            # print("-="*20)
            # print("Name:", data["name"])
            # print("Age:", data["age"])
            # print("Value:", data["value"])
            # print("Date:", data["date"])
            # print("Key PIX:", data["key_pix"])
            # print("Source:", data["source"])
            # print("To:", data["to"])
            # print("Subject:", data["subject"])
            # print("Body:", data["body"])
            # print("Phone Numbers:", data["phone_numbers"])
            # print("-="*20)
            response_format = {
            "type": "SQS",
            "count": len(response),
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
            
        return response_format_list
