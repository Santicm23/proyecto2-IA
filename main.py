
import sys

from helpers.resolucion import inferencia_resolucion
from tests.ejemplos_clase import ejemplo1, ejemplo2, ejemplo3, ejemplo4, ejemplo5
from helpers.archivo import leer_clausulas


def main() -> None:
    """Función principal del programa."""

    ruta: str
    try:
        ruta = sys.argv.pop(1)
    except IndexError:
        print('No se ingreso la dirección del archivo.')
        return

    ejemplo = leer_clausulas(ruta)

    inferencia_resolucion(ejemplo['clausulas'], ejemplo['pregunta'])


if __name__ == '__main__':
    main()
