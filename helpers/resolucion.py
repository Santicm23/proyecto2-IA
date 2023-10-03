
import time

from .reglas import cambiar_signo


def reducir_clausulas(clausula1: str, clausula2: str) -> str:
    """Reduce las clausulas de la lista de cadenas de entrada."""

    l1 = list(map(lambda x: x.strip(), clausula1.split('∨')))
    l2 = list(map(lambda x: x.strip(), clausula2.split('∨')))

    l1_inicial = l1.copy()
    l2_inicial = l2.copy()

    for el in l1:
        if cambiar_signo(el) in l2:
            l1.remove(el)
            l2.remove(cambiar_signo(el))

    if l1 == l1_inicial and l2 == l2_inicial:
        return clausula1

    return ' ∨ '.join(l1 + l2)


l:list= []

def inferencia_resolucion(clausulas: list[str], pregunta: str) -> bool:
    """Realiza la inferencia por resolución de la cadena de entrada."""

    estado_anterior = None
    estado = cambiar_signo(pregunta)

    while estado not in l:
        l.append(estado)
        estado_anterior = estado

        for clausula in clausulas:
            estado = reducir_clausulas(clausula, estado_anterior)

            if estado == '':
                return True
            elif estado not in clausulas and estado != estado_anterior:
                print(f'{estado_anterior} | {clausula} | {estado}')
                time.sleep(0.5)
                break
    return False
