ASSIGN_CONTRACT = """
    INSERT INTO contracts
        (owner_id, target_id, bounty)
    VALUES
        (%(agent_id)s, %(target_id)s, %(bounty)s);
"""


GET_CURRENT_CONTRACTS_FOR_AGENT = """
    SELECT `target_id` FROM `contracts` where `owner_id` = %(agent_id)s;
"""


GET_AVAILABLE_TARGETS_FOR_ALL_AGENTS = """
    SELECT
      asignee.id,
      possible_targets.id
    FROM `agents` asignee
      JOIN `agents` possible_targets
        ON NOT EXISTS(SELECT 1
                      FROM contracts
                      WHERE owner_id = asignee.id AND target_id = possible_targets.id)
           AND asignee.id != possible_targets.id
    ORDER BY asignee.id;
"""


GET_MAX_BOUNTY = """
    SELECT max(`bounty`) from `contracts`;
"""

# TODO handle reverse assassination
CONTRACT_VALIDATION = """
    SELECT 1
    FROM contracts
        JOIN agents owner ON contracts.owner_id = owner.id
        JOIN agents target ON contracts.target_id = target.id
    WHERE owner.is_alive = 1
        AND target.is_alive = 1
        AND owner.slack_handle = %(owner_handle)s
        AND target.slack_handle = %(target_handle)s
        AND target.code_name = %(code_name)s
"""


STEAL_CONTRACTS = """
    INSERT INTO `contracts` (owner_id, target_id, bounty)
      SELECT
        %(new_owner_id)s,
        target_id,
        bounty
      FROM `contracts` c
      WHERE c.owner_id = %(old_owner_id) AND c.is_open = 1 AND c.target_id != %(new_owner_id)s
            AND NOT EXISTS(SELECT 1
                           FROM contracts
                           WHERE owner_id = %(new_owner_id)s AND target_id = c.target_id AND is_open = 1);
"""


GET_OPEN_CONTRACTS_FOR_AGENT = """
    SELECT * FROM `contracts`
    WHERE (owner_id = %(agent_id)s OR target_id = %(agent_id)s)
        AND is_open = 1;
"""


FAIL_CONTRACTS_BY_ID = """
    UPDATE `contracts`
    SET is_open = 0, is_successful = 0
    WHERE is_open = 1
        AND id IN %(contract_ids)s;
"""


SUCCEED_CONTRACT_BY_ID = """
    UPDATE `contracts`
    SET is_open = 0, is_successful = 1
    WHERE id = %(contract_id)s;
"""


FAIL_CONTRACTS_OWNED_BY_AGENT = """
    UPDATE `contracts`
    SET is_open = 0, is_successful = 0
    WHERE owner_id = %(agent_id)s
        AND is_open = 1;
"""
