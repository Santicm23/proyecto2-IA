
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
    