class Expediente:
    """Historial de salud y atención de un animal."""

    def __init__(self, animal):
        self.animal = animal
        self.evaluaciones = []

    def registrar_evaluacion(self, texto):
        self.evaluaciones.append(texto)

    def descripcion(self):
        return f"Expediente de {self.animal.especie}"


class ExpedientePerro(Expediente):
    def descripcion(self):
        return "Expediente de perro (vacunas y esterilización)"


class ExpedienteGato(Expediente):
    def descripcion(self):
        return "Expediente de gato (pruebas de leucemia y esterilización)"


class ExpedienteFaunaSilvestre(Expediente):
    def descripcion(self):
        return "Expediente de fauna silvestre (permisos y plan de liberación)"
