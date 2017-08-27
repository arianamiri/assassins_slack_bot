from collections import namedtuple
from itertools import groupby

from utils.db import connection
from services.contract_management import sql


Contract = namedtuple('Contract', (
    'id',
    'owner_id',
    'target_id',
    'bounty',
    'is_open',
    'is_successful'
))


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


def is_contract_valid(agent_handle, target_handle, code_name):
    with connection.cursor() as cursor:
        count = cursor.execute(sql.CONTRACT_VALIDATION, args={
            'owner_handle': agent_handle,
            'target_handle': target_handle,
            'code_name': code_name
        })

    return bool(count)


def fail_contracts(contract_ids):
    with connection.cursor() as cursor:
        cursor.execute(sql.FAIL_CONTRACTS_BY_ID, args={
            'contract_ids': list(contract_ids)
        })


def succeed_contract(contract_id):
    with connection.cursor() as cursor:
        cursor.execute(sql.SUCCEED_CONTRACT_BY_ID, args={
            'contract_id': contract_id
        })


def get_open_contracts_for_agent(agent):
    with connection.cursor() as cursor:
        cursor.execute(
            sql.GET_OPEN_CONTRACTS_FOR_AGENT,
            args={'agent_id': agent.id}
        )

        results = cursor.fetchall()

    return (Contract(*row) for row in results)
