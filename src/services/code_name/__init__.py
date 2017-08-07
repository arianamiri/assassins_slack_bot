from utils.db import connection
from services.code_name.generator import generate_codename
from services.code_name import sql


def generate_n_codenames(n):
    new_code_names = set()
    existing_codenames = set(_get_existing_codenames())
    while len(new_code_names) < n:
        new_code_name = generate_codename()
        if new_code_name not in existing_codenames:
            new_code_names.add(new_code_name)

    return new_code_names


def _get_existing_codenames():
    with connection.cursor() as cursor:
        cursor.execute(sql.GET_EXISITING_CODENAMES)
        return [row[0] for row in cursor.fetchall()]
