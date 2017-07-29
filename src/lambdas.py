import logging

import boto3

import player_load

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def load_players(event, context):
    logger.info('LoadPlayers triggered')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    player_load.load_players(bucket, key)

    return key, bucket
