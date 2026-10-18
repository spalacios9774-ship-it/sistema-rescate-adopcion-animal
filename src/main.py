import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from controladores.caso_controlador import CasoControlador
from modelos.usuario import Ciudadano, Voluntario
from vistas.caso_vista import CasoVista


def main():
    controlador = CasoControlador(CasoVista())
    ciudadano = Ciudadano("María", "maria@correo.com")

    r1 = controlador.registrar_reporte("Perro herido en la vía", "Av. Principal", "perro", ciudadano)
    controlador.registrar_reporte("Gato atrapado en un árbol", "Parque Central", "gato", ciudadano)
    controlador.registrar_reporte("Búho caído", "Mercado Sur", "fauna silvestre", ciudadano)

    controlador.asignar_responsable(r1, Voluntario("Luis", "luis@refugio.org"))
    controlador.cambiar_estado(r1, "rescatado")

    print("\nCasos registrados:")
    controlador.listar_casos()


if __name__ == "__main__":
    main()
