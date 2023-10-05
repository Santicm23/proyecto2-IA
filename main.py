
from helpers.resolucion import inferencia_resolucion
from tests.ejemplos_clase import ejemplo1, ejemplo2, ejemplo3, ejemplo4, ejemplo5


def main() -> None:

    print(inferencia_resolucion(ejemplo3['clausulas'], ejemplo3['pregunta']))
    


if __name__ == '__main__':
    main()
