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
        ON NOT exists(SELECT 1
                      FROM contracts
                      WHERE owner_id = asignee.id AND target_id = possible_targets.id)
           AND asignee.id != possible_targets.id
    ORDER BY asignee.id;
"""


GET_MAX_BOUNTY = """
    SELECT max(`bounty`) from `contracts`;
"""
