from services import agent_management
from services import contract_management
from utils.db import db_transaction


@db_transaction()
def close_contract(agent_handle, target_handle, code_name):
    assassin, deceased_agent = agent_management.get_agents_by_handle(agent_handle, target_handle)
    return contract_management.is_contract_valid(assassin, deceased_agent, code_name)
