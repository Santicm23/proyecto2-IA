
from typing import TypedDict

Clausulas = TypedDict('Clausulas', {
    'clausulas': list[str],
    'pregunta': str
})


def leer_clausulas(ruta: str) -> Clausulas:
    """Lee las clausulas de un archivo."""

    with open(ruta, 'r', encoding='utf-8') as f:
        clausulas = f.read().splitlines()

    pregunta = clausulas.pop()

    clausulas = list(filter(lambda x: x != '', clausulas))
    clausulas = list(map(lambda x: x[3:], clausulas))

    return {
        'clausulas': clausulas,
        'pregunta': pregunta
    }
