from abc import ABC, abstractmethod

from modelos.expediente import ExpedienteFaunaSilvestre, ExpedienteGato, ExpedientePerro


class AnimalFactory(ABC):
    """Factory Method: cada subclase decide qué expediente crear."""

    @abstractmethod
    def crear_expediente(self, animal):
        pass


class FabricaPerro(AnimalFactory):
    def crear_expediente(self, animal):
        return ExpedientePerro(animal)


class FabricaGato(AnimalFactory):
    def crear_expediente(self, animal):
        return ExpedienteGato(animal)


class FabricaFaunaSilvestre(AnimalFactory):
    def crear_expediente(self, animal):
        return ExpedienteFaunaSilvestre(animal)


_FABRICAS = {
    "perro": FabricaPerro,
    "gato": FabricaGato,
    "fauna silvestre": FabricaFaunaSilvestre,
}


def obtener_fabrica(especie):
    """Mecanismo de selección: para una nueva especie se agrega una entrada."""
    try:
        return _FABRICAS[especie]()
    except KeyError:
        raise ValueError(f"Especie no soportada: {especie}")
