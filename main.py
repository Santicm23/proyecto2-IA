
from helpers.resolucion import inferencia_resolucion, reducir_clausulas_con_variables
from tests.ejemplos_clase import ejemplo1, ejemplo2


def main() -> None:

    # print(inferencia_resolucion(ejemplo1['clausulas'], ejemplo1['pregunta']))
    print(reducir_clausulas_con_variables('¬NarizRoja(x5) ∨ Raro(x5) ∨ Payaso(x5)', '¬Raro(Rodolfo)'))


if __name__ == '__main__':
    main()
