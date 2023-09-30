
from typing import Literal

# "∀x Romano(x) ⇒ (Leal(x, Cesar) ⇔ Odia(x, Cesar))"


l = ['∀', '∃', '¬', '∧', '∨', '⇒', '⇔', '(', ')', ',', ' ']


def obtener_lado(cadena: str, char: str, lado: Literal['i', 'd']) -> str:

    step: int
    p1: str
    p2: str
    
    if lado == 'i':
        step = -1
        p1 = '('
        p2 = ')'
    else:
        step = 1
        p1 = ')'
        p2 = '('

    index = cadena.find(char)

    i = index

    parentesis = 0

    while parentesis != -1 and i < len(cadena) - 1 and i > 0:
        i += step
        char = cadena[i]

        if char == p2:
            parentesis += 1
        elif char == p1:
            parentesis -= 1
    
    res = (cadena[index+1:i+1] if lado == 'd' else cadena[i:index]).strip()

    if parentesis == -1:
        res = res[1:] if lado == 'i' else res[:-1]

    return res


def eliminar_bicondicional(cadena: str) -> str:
    """Elimina el bicondicional de la cadena de entrada."""

    lado_i = obtener_lado(cadena, '⇔', 'i')
    lado_d = obtener_lado(cadena, '⇔', 'd')

    return f"({lado_i} ⇒ {lado_d}) ∧ ({lado_d} ⇒ {lado_i})"

   


print(obtener_lado("∀x Romano(x) ⇒ (Leal(x, Cesar) ⇔ Odia(x, Cesar))", '⇒', 'i'))
