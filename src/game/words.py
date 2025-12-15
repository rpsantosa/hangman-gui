import random

WORDS = [
    "GATO",
    "BOLA",
    "CASA",
    "LUA",
    "UVA",
    "SUCO",
    "DADO",
    "PATO"
]

def escolher_palavra() -> str:
    return random.choice(WORDS)