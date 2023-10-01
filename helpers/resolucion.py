
from helpers.reglas import cambiar_signo


def reducir_elemento(clausula: str, elemento: str) -> str:
    """Reduce los elementos de la lista de cadenas de entrada."""

    l = clausula.split('∨')
    l = list(map(lambda x: x.strip(), l))
    l.remove(cambiar_signo(elemento))

    return ' ∨ '.join(l)


def inferencia_resolucion(clausulas: list[str], pregunta: str) -> bool:
    """Realiza la inferencia por resolución de la cadena de entrada."""

    


print(reducir_elemento('¬Niño(Scrooge) ∨ Ama(Scrooge,PapáNoel)', 'Niño(Scrooge)'))
