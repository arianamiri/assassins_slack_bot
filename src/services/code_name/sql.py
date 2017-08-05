GET_EXISITING_CODENAMES = """
    SELECT `code_name`
        FROM agents
    WHERE is_alive = 1;
"""
