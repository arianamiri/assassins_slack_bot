from services.code_name.generator import generate_codename


def generate_n_codenames(n):
    new_code_names = set()
    while len(new_code_names) < n:
        new_code_names.add(generate_codename())
    return new_code_names


def _get_existing_codenames():
    with connection.cursor() as cursor:
        cursor.execute(sql.GET_EXISITING_CODENAMES)
        return [row[0] for row in cursor.fetchall()]
