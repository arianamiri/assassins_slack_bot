import logging

from services import agent_management
from services import contract_management
from utils.db import db_transaction


logger = logging.getLogger()


@db_transaction()
def close_contract(agent_handle, target_handle, code_name):
    logger.info('Processing request to close contract')
    assassin, deceased_agent = agent_management.get_agents_by_handle(agent_handle, target_handle)
    contract = contract_management.is_contract_valid(assassin, deceased_agent, code_name)

    if contract:
        logger.info('Valid contract found.')
        # Reward the assassin
        contract_management.payout_contract(contract)

        # Retrieve all contracts that were open against the agent and cancel them.
        # NOTE: We could have closed all contracts against the agent in a single query,
        # but we are doing it in 2 so that we can notify the owners of the contracts that
        # they were cancelled.
        contracts_to_cancel = contract_management.get_contracts_against_agent(deceased_agent)
        contract_management.cancel_contracts(*contracts_to_cancel)
        return True
    else:
        # TODO NOTIFY THE USER THAT HIS CONTRACT IS NOT VALID.
        # THIS MAY REQUIRE SOME EXTRA VALIDATION (WRONG CODE NAME VS NO CONTRACT)
        return False
