
# "∀x Romano(x) ⇒ (Leal(x, Cesar) ⇔ Odia(x, Cesar))"


def eliminar_bicondicional(cadena: str) -> str:
    """Elimina el bicondicional de la cadena de entrada."""
    
    index = cadena.find("⇔")

    i = index - 1

    char = ''
    closed_parentesis = 0

    while char != '(' or closed_parentesis != 0:
        char = cadena[i]
        i -= 1

        if char == ')':
            closed_parentesis += 1
        elif char == '(':
            closed_parentesis -= 1
    
    return cadena[i:index + 1]

print(eliminar_bicondicional("∀x Romano(x) ⇒ (Leal(x, Cesar) ⇔ Odia(x, Cesar))"))
    