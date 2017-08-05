import logging

import boto3

from services import agent_management, contract_management

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def create_agents(event, context):
    logger.info('LoadPlayers triggered')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    agent_management.create_agents(bucket, key)

    return key, bucket

def reset_agents(event, context):
    agent_management.reset_agents()
    return contract_management.assign_contracts()
