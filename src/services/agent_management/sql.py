ADD_PLAYERS = """
    INSERT INTO `agents`
        (agent_name, slack_handle, is_moderator)
    VALUES
        (%(agent_name)s, %(slack_handle)s, %(is_moderator)s);
"""


GET_ALL_AGENTS = """
    SELECT * FROM `agents`;
"""


GET_ASSASSINATED_PLAYERS = """
    SELECT * FROM `agents` WHERE `is_alive` = 0;
"""


GET_AGENTS_BY_HANDLE = """
    SELECT * FROM `agents` WHERE `slack_handle` IN %(agent_handles)s;
"""


ASSIGN_CODENAMES_TO_AGENTS = """
    UPDATE `agents`
        SET `code_name` = CASE `id`
            {cases}
            ELSE `code_name`
            END
    WHERE `id` in %(agent_ids)s;
"""


REVIVE_ASSASSINATED_AGENTS = """
    UPDATE `agents`
        SET `is_alive` = 1
    WHERE `is_alive` = 0
"""


ASSASSINATE_AGENT = """
    UPDATE `agents`
        SET `is_alive` = 0
    WHERE `id` = %(agent_id)s;
"""
