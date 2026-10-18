class Usuario:
    """Datos comunes de identificación y acceso."""

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def __repr__(self):
        return f"{type(self).__name__}({self.nombre})"


class Ciudadano(Usuario):
    pass


class Voluntario(Usuario):
    pass


class Veterinario(Usuario):
    pass


class Administrador(Usuario):
    pass
