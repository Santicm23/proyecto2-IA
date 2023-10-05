
from helpers.resolucion import inferencia_resolucion
from tests.ejemplos_clase import ejemplo1, ejemplo2, ejemplo3, ejemplo4


def main() -> None:

    print(inferencia_resolucion(ejemplo4['clausulas'], ejemplo4['pregunta']))
    


if __name__ == '__main__':
    main()
