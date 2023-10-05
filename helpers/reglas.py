
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

    return list(re.findall(regex, clausula))


def obtener_constantes(clausula: str) -> list[str]:
    """Obtiene las variables de una clausula."""

    regex = r'\(([^)]+)\)'

    l: list[str] = []

    for item in re.findall(regex, clausula):
        if ',' in item:
            l += item.split(',')
        else:
            l.append(item)

    return list(filter(lambda s: not s.islower(), l))


def reemplazar_variable(clausula: str, variable: str, constante: str) -> str:
    """Reemplaza la variable de la clausula por la constante."""
    clausula = clausula.replace(f"({variable})", f"({constante})")
    clausula = clausula.replace(f"({variable},", f"({constante},")
    clausula = clausula.replace(f",{variable})", f",{constante})")
    clausula = clausula.replace(f",{variable},", f",{constante},")

    return clausula
