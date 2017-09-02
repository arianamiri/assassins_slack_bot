import logging
import random

from services import agent_management
from services.contract_management import data_access


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def assign_contracts():
    """
    Assign every player a new contract

    Every player should get contract unless they already have contracts open
    against every other player.
    """
    # We are going to keep track of every agent who has a contract opened against
    # them in this round of assignments.  This is to ensure of an even distribution of targets
    all_agent_ids = set(agent.id for agent in agent_management.get_all_agents())

    # map of agent_id -> to a set of other agent_ids that are able to be have
    # a new contract added against them.
    valid_target_lookup = _get_valid_targets()

    max_bounty = _get_max_bounty()

    contract_params = []
    for agent_id, possible_target_set in valid_target_lookup.iteritems():
        logger.info('assigning contract to %s', agent_id)

        # get a set of users who have not been assigned as a target in this round
        # and are in the user's set of valid targets
        targets = possible_target_set.intersection(all_agent_ids)
        logger.info('possible targets: %s', targets)

        if not targets:
            targets = possible_target_set

        if targets:
            # grab random target
            target = targets.pop()

            contract_params.append({
                'target_id': target,
                'agent_id': agent_id,
                'bounty': int(max_bounty * _get_bounty_modifier())
            })
            # book keeping for even distribution
            all_agent_ids.discard(target)

    data_access.assign_multiple_contracts(contract_params=contract_params)


def is_contract_valid(assassin, deceased_agent, code_name):
    return data_access.is_contract_valid(assassin.id, deceased_agent.id, code_name)


def payout_contract(contract):
    data_access.payout_contract(contract.id)


def _get_valid_targets():
    return data_access.get_available_targets_lookup()


def _get_max_bounty():
    """
    The max bounty will 1.25x the existing bounty
    """
    existing_max = data_access.get_current_max_bounty()

    if existing_max:
        return int(1.25 * existing_max)

    return 1000


def _get_bounty_modifier():
    modifiers = (.5, .75, 1)
    return modifiers[random.randint(0, 2)]
