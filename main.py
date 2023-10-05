
from helpers.resolucion import inferencia_resolucion
from tests.ejemplos_clase import ejemplo1, ejemplo2, ejemplo3, ejemplo4, ejemplo5
from helpers.archivo import leer_clausulas


def main() -> None:

    ejemplo = leer_clausulas('tests/ejemplo-archivo.txt')

    print(inferencia_resolucion(ejemplo['clausulas'], ejemplo['pregunta']))


if __name__ == '__main__':
    main()
