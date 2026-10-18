from abc import ABC, abstractmethod


class Observador(ABC):
    @abstractmethod
    def actualizar(self, evento, reporte):
        pass


class PublicadorEventos:
    """Observer: emite eventos de rescate a los componentes suscritos."""

    def __init__(self):
        self._observadores = []
        self.fallidas = []          # notificaciones que fallaron, para reintentar

    def suscribir(self, observador):
        self._observadores.append(observador)

    def cancelar(self, observador):
        self._observadores.remove(observador)

    def emitir(self, evento, reporte):
        for o in self._observadores:
            try:
                o.actualizar(evento, reporte)
            except Exception as error:
                self.fallidas.append((o, evento, reporte))
                print(f"[Aviso] Falló {type(o).__name__}: {error}")

    def reintentar_fallidas(self):
        pendientes, self.fallidas = self.fallidas, []
        for o, evento, reporte in pendientes:
            self.emitir(evento, reporte)


class NotificadorVoluntarios(Observador):
    def actualizar(self, evento, reporte):
        print(f"[Notificación a voluntarios] {evento}: {reporte.id} en {reporte.ubicacion}")


class TableroRefugio(Observador):
    def actualizar(self, evento, reporte):
        print(f"[Tablero del refugio] {evento}: {reporte.id} ({reporte.animal.especie})")
