class Animal:
    """Animal rescatado: conserva su especie y su estado."""

    ESTADOS = ("reportado", "rescatado", "en tratamiento", "disponible para adopción")

    def __init__(self, especie, nombre="Sin nombre"):
        self.especie = especie.lower()      # perro, gato o fauna silvestre
        self.nombre = nombre
        self.estado = "reportado"

    def cambiar_estado(self, nuevo):
        if nuevo not in self.ESTADOS:
            raise ValueError(f"Estado no válido: {nuevo}")
        self.estado = nuevo
