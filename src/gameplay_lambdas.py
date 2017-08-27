import json
import logging

import gameplay


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def close_contract(event, context):
    payload = json.loads(event['body'])

    agent = payload.get('agent_handle')
    target = payload.get('target_handle')
    code_name = payload.get('code_name')

    debug = gameplay.close_contract(agent, target, code_name)

    debug = '   '.join(debug)

    return {
        "statusCode": 202,
        "headers": {},
        "body": debug
    }
