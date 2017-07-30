import logging

import boto3

import agent_management
from services.code_name.generator import generate_codename

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def create_agents(event, context):
    logger.info('LoadPlayers triggered')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    agent_management.create_agents(bucket, key)

    return key, bucket

def reset_players(event, context):
    return generate_codename()
