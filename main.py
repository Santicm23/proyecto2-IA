
from helpers.resolucion import inferencia_resolucion
from tests.ejemplos_clase import ejemplo1, ejemplo2


def main() -> None:

    print(inferencia_resolucion(ejemplo2['clausulas'], ejemplo2['pregunta']))


if __name__ == '__main__':
    main()
