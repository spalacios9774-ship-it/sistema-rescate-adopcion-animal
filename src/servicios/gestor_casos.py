class GestorCasos:
    """Singleton: una única instancia coordina todos los casos de rescate."""

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._casos = []
        return cls._instancia

    def registrar_caso(self, reporte):
        self._casos.append(reporte)

    def asignar_responsable(self, reporte, responsable):
        reporte.responsable = responsable

    def actualizar_estado(self, reporte, nuevo_estado):
        reporte.animal.cambiar_estado(nuevo_estado)

    def listar(self):
        return list(self._casos)
