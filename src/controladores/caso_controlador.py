from modelos.animal import Animal
from modelos.reporte_rescate import ReporteRescate
from servicios.animal_factory import obtener_fabrica
from servicios.gestor_casos import GestorCasos


class CasoControlador:
    """MVC: recibe la solicitud, valida y coordina el modelo y los servicios."""

    def __init__(self, vista):
        self._vista = vista
        self._gestor = GestorCasos()

    def registrar_reporte(self, descripcion, ubicacion, especie, reportante):
        if not descripcion or not ubicacion:
            self._vista.mostrar_error("La descripción y la ubicación son obligatorias.")
            return None
        animal = Animal(especie)
        reporte = ReporteRescate(descripcion, ubicacion, reportante, animal)
        reporte.expediente = obtener_fabrica(animal.especie).crear_expediente(animal)
        self._gestor.registrar_caso(reporte)
        self._vista.mostrar_confirmacion(reporte)
        return reporte

    def cambiar_estado(self, reporte, nuevo_estado):
        self._gestor.actualizar_estado(reporte, nuevo_estado)
        self._vista.mostrar_estado(reporte)

    def asignar_responsable(self, reporte, responsable):
        self._gestor.asignar_responsable(reporte, responsable)

    def listar_casos(self):
        self._vista.mostrar_casos(self._gestor.listar())
