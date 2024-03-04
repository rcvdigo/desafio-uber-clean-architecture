import os
from typing import Dict


from src.main.infra.sqs.sqs_consumer import SqsConsumer
from src.main.application.sqs_consumer_service import SqsService


def sqs_consumer_composer():
    sqs_gateway = SqsConsumer(
        service_name=os.getenv('SQS'),
        region_name=os.getenv('REGIAO'),
        access_key=os.getenv('CHAVE_ACESSO'),
        secret_key=os.getenv('CHAVE_SECRETA')
    )
    sqs_service = SqsService(use_case=sqs_gateway)
    response = sqs_service.consumer()
    return response
