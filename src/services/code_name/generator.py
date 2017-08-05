import random

from services.code_name.parts import adjectives, animals


def generate_codename():
    adj = random.choice(adjectives)
    animal = random.choice(animals)
    return '{} {}'.format(adj, animal)
