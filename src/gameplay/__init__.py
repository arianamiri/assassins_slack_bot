from services import agent_management
from utils.db import db_transaction


@db_transaction()
def close_contract(agent_handle, target_handle, code_name):
    assassin, deceased_agent = agent_management.get_agents_by_handle(agent_handle, target_handle)
    # TODO debug return
    return assassin.agent_name, deceased_agent.agent_name
