import logging

from services import agent_management, contract_management
from utils.db import managed_transaction


logger = logging.getLogger()
logger.setLevel(logging.INFO)


@managed_transaction
def close_contract(agent_handle, target_handle, code_name):
    agent, target = agent_management.get_agents_by_handles(agent_handle, target_handle)
    if contract_management.is_contract_valid(agent_handle, target_handle, code_name):
        agent_management.assassinate_agent(target)
        targets_contracts, contracts_against_target = contract_management.get_open_contracts_for_agent(target)

        # TODO 2 transfer the targets contract to the agent
        contract_management.transfer_contracts_to_agent(targets_contracts, agent)

        # TODO 3 close the contract
        targets_contracts = tuple(targets_contracts)
        successful_contract = None
        for contract in targets_contracts:
            if contract.owner_id == agent.id:
                successful_contract = contract
                break

        contract_management.close_contract_successfully(successful_contract)

        # TODO 3 close all other contracts against the target
        failed_contracts = filter(lambda x: x.id != successful_contract.id, )
        contract_management.fail_contracts()

        # TODO 4 close the contract
        pass
    else:
        # TODO figure out why the contract is invalid
        # TODO notify the user about the failure
        pass
