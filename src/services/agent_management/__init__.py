from csv import DictReader
from itertools import izip
import logging

import boto3

from utils.db import connection
from services import code_name
from services.agent_management import sql
from services.agent_management import data_access

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.resource('s3')


def create_agents(bucket, key):
    logger.info('Loading player data from s3://%s/%s', bucket, key)
    obj = s3.Object(bucket_name=bucket, key=key)
    lines = obj.get()['Body'].read().split('\n')
    data = [line for line in DictReader(lines)]

    logger.info('Inserting %s players', len(data))

    with connection.cursor() as cursor:
        cursor.executemany(sql.ADD_PLAYERS, data)
    connection.commit()

    logger.info('Player load complete')


def reset_agents():
    """
    First iteration:  Just assigning code names.

    Need to figure out:
        - How many agents need new code names (based on being alive)
        - What are all the current code names
    """
    logger.info('Beginning player reset')
    assassinated_players = tuple(data_access.get_assassinated_players())

    if not assassinated_players:
        logger.info('No players need to be reset')
        return

    new_codenames = code_name.generate_n_codenames(len(assassinated_players))
    data_access.assign_codenames(izip(assassinated_players, new_codenames))
    data_access.revive_assassinated_agents()
    logger.info('Player reset was successful')


def get_all_agents():
    """
    Return all agents in the game
    """
    return data_access.get_all()


def get_agents_by_handle(*handles):
    """
    For the handles passed in, return Agent objects.
    """
    handle_to_agent = {
        agent.handle: agent
        for agent in data_access.get_agents_by_handle(*handles)
    }

    return tuple(handle_to_agent[h] for h in handles)

def assassinate_agent(agent):
    """
    Assassinate an agent.
    """
    # TODO notify the user that they've been assassinated
    data_access.assassinate_agent(agent.id)
