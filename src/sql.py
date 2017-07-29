ADD_PLAYERS = """
INSERT INTO `agents`
    (agent_name, slack_handle, is_moderator)
VALUES
    (%(agent_name)s, %(slack_handle)s, %(is_moderator)s);
"""
