import logging
import os
from csv import DictReader

import boto3

from services.code_name import generate_n_codenames

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

s3 = boto3.resource('s3')
dynamodb = boto3.client('dynamodb')


def create_agents(bucket, key):
    logger.info('Loading player data from s3://%s/%s', bucket, key)
    obj =  s3.Object(bucket_name=bucket, key=key)
    lines = obj.get()['Body'].read().decode('utf-8').split('\n')
    batch = []
    code_names = generate_n_codenames(len(lines))
    for line in DictReader(lines):
        if len(batch) == 25:
            _create_agents_batch(batch)
            batch = []
        else:
            batch.append({
                'PutRequest': {
                    'Item': {
                        'slack_handle': {'S': line['slack_handle']},
                        'name': {'S': line['agent_name']},
                        'code_name': {'S': code_names.pop()},
                        'is_alive': {'BOOL': True},
                        'kills': {'N': '0'},
                        'deaths': {'N': '0'}
                    }
                }
            })

    if batch:
        _create_agents_batch(batch)

    logger.info('Player load complete')


def _create_agents_batch(agents_batch):
    logger.info(agents_batch)
    table_name = os.environ['PLAYER_TABLE']
    request_items = {
        table_name: agents_batch
    }
    logger.info(request_items)
    dynamodb.batch_write_item(
        RequestItems=request_items
    )
