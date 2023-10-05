
import time

from .reglas import cambiar_signo, obtener_constantes, obtener_variables, reemplazar_variable


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


def reducir_clausulas_con_variables(clausula1: str, clausula2: str) -> str:
    """Reduce las clausulas de la lista de cadenas de entrada."""

    constantes1 = obtener_constantes(clausula1)
    variables1 = obtener_variables(clausula1)

    constantes2 = obtener_constantes(clausula2)
    variables2 = obtener_variables(clausula2)

    if len(variables1) == 0 and len(variables2) == 0:
        return reducir_clausulas(clausula1, clausula2)
    
    print(f'Variables 1: {variables1}')
    print(f'Variables 2: {variables2}')
    print(f'Constantes 1: {constantes1}')
    print(f'Constantes 2: {constantes2}')

    for constante in constantes1:
        for variable in variables2:
            clausula_temp = reemplazar_variable(clausula2, variable, constante)
            res = reducir_clausulas(clausula_temp, clausula1)
            if res != clausula1 and res != clausula_temp:
                return res

    for constante in constantes2:
        for variable in variables1:
            clausula_temp = reemplazar_variable(clausula1, variable, constante)
            res = reducir_clausulas(clausula_temp, clausula2)
            if res != clausula2 and res != clausula_temp:
                return res
    
    return clausula1


def inferencia_resolucion(clausulas: list[str], pregunta: str) -> bool:
    """Realiza la inferencia por resolución de la cadena de entrada."""
    l: list = []

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
