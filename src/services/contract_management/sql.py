ASSIGN_CONTRACT = """
    INSERT INTO contracts
        (owner_id, target_id, bounty)
    VALUES
        (%(agent_id)s, %(target_id)s, %(bounty)s);
"""


GET_CURRENT_CONTRACTS_FOR_AGENT = """
    SELECT `target_id` FROM `contracts` where `owner_id` = %(agent_id)s;
"""


GET_OPEN_CONTRACTS_AGAINST_AGENT = """
    SELECT
        *
    FROM `contracts`
    WHERE
        `target_id` = %(target_id)s
        AND `is_open` = 1;
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


VALIDATE_CONTRACT = """
    SELECT contracts.*
    FROM contracts
        JOIN agents owner ON contracts.owner_id = owner.id
        JOIN agents target ON contracts.target_id = target.id
    WHERE owner.is_alive = 1
        AND target.is_alive = 1
        AND owner.id = %(owner_id)s
        AND target.id = %(target_id)s
        AND target.code_name = %(code_name)s;
"""


PAYOUT_CONTRACT = """
    UPDATE contracts
    SET
        is_open = 0,
        is_successful = 1
    WHERE id = %(contract_id)s;
"""


CANCEL_MULTIPLE_CONTRACTS = """
    UPDATE contracts
    SET
        is_open = 0,
        is_successful = 0
    WHERE id IN %(contract_ids)s;
"""


GET_TRANFERABLE_CONTRACTS = """
    SELECT a.*
    FROM contracts a
    WHERE a.is_open = 1
          AND a.owner_id = %(from_agent_id)s
          AND a.target_id != %(to_agent_id)s
          AND NOT EXISTS(SELECT 1
                          FROM contracts b
                         WHERE b.is_open = 1
                          AND b.owner_id = %(to_agent_id)s
                          AND b.target_id = a.target_id);
"""


TRANSER_CONTRACTS_TO_AGENT = """
    UPDATE contracts
        SET
            owner_id = %(new_owner_id)s
        WHERE
            id in %(contract_ids)s;
"""
