class CasoVista:
    """MVC: solo presenta información; no contiene reglas del negocio."""

    def mostrar_confirmacion(self, reporte):
        print(f">> Reporte {reporte.id} registrado ({reporte.animal.especie}, {reporte.ubicacion}).")

    def mostrar_estado(self, reporte):
        print(f">> Caso {reporte.id}: estado actual = {reporte.animal.estado}")

    def mostrar_casos(self, reportes):
        for r in reportes:
            responsable = r.responsable or "sin asignar"
            print(f"{r.id} | {r.animal.especie:15} | {r.animal.estado:25} | {responsable} | {r.expediente.descripcion()}")

    def mostrar_error(self, mensaje):
        print(f"!! {mensaje}")
