
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


def reducir_clausulas_recursivo(
    clausula_reducir: str,
    clausula_reemplazar: str,
    constantes: list[str],
    variables: list[str],
) -> str:
    for constante in constantes:
        for variable in variables:
            clausula_temp = reemplazar_variable(clausula_reemplazar, variable, constante)
            res = reducir_clausulas(clausula_temp, clausula_reducir)
            if res != clausula_reducir and res != clausula_temp:
                return res
            else:
                consts_temp = list(filter(lambda x: x != constante, constantes))
                vars_temp = list(filter(lambda x: x != variable, variables))
                res = reducir_clausulas_recursivo(clausula_reducir, clausula_temp, consts_temp, vars_temp)
                if res != clausula_reducir and res != clausula_temp:
                    return res
    return clausula_reducir


def reducir_clausulas_con_variables(clausula1: str, clausula2: str) -> str:
    """Reduce las clausulas de la lista de cadenas de entrada."""

    constantes1 = obtener_constantes(clausula1)
    variables1 = obtener_variables(clausula1)

    constantes2 = obtener_constantes(clausula2)
    variables2 = obtener_variables(clausula2)

    res = reducir_clausulas(clausula1, clausula2)
    if res != clausula1 and res != clausula2:
        return res

    res = reducir_clausulas_recursivo(clausula1, clausula2, constantes1 + variables1, variables2)
    if res != clausula1 and res != clausula2:
        return res
    
    return reducir_clausulas_recursivo(clausula2, clausula1, constantes2 + variables2, variables1)


def inferencia_resolucion(clausulas: list[str], pregunta: str) -> bool:
    """Realiza la inferencia por resolución de la cadena de entrada."""
    l: list = []

    estado_anterior = None
    estado = cambiar_signo(pregunta)

    while estado not in l:
        l.append(estado)
        estado_anterior = estado

        for clausula in clausulas:
            estado = reducir_clausulas_con_variables(clausula, estado_anterior)

            if estado == '':
                print(f'{estado_anterior} | {clausula} | {estado}')
                return True
            elif estado not in clausulas and estado != estado_anterior:
                print(f'{estado_anterior} | {clausula} | {estado}')
                time.sleep(0.5)
                break
    return False
