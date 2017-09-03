import logging
from collections import namedtuple
from itertools import groupby

from utils.db import connection
from services.contract_management import sql


logger = logging.getLogger()


Contract = namedtuple('Contract', ('id', 'owner_id', 'target_id', 'bounty', 'is_open', 'is_successful'))


def assign_contract(agent_id, target_id, bounty):
    with connection.cursor() as cursor:
        cursor.execute(sql.ASSIGN_CONTRACT, args={
            'agent_id': agent_id,
            'target_id': target_id,
            'bounty': bounty
        })
    connection.commit()


def assign_multiple_contracts(contract_params):
    with connection.cursor() as cursor:
        cursor.executemany(sql.ASSIGN_CONTRACT, args=contract_params)
    connection.commit()


def get_available_targets_lookup():
    with connection.cursor() as cursor:
        cursor.execute(sql.GET_AVAILABLE_TARGETS_FOR_ALL_AGENTS)
        results = cursor.fetchall()

    return {
        agent_id: set(pt[1] for pt in possible_targets)
        for agent_id, possible_targets in groupby(results, key=lambda x: x[0])
    }


def get_current_max_bounty():
    with connection.cursor() as cursor:
        cursor.execute(sql.GET_MAX_BOUNTY)
        results = cursor.fetchone()

    return results[0]


def is_contract_valid(agent_id, target_id, code_name):
    with connection.cursor() as cursor:
        count = cursor.execute(sql.VALIDATE_CONTRACT, args={
            'owner_id': agent_id,
            'target_id': target_id,
            'code_name': code_name
        })

        if count:
            contract = Contract(*cursor.fetchone())
        else:
            contract = None

    return contract


def payout_contract(contract_id):
    """
    Successfully closes a contract.
    Requires caller to handle transaction management.
    """
    with connection.cursor() as cursor:
        cursor.execute(sql.PAYOUT_CONTRACT, args={
            'contract_id': contract_id
        })


def cancel_contracts(*contract_ids):
    """
    Fails multiple contracts.
    Requires caller to handle transaction management.
    """
    logger.info('Cancelling contracts with ids: %s', contract_ids)
    with connection.cursor() as cursor:
        cursor.execute(sql.CANCEL_MULTIPLE_CONTRACTS, args={
            'contract_ids': contract_ids
        })


def get_transferable_contracts(from_agent_id, to_agent_id):
    logger.info('Getting contracts transferable from %s to %s', from_agent_id, to_agent_id)
    with connection.cursor() as cursor:
        cursor.execute(sql.GET_TRANFERABLE_CONTRACTS, args={
            'from_agent_id': from_agent_id,
            'to_agent_id': to_agent_id
        })

        results = cursor.fetchall()

    return (Contract(*row) for row in results)


def transfer_contracts(new_owner_id, contract_ids):
    """
    Updates contracts specified by contract_id so that the owner references new_owner_id.
    Requires caller to handle transaction management.
    """
    logger.info('transferring contracts %s to agent %s', contract_ids, new_owner_id)
    with connection.cursor() as cursor:
        cursor.execute(sql.TRANSER_CONTRACTS_TO_AGENT, args={
            'new_owner_id': new_owner_id,
            'contract_ids': tuple(contract_ids)
        })


def get_open_contracts_against_agent(agent_id):
    with connection.cursor() as cursor:
        cursor.execute(sql.GET_OPEN_CONTRACTS_AGAINST_AGENT, args={'target_id': agent_id})
    return (Contract(*row) for row in cursor.fetchall())
