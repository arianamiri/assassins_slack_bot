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

    # TODO figure out a way to make this vary
    bounty = 1000

    for agent_id, possible_target_set in valid_target_lookup.iteritems():
        logger.info('assigning contract to %s', agent_id)

        # get a set of users who have not been assigned as a target in this round
        # and are in the user's set of valid targets
        targets = possible_target_set.intersection(all_agent_ids)
        logger.info('possible targets: %s', targets)

        if not targets:
            targets = possible_targets_set

        # grab random target
        target = targets.pop()

        logger.info('selected target: %s', target)

        data_access.assign_contract(agent_id, target, bounty)

        # book keeping for even distribution
        all_agent_ids.discard(target)

def _get_valid_targets():
    return data_access.get_available_targets_lookup()
