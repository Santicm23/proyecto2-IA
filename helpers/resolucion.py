
import time

from .reglas import cambiar_signo

def reducir_elemento(clausula: str, elemento: str) -> str:
    """Reduce los elementos de la lista de cadenas de entrada."""

    l_clausula = clausula.split('∨')
    l_clausula = list(map(lambda x: x.strip(), l_clausula))
    try:
        l_clausula.remove(cambiar_signo(elemento))
    except ValueError:
        pass

    return ' ∨ '.join(l_clausula)


def reducir_clausulas(clausula1: str, clausula2: str) -> str:
    clausula = reducir_elemento(clausula1, clausula2)

    if clausula == clausula1:
        clausula = reducir_elemento(clausula2, clausula1)
    
    return clausula


def inferencia_resolucion(clausulas: list[str], pregunta: str) -> bool:
    """Realiza la inferencia por resolución de la cadena de entrada."""

    estado_anterior = None
    estado = cambiar_signo(pregunta)

    while estado != estado_anterior:
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
