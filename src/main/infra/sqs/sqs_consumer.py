# Imports AWS services
import os
import json
from typing import Dict
from typing import List
import boto3 as AmazonSqs


# Imports Interfaces Adapters
from src.main.adapters.sqs_consumer_gateway import SqsConsumerGateway


class SqsConsumer(SqsConsumerGateway):

    def __init__(
            self,
            service_name: str,
            access_key: str,
            secret_key: str,
            region_name: str
    ) -> None:


        amazon_simple_queu_service: AmazonSqs

        amazon_simple_queu_service = AmazonSqs.client(
            service_name,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name
        )

        self.__amazon_simple_queu_service = amazon_simple_queu_service


    @classmethod
    def __extract_messages(cls, messages: List[Dict[str, str]]):
        response_list = [json.loads(msg['Body'])['Message'] for msg in messages if 'Body' in msg]
        return response_list
    
    def delete_messages(self, receipt_handles: List[str]):
        try:
            for receipt_handle in receipt_handles:
                self.__amazon_simple_queu_service.delete_message(
                    QueueUrl= os.getenv('URL_SQS'),
                    ReceiptHandle=receipt_handle
                )
        except Exception as e:
            raise e

    def consumer_sqs(self):
        response_list = []
        try:
            while True:
                response = self.__amazon_simple_queu_service.receive_message(
                    QueueUrl= os.getenv('URL_SQS'),
                    AttributeNames=['All'],
                    MessageAttributeNames=['All'],
                    MaxNumberOfMessages=10,
                    WaitTimeSeconds=2
                )
                
                messages = response.get('Messages', [])
                if not messages:
                    break
                else:
                    receipt_handles = [msg['ReceiptHandle'] for msg in messages]
                    extracted_messages = self.__extract_messages(messages=messages)
                    response_list.append(extracted_messages)
                    # self.delete_messages(receipt_handles)

            return response_list
        except Exception as e:
            raise e
