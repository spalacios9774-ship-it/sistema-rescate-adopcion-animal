from servicios.notificaciones import PublicadorEventos


class GestorCasos:
    """Singleton: una única instancia coordina todos los casos de rescate."""

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._casos = []
            cls._instancia.publicador = PublicadorEventos()
        return cls._instancia

    def registrar_caso(self, reporte):
        self._casos.append(reporte)
        self.publicador.emitir("nuevo caso de rescate", reporte)      # RF08

    def asignar_responsable(self, reporte, responsable):
        reporte.responsable = responsable

    def actualizar_estado(self, reporte, nuevo_estado):
        reporte.animal.cambiar_estado(nuevo_estado)
        self.publicador.emitir(f"cambio de estado a '{nuevo_estado}'", reporte)

    def listar(self):
        return list(self._casos)
