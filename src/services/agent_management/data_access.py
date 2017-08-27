from collections import namedtuple
import logging

from utils.db import connection
from services.agent_management import sql


logger = logging.getLogger()
logger.setLevel(logging.INFO)


Agent = namedtuple('Agent', (
    'id',
    'agent_name',
    'code_name',
    'handle',
    'is_mod',
    'is_alive'
))


def get_all():
    with connection.cursor() as cursor:
        cursor.execute(sql.GET_ALL_AGENTS)
        results = cursor.fetchall()

    return (Agent(*row) for row in results)


def get_assassinated_players():
    with connection.cursor() as cursor:
        cursor.execute(sql.GET_ASSASSINATED_PLAYERS)
        results = cursor.fetchall()

    return (Agent(*row) for row in results)


def assign_codenames(agents_and_codenames):
    logger.info('Beginning codename assignment')
    case_clause_template = 'WHEN {agent_id} THEN "{codename}"'
    case_clauses = []
    agent_ids = []
    for agent, codename in agents_and_codenames:
        logger.info('Attempting to assign codename "%s" to agent %s', codename, agent.id)
        agent_ids.append(agent.id)
        case_clauses.append(
            case_clause_template.format(agent_id=agent.id, codename=codename))

    case_clauses = ' '.join(case_clauses)

    update_sql = sql.ASSIGN_CODENAMES_TO_AGENTS.format(cases=case_clauses)
    with connection.cursor() as cursor:
        cursor.execute(update_sql, args={'agent_ids': agent_ids})
    connection.commit()

    logger.info('Codename assignment was successful')


def revive_assassinated_agents():
    logger.info('Reviving all assassinated agents')
    with connection.cursor() as cursor:
        cursor.execute(sql.REVIVE_ASSASSINATED_AGENTS)
    connection.commit()
    logger.info('Player revival was successful')


def get_agents_by_handles(*agent_handles):
    with connection.cursor() as cursor:
        cursor.execute(sql.GET_AGENTS_BY_HANDLE, args={'agent_handles': agent_handles})
        results = cursor.fetchall()

    return (Agent(*row) for row in results)


def assassinate_agent(agent):
    with connection.cursor() as cursor:
        cursor.execute(sql.ASSASSINATE_AGENT, args={'agent_id': agent.id})
