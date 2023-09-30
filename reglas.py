
from typing import Literal

# "∀x Romano(x) ⇒ (Leal(x, Cesar) ⇔ Odia(x, Cesar))"

l = ['∧', '∨', '⇒', '⇔', '.']

def separacionElementos(cadena: str) -> list:
    """Elimina el bicondicional de la cadena de entrada."""
    lstrings= []
    lchars= []
    tamCadena = len(cadena)
    index=0
    char= ''
    i=0
    while i != tamCadena:
        char=cadena[i]
        if char in l:
            lchars.append(i)
        i+=1
        j: int =0
    for i in range(len(lchars)):
        cadenaux = ''
        while j != (lchars[i]):
            if cadena[j] not in l:
                cadenaux += cadena[j]
            j+=1
        lstrings.append(cadenaux)
        j=lchars[i]

    print(lstrings)

(separacionElementos("∀x Romano(x)⇒(Leal(x, Cesar)⇔Odia(x, Cesar))."))

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

def eliminar_implicacion(cadena: str) -> str:
    """Elimina la implicación de la cadena de entrada."""

    lado_i = obtener_lado(cadena, '⇒', 'i')
    lado_d = obtener_lado(cadena, '⇒', 'd')

    return f"¬{lado_i} ∨ {lado_d}"




print(eliminar_bicondicional("∀x Romano(x) ⇒ (Leal(x, Cesar) ⇔ Odia(x, Cesar))"))
