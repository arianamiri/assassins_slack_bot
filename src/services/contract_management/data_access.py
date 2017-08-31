from itertools import groupby

from utils.db import connection
from services.contract_management import sql


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

    return bool(count)
