
# "∀x Romano(x) ⇒ (Leal(x, Cesar) ⇔ Odia(x, Cesar))"


def eliminar_bicondicional(cadena: str) -> str:
    """Elimina el bicondicional de la cadena de entrada."""
    
    index = cadena.find("⇔")

    i = index

    char = ''
    closed_parentesis = 0

    while char != '(' or closed_parentesis != -1:
        i -= 1
        char = cadena[i]

        if char == ')':
            closed_parentesis += 1
        elif char == '(':
            closed_parentesis -= 1
    
    return cadena[i+1:index]

print(eliminar_bicondicional("∀x Romano(x) ⇒ (Leal(x, Cesar) ⇔ Odia(x, Cesar))"))
    