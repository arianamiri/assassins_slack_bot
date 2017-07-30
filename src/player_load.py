from csv import DictReader
import logging

import boto3

from db_access import connection
import sql


logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.resource('s3')

def load_players(bucket, key):
    logger.info('Loading player data from s3://%s/%s', bucket, key)
    obj =  s3.Object(bucket_name=bucket, key=key)
    lines = obj.get()['Body'].read().split('\n')
    data = [line for line in DictReader(lines)]

    logger.info('Inserting %s players', len(data))
    logger.info(data)
    with connection.cursor() as cursor:
        cursor.executemany(sql.ADD_PLAYERS, data)

    connection.commit()

    logger.info('Player load complete')
