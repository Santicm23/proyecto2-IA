
import re

def cambiar_signo(elemento: str) -> str:
    """Cambia el signo de la cadena de entrada."""

    if elemento[0] == '¬':
        return elemento[1:]
    else:
        return '¬' + elemento


def obtener_variables(clausula: str) -> list[str]:
    """Obtiene las variables de una clausula."""

    regex = r'\b[a-z][a-z1-9]*\b'

    return re.findall(regex, clausula)
