from datetime import datetime


class ReporteRescate:
    """Información del incidente reportado por un ciudadano."""

    _contador = 0

    def __init__(self, descripcion, ubicacion, reportante, animal):
        ReporteRescate._contador += 1
        self.id = f"RR-{ReporteRescate._contador:03d}"
        self.fecha = datetime.now()
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.reportante = reportante
        self.animal = animal
        self.responsable = None
        self.expediente = None
